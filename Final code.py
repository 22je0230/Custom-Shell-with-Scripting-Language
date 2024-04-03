import tkinter as tk
from tkinter import scrolledtext
import os
import re
# Function to create a directory
def create_directory(path, name, overwrite=False):
    try:
        # Check if the directory already exists
        if os.path.exists(os.path.join(path, name)):
            if overwrite:
                os.rmdir(os.path.join(path, name))
            else:
                raise FileExistsError("Directory already exists")
        
        # Create the directory
        os.mkdir(os.path.join(path, name))
        return f"Directory '{name}' created successfully at {path}"
    except FileNotFoundError:
        return f"Error: Path '{path}' not found"
    except PermissionError:
        return f"Error: Permission denied to create directory at {path}"
    except Exception as e:
        return f"Error: {str(e)}"

# Function to delete a directory
def delete_directory(path, name, hard_delete=False):
    try:
        # Check if the directory exists
        if not os.path.exists(os.path.join(path, name)):
            raise FileNotFoundError("Directory not found")

        # Delete the directory
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

# Function to create a file
def create_file(path, name):
    try:
        # Check if the file already exists
        if os.path.exists(os.path.join(path, name)):
            raise FileExistsError("File already exists")
        
        # Create the file
        with open(os.path.join(path, name), 'w') as f:
            f.write('')
        return f"File '{name}' created successfully at {path}"
    except FileNotFoundError:
        return f"Error: Path '{path}' not found"
    except PermissionError:
        return f"Error: Permission denied to create file at {path}"
    except Exception as e:
        return f"Error: {str(e)}"

# Function to delete a file
def delete_file(path, name):
    try:
        # Check if the file exists
        if not os.path.exists(os.path.join(path, name)):
            raise FileNotFoundError("File not found")

        # Delete the file
        os.remove(os.path.join(path, name))
        return f"File '{name}' deleted successfully from {path}"
    except FileNotFoundError:
        return f"Error: File '{name}' not found at {path}"
    except PermissionError:
        return f"Error: Permission denied to delete file at {path}"
    except Exception as e:
        return f"Error: {str(e)}"

# Function to rename a file
def rename_file(path, name, new_name):
    try:
        # Check if the file exists
        if not os.path.exists(os.path.join(path, name)):
            raise FileNotFoundError("File not found")

        # Rename the file
        os.rename(os.path.join(path, name), os.path.join(path, new_name))
        return f"File '{name}' renamed to '{new_name}' successfully"
    except FileNotFoundError:
        return f"Error: File '{name}' not found at {path}"
    except PermissionError:
        return f"Error: Permission denied to rename file at {path}"
    except Exception as e:
        return f"Error: {str(e)}"

# Function to execute the command entered by the user
def execute_command():
    command_input = command_entry.get()
    command, path, name, options = parse_command(command_input)
    
    if command == "dirmk":
        if options == "-h":
            result = create_directory(path, name, overwrite=True)
        else:
            result = create_directory(path, name)
    elif command == "dirdel":
        if options == "-h":
            result = delete_directory(path, name, hard_delete=True)
        else:
            result = delete_directory(path, name)
    elif command == "filmk":
        result = create_file(path, name)
    elif command == "fildel":
        result = delete_file(path, name)
    elif command == "filren":
        new_name = options.strip() if options else None
        if new_name:
            result = rename_file(path, name, new_name)
        else:
            result = "Error: New name not provided"
    else:
        result = "Error: Invalid command"
    
    output_area.insert(tk.INSERT, f"{result}\n")
    command_entry.delete(0, tk.END)

# Function to parse the command entered by the user
def parse_command(input_string):
    # Regular expressions to match the command, path, name, and options
    command_pattern = r'^(\w+) (\S+) (\S+)( -h)?$'
    
    # Match the input string with the regular expression
    match = re.match(command_pattern, input_string)
    
    if match:
        # Extract the matched groups
        command = match.group(1)
        path = match.group(2)
        name = match.group(3)
        options = match.group(4)
        
        # Check if options were provided and clean up the output
        options = options.strip() if options else None
        
        return command, path, name, options
    else:
        return None, None, None, None

# Create the main window
root = tk.Tk()
root.title("Command Executor")
root.geometry("500x300")  # Width x Height

# Create a frame for the command input
command_frame = tk.Frame(root)
command_frame.pack(padx=10, pady=10, fill=tk.X)

# Label for the command entry
command_label = tk.Label(command_frame, text="Enter Command:")
command_label.pack(side=tk.LEFT, padx=(0, 10))

# Command entry widget
command_entry = tk.Entry(command_frame)
command_entry.pack(side=tk.LEFT, expand=True, fill=tk.X)

# Button to execute the command
execute_button = tk.Button(command_frame, text="Execute", command=execute_command)
execute_button.pack(side=tk.LEFT, padx=(10, 0))

# ScrolledText widget for displaying the outputs
output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
output_area.pack(padx=10, pady=(0, 10), expand=True, fill=tk.BOTH)

root.mainloop()
