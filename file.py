import os
from component import Component

class File(Component):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def draw(self, indent: int = 0):
        print(" " * indent + f"📄 {self.name} ({self.size} bytes)")