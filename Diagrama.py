### Diagram:

# +----------------------+
# |   File               |
# +----------------------+
# | - name: str          |
# | - size: int          |
# +----------------------+
# | + __init__(name, size)|
# | + get_size()        |
# | + display(indent)    |
# +----------------------+
#
# +----------------------+
# |   Directory          |
# +----------------------+
# | - name: str          |
# | - children: List[FileComponent] |
# +----------------------+
# | + __init__(name)     |
# | + add(component)     |
# | + get_size()        |
# | + display(indent)    |
# +----------------------+
#
# +----------------------+
# |   format_size        |
# +----------------------+
# | + format_size(size_in_bytes) |
# +----------------------+


### Components of the Diagram

# 1. **File Class**:
#    - **Attributes**:
#      - `name`: The name of the file (type: `str`).
#      - `size`: The size of the file in bytes (type: `int`).
#    - **Methods**:
#      - `__init__(name, size)`: Constructor that initializes the file's name and size.
#      - `get_size()`: Returns the size of the file.
#      - `display(indent)`: Displays the file's name and its size in a human-readable format.

# 2. **Directory Class**:
#    - **Attributes**:
#      - `name`: The name of the directory (type: `str`).
#      - `children`: A list that holds child components (which can be `File` or `Directory` objects).
#    - **Methods**:
#      - `__init__(name)`: Constructor that initializes the directory's name and creates an empty list for children.
#      - `add(component)`: Adds a child component (file or directory) to the directory.
#      - `get_size()`: Calculates and returns the total size of all child components.
#      - `display(indent)`: Displays the directory's name and recursively calls the `display` method on its children.

# 3. **format_size Function**:
#    - This is a standalone function (not part of a class) that converts a given size in bytes to a human-readable format (KB, MB, GB).
#    - **Parameters**:
#      - `size_in_bytes`: Size in bytes to be formatted.
#    - **Returns**: A string representing the size in a human-readable format.

# ### Explanation of the Code Flow

# 1. **Building the File System**:
#    - The `main.py` script triggers the file system building by calling the `build_file_system` function.
#    - This function creates `Directory` instances for directories and `File` instances for files, recursively traversing the specified folder.

# 2. **Displaying the Structure**:
#    - The `display` method of the `Directory` class is called, which prints the directory's name.
#    - It then iterates through its children, calling their respective `display` methods to print each file or subdirectory in an indented format.
