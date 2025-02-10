import os
from file import File
from directory import Directory


def build_filesystem_tree(path: str) -> Directory:
    if not os.path.exists(path) or not os.path.isdir(path):
        raise ValueError("Invalid directory path")

    root_name = os.path.basename(path) or path  # Handle root dirs
    root = Directory(root_name)

    for entry in os.scandir(path):
        if entry.is_file():
            root.add(File(entry.name, entry.stat().st_size))
        elif entry.is_dir():
            root.add(build_filesystem_tree(entry.path))

    return root