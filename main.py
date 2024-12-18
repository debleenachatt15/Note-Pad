import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def new_file():
    global file_name
    file_name = None
    text_area.delete(1.0, tk.END)

def open_file():
    global file_name
    file_name = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text files", ".txt"), ("All files", ".*")]
    )
    if file_name:
        text_area.delete(1.0, tk.END)
        with open(file_name, "r") as file:
            text_area.insert(1.0, file.read())

def save_file():
    global file_name
    if file_name:
        with open(file_name, "w") as file:
            file.write(text_area.get(1.0, tk.END))
    else:
        save_as_file()

def save_as_file():
    global file_name
    file_name = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", ".txt"), ("All files", ".*")]
    )
    if file_name:
        with open(file_name, "w") as file:
            file.write(text_area.get(1.0, tk.END))

def exit_notepad():
    if messagebox.askyesno("Exit", "Do you really want to exit?"):
        root.destroy()

# Create the main application window
root = tk.Tk()
root.title("Python Notepad")
root.geometry("800x600")

# Create the Text Widget
text_area = tk.Text(root, font=("Arial", 12))
text_area.pack(expand=True, fill=tk.BOTH)

# Create the Menu Bar
menu_bar = tk.Menu(root)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_notepad)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add Menu Bar to Window
root.config(menu=menu_bar)

# Run the application
root.mainloop()
