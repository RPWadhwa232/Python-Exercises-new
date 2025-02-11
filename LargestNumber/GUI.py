import tkinter as tk

# creating the main window
root = tk.Tk()
root.title("My Application")

# adding text
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()


def on_click():
    print("Button cliked!")

# creating button
button = tk.Button(root, text="Click Me", command=on_click)
button.pack()

root.title("Calculator")

# Create three buttons
button1 = tk.Button(root, int = 1)
button2 = tk.Button(root, int = 2)
button3 = tk.Button(root, int = 3)

# Pack the buttons vertically
button1.pack()
button2.pack()
button3.pack()

# To run the application
root.mainloop()