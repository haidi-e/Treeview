import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Function to display record details in a message box
def show_record_details(event):
    item = tree.selection()[0]
    values = tree.item(item, "values")
    messagebox.showinfo("Record Details", f"Name: {values[0]}\nAge: {values[1]}\nGender: {values[2]}")

# Create the main window
root = tk.Tk()
root.title("Table with TreeView")

# Create a Treeview widget
tree = ttk.Treeview(root)
tree["columns"] = ("Name", "Age", "Gender")

# Define column headings
tree.heading("#0", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Gender", text="Gender")

# Add sample data to the Treeview
tree.insert("", "end", text="1", values=("John Doe", 00, "Male"))
tree.insert("", "end", text="2", values=("Damon", 00, "Male"))
tree.insert("", "end", text="3", values=("Peter", 00, "Male"))
tree.insert("", "end", text="4", values=("SD Jack", 00, "Male"))

# Bind double click event to show record details
tree.bind("<Double-1>", show_record_details)

# Add the Treeview to the window
tree.pack()

# Start the GUI event loop
root.mainloop()
