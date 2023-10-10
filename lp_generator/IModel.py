
from abc import ABC, abstractmethod
class IModel(ABC):
    @abstractmethod
    def initialize(self, data):
        pass
    @abstractmethod
    def run(self):
        pass