import tkinter as tk
from tkinter import filedialog

def process_file():
    # Open file dialog to select the file
    file_path = filedialog.askopenfilename(title="Select a .txt file", filetypes=[("Text Files", "*.txt")])

    if file_path:
        try:
            # Read the file
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Process the lines
            processed_lines = []
            for line in lines:
                processed_line = line.split('@')[0].strip() + '\n'
                processed_lines.append(processed_line)

            # Save the processed lines to a new file
            with open('users.txt', 'w') as new_file:
                new_file.writelines(processed_lines)

            status_label.config(text="File processed successfully!", fg="green")
        except Exception as e:
            status_label.config(text="Error: " + str(e), fg="red")

# Create the main window
root = tk.Tk()
root.title("Text File Processor")

# Create a button to trigger the file processing
process_button = tk.Button(root, text="Select and Process File", command=process_file)
process_button.pack(padx=10, pady=10)

# Create a label to display the status
status_label = tk.Label(root, text="")
status_label.pack(padx=10, pady=10)

# Start the GUI event loop
root.mainloop()