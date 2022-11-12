import tkinter as tk
from tkinter import messagebox
import pandas as pd

class App(tk.Frame):
    def __init__(self, master):
      super().__init__(master)

      #################### text area para o link ##################
      linkLabel = tk.Label(master, text = "Database link (.csv):", font = ("Comic Sans",10))
      linkLabel.place(x = 0, y = 0)

      self.link = tk.StringVar()

      self.linkArea = tk.Entry(master, textvariable=self.link,width = 66, border = 2, relief = "ridge", highlightthickness=1, highlightcolor="blue")
      self.linkArea.bind('<Return>', lambda x: self.validateLink(self.link))
      self.linkArea.place(x = 3, y = 20)
      
      loadButton = tk.Button(master, text="Load", command = lambda: self.validateLink(self.link), bg = "ForestGreen", cursor="hand2")
      loadButton.place(x = 410, y = 18)

      ############### radiobuttons para o separador ###############
      self.sep = tk.StringVar()

      separatorLabel = tk.Label(master, text="Separator: ")
      separatorLabel.place(x = 70, y = 43)

      self.RadioVirgula = tk.Radiobutton(master, text="comma ( , )", variable=self.sep, value=',')
      self.RadioVirgula.place(x = 130, y = 43)

      self.RadioPontoVirgula = tk.Radiobutton(master, text="semicolon ( ; )", variable=self.sep, value=';')
      self.RadioPontoVirgula.place(x = 230, y = 43)
      self.RadioPontoVirgula.select()

      self.RadioPontoVirgula.config(state="disabled")
      self.RadioVirgula.config(state="disabled")

      ################### areas de texto e labels ##########################
      percepLabel = tk.Label(master, text="JustPerceptron", font = ("Comic Sans",9))
      percepLabel.place(x = 47, y = 73)
 
      self.percepText = tk.StringVar()
      percepBox = tk.Entry(master, textvariable=self.percepText, width=13, border = 2, relief = "ridge", highlightthickness=1, highlightbackground="blue", state="disabled", cursor="arrow")
      percepBox.place(x = 50, y = 93)

      #--------------#

      knnLAbel = tk.Label(master, text="K-NearestNeighbors", font = ("Comic Sans",9))
      knnLAbel.place(x = 160, y = 73)

      self.knnText = tk.StringVar()
      knnBox = tk.Entry(master, textvariable=self.knnText, width=13, border = 2, relief = "ridge", highlightthickness=1, highlightbackground="blue", state="disabled", cursor="arrow")
      knnBox.place(x = 178, y = 93)

      #--------------#

      oneRLabel = tk.Label(master, text="One Rule (1R)", font = ("Comic Sans",9))
      oneRLabel.place(x = 310, y = 73)

      self.oneRText = tk.StringVar()
      oneRBox = tk.Entry(master, textvariable=self.oneRText, width=13, border = 2, relief = "ridge", highlightthickness=1, highlightbackground="blue", state="disabled", cursor="arrow")
      oneRBox.place(x = 311, y = 93)

      ###############################################################
      self.doitButton = tk.Button(master, text="Do It!", command=None, font = ("Comic Sans",14), bg="green", fg="white", state="disabled", cursor="arrow")
      self.doitButton.place(x = 190, y = 123)
      

      #botão quit
      quitButton = tk.Button(
                          master, text="Quit", width=20, command=master.destroy,
                          height=1, bg="red3", fg="white", cursor="hand2"
                        )
      quitButton.pack(side="bottom", pady=2)

    #valida se há arquivo no link ou não
    #utiliza o try except para isso
    def validateLink(self, link):
      url = link.get()

      print(url)

      try:
        arq = pd.read_csv(url, sep = None, encoding='latin1')
      except:
        self.doitButton.config(state="disabled", cursor="arrow")
        self.RadioPontoVirgula.config(state="disabled")
        self.RadioVirgula.config(state="disabled")
        messagebox.showerror(title="Warning!", message= "Possible problems:\n" +
                                                        "1 - File does not exist in link/directory\n"+
                                                        "2 - File is not .csv\n"+
                                                        "3 - Unable to access the link")
      else:
        self.doitButton.config(state="normal", cursor="hand2")
        self.RadioPontoVirgula.config(state="normal")
        self.RadioVirgula.config(state="normal")

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
