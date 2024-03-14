# File and Directory Manipulation Script

This Python script provides functions to create, delete, and manipulate directories and files.

## Overview

The script offers a set of functions to interact with directories and files in a Python environment. It simplifies tasks such as creating directories, deleting directories, creating files, and deleting files.

## Functions

### `create_directory(path, name, overwrite=False)`

Creates a directory at a specified path.

- `path`: The path where the directory should be created.
- `name`: The name of the directory to be created.
- `overwrite` (optional): If `True`, the directory will be overwritten if it already exists.

### `delete_directory(path, name, hard_delete=False)`

Deletes a directory at a specified path.

- `path`: The path where the directory is located.
- `name`: The name of the directory to be deleted.
- `hard_delete` (optional): If `True`, the directory will be permanently deleted. Otherwise, it will be deleted only if it's empty.

### `create_file(path, name)`

Creates a file at a specified path.

- `path`: The path where the file should be created.
- `name`: The name of the file to be created.

### `delete_file(path, name)`

Deletes a file at a specified path.

- `path`: The path where the file is located.
- `name`: The name of the file to be deleted.

## Usage

To use these functions, import the script into your Python environment and call the functions as needed.

```python
import file_directory_operations as fdo

# Example: Create a directory
result = fdo.create_directory('/path/to/directory', 'example_directory')

# Example: Delete a file
result = fdo.delete_file('/path/to/directory', 'example_file.txt')

# Example: Create a file
result = fdo.create_file('/path/to/directory', 'example_file.txt')

This script relies on the built-in os module, which is part of the Python standard library.
