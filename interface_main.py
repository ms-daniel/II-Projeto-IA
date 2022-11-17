import tkinter as tk
from interface.mainFrame import App

root = tk.Tk()
root.title('Testing Classifiers')

#selecionar frame no centro da tela
sW = root.winfo_screenwidth()  #retorna o largura da tela do user
sH = root.winfo_screenheight() #retorna a altura da tela do user

width = 450
height = 200
sW = (sW/2) - (width/2)
sH = (sH/2) - (height/2)

root.geometry('%dx%d+%d+%d' % (width, height, sW, sH))
##################################

root.resizable(False, False)

icon = tk.PhotoImage(file = "images\icon.png")
root.iconphoto(False, icon)

myapp = App(root)
myapp.mainloop()
