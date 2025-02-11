# main.py

import os
from directory import Directory
from file import File, format_size  # Import both File and the format_size function

def build_file_system(folder_path):
    """Recursively build the file system structure."""
    directory = Directory(os.path.basename(folder_path))
    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)
        if os.path.isdir(full_path):
            child_directory = build_file_system(full_path)
            directory.add(child_directory)
        else:
            size = os.path.getsize(full_path)
            file_component = File(item, size)
            directory.add(file_component)
    return directory

# Example usage
folder_to_explore = r"C:\python"  # Change this to your target directory
file_system = build_file_system(folder_to_explore)
file_system.display()
