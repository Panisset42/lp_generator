from lp_generator.IModel import IModel
import json


class page(IModel):
    def initialize(self, data):
        self.link  = data.get('link')
        self.name  = data.get('name')
        self.city  = data.get('city')
        self.date  = data.get('date')
        self.model = data.get('model')

    def run(self):
        print(f'running automation for model "{self.model}" into the city: {self.city}')
