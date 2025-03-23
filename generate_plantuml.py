import ast
import sys
import os

# SQLite-friendly Django field type mapping
SQLITE_TYPE_MAP = {
    "CharField": "TEXT",
    "TextField": "TEXT",
    "IntegerField": "INTEGER",
    "DecimalField": "REAL",
    "DateTimeField": "DATETIME",
    "DateField": "DATE",
    "FloatField": "REAL",
    "BooleanField": "BOOLEAN",
    "ForeignKey": "INTEGER",  # will be shown as *_id
    "AutoField": "INTEGER",
    "BigIntegerField": "INTEGER",
    "SmallIntegerField": "INTEGER"
}

def get_sqlite_type(django_type):
    return SQLITE_TYPE_MAP.get(django_type, "TEXT")

def pluralize(name: str):
    return name if name.endswith('s') else f"{name}s"

class ModelVisitor(ast.NodeVisitor):
    def __init__(self):
        self.models = {}

    def visit_ClassDef(self, node):
        is_model = any(
            isinstance(base, (ast.Name, ast.Attribute)) and 
            (getattr(base, 'id', None) == "Model" or getattr(base, 'attr', None) == "Model")
            for base in node.bases
        )
        if is_model:
            model_name = node.name
            fields = []
            enums = {}
            raw_enum_defs = {}
            for stmt in node.body:
                if isinstance(stmt, ast.Assign):
                    if isinstance(stmt.value, ast.List) and all(isinstance(elt, ast.Tuple) for elt in stmt.value.elts):
                        enum_values = []
                        for elt in stmt.value.elts:
                            if isinstance(elt, ast.Tuple) and isinstance(elt.elts[0], ast.Str):
                                enum_values.append(elt.elts[0].s)
                        if enum_values:
                            raw_enum_defs[stmt.targets[0].id] = enum_values
                    elif isinstance(stmt.value, ast.Call):
                        field_type = stmt.value.func.attr if isinstance(stmt.value.func, ast.Attribute) else 'UNKNOWN'
                        args = stmt.value.args
                        fields.append((stmt.targets[0].id, field_type, args))
            for const_name, values in raw_enum_defs.items():
                suffix = const_name.lower().replace(model_name.lower() + "_", "")
                enums[suffix] = values
            self.models[model_name] = {'fields': fields, 'enums': enums}

def parse_models_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        tree = ast.parse(file.read())
    visitor = ModelVisitor()
    visitor.visit(tree)
    return visitor.models

def generate_plantuml(models):
    lines = ["@startuml", "hide circle"]
    relations = []

    # map model name -> pluralized table name
    model_table_map = {model_name: pluralize(model_name) for model_name in models}

    for model_name, model_data in models.items():
        table_name = model_table_map[model_name]
        lines.append(f"entity {table_name} {{")
        lines.append(f"    +id : INTEGER <<PK>>")
        for field_name, field_type, args in model_data["fields"]:
            if field_name == "id":
                continue
            if field_type == "ForeignKey":
                target_model = "UNKNOWN"
                if args and isinstance(args[0], (ast.Name, ast.Attribute, ast.Str)):
                    if isinstance(args[0], ast.Name):
                        target_model = args[0].id
                    elif isinstance(args[0], ast.Attribute):
                        target_model = args[0].attr
                    elif isinstance(args[0], ast.Str):
                        target_model = args[0].s
                lines.append(f"    {field_name}_id : INTEGER <<FK>>")
                if target_model in model_table_map:
                    target_table = model_table_map[target_model]
                    relations.append(f"{target_table} ||--o{{ {table_name}")
            elif field_name in model_data["enums"]:
                enum_vals = model_data["enums"][field_name]
                enum_str = ', '.join(f'"{val}"' for val in enum_vals)
                lines.append(f"    {field_name} : ENUM[{enum_str}]")
            else:
                field_sqlite_type = get_sqlite_type(field_type)
                lines.append(f"    {field_name} : {field_sqlite_type}")
        lines.append("}")

    lines.extend(relations)
    lines.append("@enduml")
    return "\n".join(lines)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Použití: python generate_plantuml.py path/to/models.py")
        sys.exit(1)

    model_path = sys.argv[1]
    if not os.path.exists(model_path):
        print("Failed to find:", model_path)
        sys.exit(1)

    models = parse_models_file(model_path)
    plantuml_code = generate_plantuml(models)
    print(plantuml_code)
