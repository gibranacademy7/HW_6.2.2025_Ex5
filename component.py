# component.py
from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def draw(self, indent: int = 0):
        pass