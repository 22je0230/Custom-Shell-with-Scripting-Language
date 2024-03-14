import re

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
