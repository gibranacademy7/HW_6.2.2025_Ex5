# directory.py

from file import File  # Import the File class

class Directory:
    """Class representing a directory."""
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def get_size(self):
        return sum(child.get_size() for child in self.children)

    def display(self, indent=0):
        print(f"{' ' * indent}[{self.name}]")
        for child in self.children:
            child.display(indent + 4)
