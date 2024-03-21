Command Executor
Command Executor is a Python application that provides a graphical user interface (GUI) for executing various file and directory commands. It allows users to interactively enter commands and view the output of those commands within the application.

Features
User-friendly Interface: The application features a simple and intuitive interface built using Tkinter, making it easy for users to interact with.

Command Execution: Users can enter commands directly into the provided input field. Upon clicking the "Execute" button, the application processes the command and displays the result in the output area.

Supported Commands:

Create Directory (dirmk): Creates a directory at the specified path with the given name.
Delete Directory (dirdel): Deletes a directory at the specified path with the given name.
Create File (filmk): Creates a file at the specified path with the given name.
Delete File (fildel): Deletes a file at the specified path with the given name.
Rename File (filren): Renames a file at the specified path from its current name to the new name provided.
Output Display: The application utilizes a scrollable text area to display the output of executed commands, providing users with clear feedback on the success or failure of each operation.

Requirements
Python: The application requires Python to be installed on the system.
Tkinter: Tkinter, Python's standard GUI library, is used for building the graphical interface.
Usage
Clone the Repository: Clone the repository containing the source code to your local machine, or download the source files directly.

Run the Application: Execute the command_executor.py file using Python. This will launch the Command Executor application window.

Enter Commands: Enter commands in the provided "Enter Command" input field. Supported commands follow a specific format (<command> <path> <name>), where applicable.

Execute Commands: Click the "Execute" button to execute the entered command. The output of the command will be displayed in the output area below.

View Output: Scroll through the output area to view the results of executed commands. The output will indicate whether the command was successful or if any errors occurred.
