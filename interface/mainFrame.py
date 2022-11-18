import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
from modulos.back_test import test

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
    separatorLabel.place(x = 47, y = 45)

    self.RadioVirgula = tk.Radiobutton(master, text="comma ( , )", variable=self.sep, value=',')
    self.RadioVirgula.place(x = 104, y = 43)

    self.RadioPontoVirgula = tk.Radiobutton(master, text="semicolon ( ; )", variable=self.sep, value=';')
    self.RadioPontoVirgula.place(x = 190, y = 43)
    self.RadioPontoVirgula.select()

    self.RadioPontoVirgula.config(state="disabled")
    self.RadioVirgula.config(state="disabled")

    #Combobox para neighbors

    neighborsLabel = tk.Label(master, text="Neighbors: ")
    neighborsLabel.place(x = 298, y = 45)

    self.knnNeighbors = tk.StringVar()
    self.knnNeighborBox = ttk.Combobox(master, textvariable=self.knnNeighbors, width=2,
                                  state='readonly', values=('1', '2'))
    self.knnNeighborBox.config(state='disabled')
    self.knnNeighborBox.set(value=1)
    self.knnNeighborBox.place(x = 362, y = 45)

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
    self.doitButton = tk.Button(master, text="Do It!", command = lambda: self.do_it(self.link.get(), self.sep.get(),
                                self.knnNeighbors.get(), self.percepText, self.knnText, self.oneRText),
                                font = ("Comic Sans",14), bg="green", fg="white", state="disabled", cursor="arrow", width=13)
    self.doitButton.place(x = 243, y = 123)

    self.removeColumns = tk.Button(master, text="Select Columns", command = None, font = ("Comic Sans",14), bg="blue3",
                                      fg="white", state="disabled", cursor="arrow", activebackground="blue", activeforeground="black")
    self.removeColumns.place(x = 50, y = 123)

    #botão quit
    quitButton = tk.Button(
                        master, text="Quit", width=20, command= self.createTopLevelWindows,
                        height=1, bg="red3", fg="white", cursor="hand2"
                      )
    quitButton.pack(side="bottom", pady=2)

  def validateLink(self, link):
    """
        validate the link, directory and file extension
        :param link: string
    """
    url = link.get()

    try:
      self.arq = pd.read_csv(url, sep = None, encoding='latin1', engine='python')
      
    except:
      self.knnNeighborBox.config(state="disabled")
      self.doitButton.config(state="disabled", cursor="arrow")
      self.RadioPontoVirgula.config(state="disabled")
      self.RadioVirgula.config(state="disabled")
      self.removeColumns.config(state="disabled")
      self.removeColumns.bind('<Enter>', lambda x: None)
      messagebox.showerror(title="Warning!", message= "Possible problems:\n" +
                                                      "1 - File does not exist in link/directory\n"+
                                                      "2 - File is not .csv\n"+
                                                      "3 - Unable to access the link")
    else:
      
      x, columns = self.arq.shape
      self.removeColumns.config(state="normal")
      self.knnNeighborBox['values'] = [x+1 for x in range(columns-1)]
      self.knnNeighborBox.config(state="readonly")
      self.doitButton.config(state="normal", cursor="hand2")
      self.RadioPontoVirgula.config(state="normal")
      self.RadioVirgula.config(state="normal")

  def loadColumns(self):
    '''
      Creates a checkbox for each column of the csv
    '''
    j = 1
    #para cada coluna do arquivo ele adiciona um elemento na listbox
    #e associa um index(j) a ela, ao final a ulima coluna é removida
    #pois é a coluna de testes 
    for x in self.arq.columns:
      self.listColumns.insert(j, x)
      j+=1
    else:
      self.listColumns.delete(first=j-2)
      if j > 13:
        j = 13
      self.listColumns.config(height=j-2, width=30)
      

  def createTopLevelWindows(self):
    self.winTest = tk.Toplevel(padx=5, pady=5)
    self.winTest.resizable(width = 0, height = 0)
    self.winTest.title('Remove Columns')
    self.winTest.grab_set()

    scrollBar = tk.Scrollbar(self.winTest)
    scrollBar.pack(side="right", fill="both")

    self.listColumns = tk.Listbox(self.winTest, selectmode="multiple", selectbackground="green", background="red", foreground="white")
    self.loadColumns()
    self.listColumns.selection_set(first=0, last=self.listColumns.index("end"))
    self.listColumns.pack(expand = True, side = "left", fill = "both")

    self.listColumns.config(yscrollcommand = scrollBar.set)
    scrollBar.config(command = self.listColumns.yview)


  #def removeColumns():
    #Todo

  def do_it(self, link, separator, neighbors, varPercep, varKnn, varOneR):
    try:
      test(link, separator, int(neighbors), [varPercep, varKnn, varOneR])
    except:
      messagebox.showerror(title="Warning!", message= "the algorithm failed to run for some reason.\nMaybe you selected the wrong separator.")
      
