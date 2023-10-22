import json
from time import sleep
from lp_generator.models.archive.originals.page import page as page
class M2(page):
    def initialize(self, data, driver):
        self.model = []
        self.driver = driver
        for pre_processed_model in data:
            self.model.append(pre_processed_model)
    def run(self):
        for data in self.model:
            with open(data,'r', encoding='utf-8') as f:
                info = json.load(f)
                self.driver.get(info["link"])
                sleep(10)
    pass
