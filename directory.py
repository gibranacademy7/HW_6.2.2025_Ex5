from component import Component

class Directory(Component):
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add(self, component: Component):
        self.children.append(component)

    def draw(self, indent: int = 0):
        print(" " * indent + f"📁 {self.name}")
        for child in self.children:
            child.draw(indent + 2)