import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        



root = tk.Tk()
root.title('Diabético?')
root.geometry('600x400')
root.resizable(False, False)
icon = tk.PhotoImage(file = "icon.png")
root.iconphoto(False, icon)
#root.attributes("-alpha", 0.5)

myapp = App(root)
myapp.mainloop()
