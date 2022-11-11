import tkinter as tk
from tkinter import messagebox
import pandas as pd

class App(tk.Frame):
    def __init__(self, master):
      super().__init__(master)

      #text area para o link
      linkLabel = tk.Label(master, text = "Link da base de dados:", font = ("Comic Sans",10))
      linkLabel.place(x = 0, y = 0)

      link = tk.StringVar()

      linkArea = tk.Entry(master, textvariable=link,width = 66, border = 2, relief = "ridge", highlightthickness=1, highlightcolor="blue")
      linkArea.bind('<Return>', lambda x: self.validateLink(link))
      linkArea.place(x = 3, y = 20)
      
      loadButton = tk.Button(master, text="Load", command = lambda: self.validateLink(link), bg = "ForestGreen")
      loadButton.place(x = 410, y = 18)

      #########
      percepLabel = tk.Label(master, text="JustPerceptron", font = ("Comic Sans",9))
      percepLabel.place(x = 47, y = 43)
 
      percepText = tk.StringVar()
      percepBox = tk.Entry(master, textvariable=percepText, width=13, border = 2, relief = "ridge", highlightthickness=1, highlightbackground="blue", state="disabled")
      percepBox.place(x = 50, y = 63)

      #--------------#

      knnLAbel = tk.Label(master, text="K-NearestNeighbors", font = ("Comic Sans",9))
      knnLAbel.place(x = 160, y = 43)

      knnText = tk.StringVar()
      knnBox = tk.Entry(master, textvariable=knnText, width=13, border = 2, relief = "ridge", highlightthickness=1, highlightbackground="blue", state="disabled")
      knnBox.place(x = 178, y = 63)

      #--------------#

      oneRLabel = tk.Label(master, text="One Rule (1R)", font = ("Comic Sans",9))
      oneRLabel.place(x = 310, y = 43)

      oneRText = tk.StringVar()
      oneRBox = tk.Entry(master, textvariable=oneRText, width=13, border = 2, relief = "ridge", highlightthickness=1, highlightbackground="blue", state="disabled")
      oneRBox.place(x = 311, y = 63)

      #--------------#
      doitButton = tk.Button(master, text="Do It!", command=None, font = ("Comic Sans",14), bg="green", fg="white", state="disabled")
      doitButton.place(x = 190, y = 100)
      

      #botão quit
      quitButton = tk.Button(
                          master, text="Quit", width=20, command=master.destroy,
                          height=1, bg="red3", fg="white"
                        )
      quitButton.pack(side="bottom", pady=2)
  
    def validateLink(self, link):
      url = link.get()
      try:
        dataBase = pd.read_csv(url, sep=',', encoding = 'latin1').values
      except:
        messagebox.showerror(title="Aviso!", message="Arquivo ou local não existe")

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

icon = tk.PhotoImage(file = "icon.png")
root.iconphoto(False, icon)

myapp = App(root)
myapp.mainloop()
