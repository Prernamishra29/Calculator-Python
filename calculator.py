import tkinter as tk

def on_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.configure(bg="lightgray")  # Set the background color

# Create an entry widget to display input and results
entry = tk.Entry(root, width=20, font=("Helvetica", 20))
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for digits and operations
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=("Helvetica", 15),
                       command=lambda t=text: on_click(t) if t != "=" else calculate())
    button.grid(row=row, column=col)
    button.configure(bg="skyblue")  # Set the background color for buttons

clear_button = tk.Button(root, text="C", width=5, height=2, font=("Helvetica", 15), command=clear)
clear_button.grid(row=5, column=0, columnspan=4)
clear_button.configure(bg="grey")  # Set the background color for the clear button

# Run the GUI event loop
root.mainloop()
