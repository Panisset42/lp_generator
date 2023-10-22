from lp_generator.IModel import IModel
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

class page(IModel):
    def initialize(self, data, driver):
        self.data  = data
        self.driver = driver
    def run(self):
        pass
