from database.models import GeneratingModel

def generate_model(model: GeneratingModel, amount: int) -> None:
    for _ in range(amount):
        model.generate()