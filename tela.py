import tkinter as tk
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
        print(dataBase[:,:])
      except:
        print('Não há arquivos no local')


        

root = tk.Tk()
root.title('Testing Classifiers')
root.geometry('450x200')
root.resizable(False, False)

icon = tk.PhotoImage(file = "icon.png")
root.iconphoto(False, icon)


#root.attributes("-alpha", 0.5)

myapp = App(root)
myapp.mainloop()
