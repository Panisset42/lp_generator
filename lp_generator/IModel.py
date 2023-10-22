
from abc import ABC, abstractmethod
class IModel(ABC):
    @abstractmethod
    def initialize(self, data, driver):
        pass
    @abstractmethod
    def run(self):
        pass