import tkinter as tk
from tkinter import scrolledtext

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
