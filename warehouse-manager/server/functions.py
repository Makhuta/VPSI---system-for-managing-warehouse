from django.db import connection

def model_table_exists(model_class):
    return model_class._meta.db_table in connection.introspection.table_names()