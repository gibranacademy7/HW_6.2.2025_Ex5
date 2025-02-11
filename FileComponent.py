import os


class FileComponent:
    """Abstract base class for file and directory components."""

    def get_size(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def display(self, indent=0):
        raise NotImplementedError("Subclasses should implement this method.")
