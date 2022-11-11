import tkinter as tk
from tkinter import ttk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        #text area para o link
        linkLabel = tk.Label(master, text = "Link da base de dados:", font = ("Comic Sans",10))
        linkLabel.place(x = 0, y = 0)


        #botão quit
        quitButton = tk.Button(
                            master, text="Quit", width=20, command=master.destroy,
                            height=1, bg="red3", fg="white"
                          )
        quitButton.pack(side="bottom", pady=2)

        

root = tk.Tk()
root.title('Testing Classifiers')
root.geometry('450x200')
root.resizable(False, False)

icon = tk.PhotoImage(file = "icon.png")
root.iconphoto(False, icon)


#root.attributes("-alpha", 0.5)

myapp = App(root)
myapp.mainloop()
