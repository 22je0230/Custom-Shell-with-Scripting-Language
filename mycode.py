import os

def create_directory(path, name, overwrite=False):
    try:
        if os.path.exists(os.path.join(path, name)):
            if overwrite:
                os.rmdir(os.path.join(path, name))
            else:
                raise FileExistsError("Directory already exists")
        
        os.mkdir(os.path.join(path, name))
        return f"Directory '{name}' created successfully at {path}"
    except FileNotFoundError:
        return f"Error: Path '{path}' not found"
    except PermissionError:
        return f"Error: Permission denied to create directory at {path}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_directory(path, name, hard_delete=False):
    try:
        if not os.path.exists(os.path.join(path, name)):
            raise FileNotFoundError("Directory not found")

        if hard_delete:
            os.rmdir(os.path.join(path, name))
        else:
            os.removedirs(os.path.join(path, name))
        return f"Directory '{name}' deleted successfully from {path}"
    except FileNotFoundError:
        return f"Error: Directory '{name}' not found at {path}"
    except PermissionError:
        return f"Error: Permission denied to delete directory at {path}"
    except Exception as e:
        return f"Error: {str(e)}"

def create_file(path, name):
    try:
        if os.path.exists(os.path.join(path, name)):
            raise FileExistsError("File already exists")
        
        with open(os.path.join(path, name), 'w') as f:
            f.write('')
        return f"File '{name}' created successfully at {path}"
    except FileNotFoundError:
        return f"Error: Path '{path}' not found"
    except PermissionError:
        return f"Error: Permission denied to create file at {path}"
    except Exception as e:
        return f"Error: {str(e)}"

def delete_file(path, name):
    try:
        if not os.path.exists(os.path.join(path, name)):
            raise FileNotFoundError("File not found")

        os.remove(os.path.join(path, name))
        return f"File '{name}' deleted successfully from {path}"
    except FileNotFoundError:
        return f"Error: File '{name}' not found at {path}"
    except PermissionError:
        return f"Error: Permission denied to delete file at {path}"
    except Exception as e:
        return f"Error: {str(e)}"

def rename_file(path, name, new_name):
    try:
        if not os.path.exists(os.path.join(path, name)):
            raise FileNotFoundError("File not found")

        os.rename(os.path.join(path, name), os.path.join(path, new_name))
        return f"File '{name}' renamed to '{new_name}' successfully"
    except FileNotFoundError:
        return f"Error: File '{name}' not found at {path}"
    except PermissionError:
        return f"Error: Permission denied to rename file at {path}"
    except Exception as e:
        return f"Error: {str(e)}"
