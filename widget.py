import tkinter as tk


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        b = tk.Button(self, text= "Hello")
        b.pack()



w = Window()
w.mainloop()
