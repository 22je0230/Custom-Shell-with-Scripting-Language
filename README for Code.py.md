# Command Execution Script

This Python script allows users to execute various file and directory manipulation commands through a simple command-line interface.

## Introduction

The script provides functionality to create directories, delete directories, create files, delete files, and rename files. Users can enter commands in a specific format to perform these operations.

## Usage

Users can execute commands in the following format:
- <command>: Specifies the operation to perform (dirmk for directory creation, dirdel for directory deletion, filmk for file creation, fildel for file deletion, filren for file renaming).
- <path>: Indicates the path where the directory or file should reside or be created.
- <name>: Specifies the name of the directory or file.
- [options] (optional): Additional flags or parameters. For instance, -h can be used for a hard delete.

## Functions

### execute_command()

Executes the command provided by the user. It parses the command, extracts relevant information, and invokes the appropriate functions to carry out the operation.

### parse_command(input_string)

Parses the user-entered command. It utilizes regular expressions to identify the command, path, name, and options. The parsed components are then returned.

## Dependencies

This script relies on the re module, which is part of the Python standard library.

## Installation

Simply download the script and run it using Python 3.x.

```bash
python command_execution script.py
File Structure
command_execution_script.py: Contains the main script with functions for executing and parsing commands.
