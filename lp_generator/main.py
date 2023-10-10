#
import importlib
import json
import os

from selenium import webdriver

from lp_generator.IModel import IModel
from pre_process_model import pre_process_model  # Import the pre_process_model class


def read_csv_file(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()[1:]  # Skip the header and read the rest


def login():
    driver = webdriver.Chrome()
    return driver


def pre_process():
    # File path to the CSV file
    csv_file_path = 'archives/csv/test.csv'

    # Read the CSV file
    csv_data = read_csv_file(csv_file_path)

    # Initialize the pre_process_model class
    model = pre_process_model()

    # Pass the CSV data to initialize
    model.initialize(csv_data)

    # Run the model
    model.run()


def import_model(pre_processed_model):
    with open(pre_processed_model, 'r') as f:
        pre_processed_data = json.load(f)
    model_name = pre_processed_data.get('model')

    if f"{model_name}.py" in os.listdir('./models'):
        module = importlib.import_module(f'models.{model_name}')

        model_class = [cls for cls in module.__dict__.values() if isinstance(cls, type) and issubclass(cls, IModel)][0]
        model_instance = model_class()
        model_instance.initialize(pre_processed_data)
        return model_instance


def get_pre_processed_models():
    pre_processed_models = []
    pre_processed_dir = './pre-models'
    for filename in os.listdir(pre_processed_dir):
        if filename.endswith('.json'):
            pre_processed_models.append(os.path.join(pre_processed_dir, filename))
    return pre_processed_models


def main():
    pre_process()
    # driver = login()
    pre_processed_models = get_pre_processed_models()

    for pre_processed_model in pre_processed_models:
       # Se for um modelo de agenda
       # enviar todos eles e ao final enviar um código de confirmacao
       # se nao, iniciar o processo de criação imediatamente

       model = import_model(pre_processed_model)
       model.run()


if __name__ == '__main__':
    main()
