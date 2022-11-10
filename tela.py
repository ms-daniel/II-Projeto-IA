import tkinter as tk
from tkinter import ttk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        button = tk.Button(
                            master, text="Quit", width=20, command=master.destroy,
                            height=1, bg="red3", fg="white"
                          )
        button.pack(side="bottom", pady=2)

        button2 = tk.Button(master, text='dan')
        button2.place(x=0,y=0)

root = tk.Tk()
root.title('Testing Classifiers')
root.geometry('600x400')
root.resizable(False, False)
icon = tk.PhotoImage(file = "icon.png")
root.iconphoto(False, icon)
#root.attributes("-alpha", 0.5)

myapp = App(root)
myapp.mainloop()
