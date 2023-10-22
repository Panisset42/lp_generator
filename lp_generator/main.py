#
import importlib
import json
import os
from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from lp_generator.IModel import IModel
from pre_process_model import pre_process_model  # Import the pre_process_model class


def read_csv_file(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()[1:]  # Skip the header and read the rest


def login():
    # get login info
    user_account = input("Insira o usuário: ")
    user_pass = input("Insira a senha: ")
    # instantiate driver and go to the site
    driver = webdriver.Chrome()
    driver.get('https://app.greatpages.com.br/login')
    # get camps and making login
    user_input = driver.find_element(By.XPATH, "//*[@id=\"usuario\"]")
    pass_input = driver.find_element(By.XPATH, "//*[@id=\"senha\"]")
    user_input.send_keys(user_account)
    pass_input.send_keys(user_pass)
    pass_input.submit()
    # returning driver
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


def import_model(class_name):
    model_dir = 'models'  # Note: Removed the leading './' for the package name
    package_name = 'models'  # Specify the package name

    for filename in os.listdir(model_dir):
        if filename.endswith(".py"):
            module_name = filename[:-3]  # Remove the '.py' extension
            module = importlib.import_module(f'{package_name}.{module_name}')

            # Check if the class exists in the module
            if hasattr(module, class_name):
                my_class = getattr(module, class_name)
                instance = my_class()
                return instance

    return None  # Class not found


def get_pre_processed_models():
    pre_processed_models = []
    pre_processed_dir = './pre-models'
    for filename in os.listdir(pre_processed_dir):
        if filename.endswith('.json'):
            pre_processed_models.append(os.path.join(pre_processed_dir, filename))
    return pre_processed_models


def main():
    pre_process()
    driver = login()
    needed_models = []
    pre_processed_models_path = []
    #verify the models that will be needed
    for archive in get_pre_processed_models():
        with open(archive,'r',encoding='utf-8') as f:
            archive_data = json.load(f)
            if archive_data["model"] not in needed_models:
                needed_models.append(archive_data["model"])
    # for each needed model generate a list and execute it
    for model in needed_models:
        process_batch = []
        for archive in get_pre_processed_models():
            with open(archive,'r',encoding='utf-8') as f:
                archive_data = json.load(f)
                if archive_data["model"] == model:
                    process_batch.append(archive)
        instance = import_model(model)
        instance.initialize(process_batch, driver)
        instance.run()

if __name__ == '__main__':
    main()
