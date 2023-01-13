import tkinter as tk
from tkinter import *
from collect import init, sync_playwright

class App(tk.Frame):
  def __init__(self, master=None):
    super().__init__(master)
    options = {'padx': 5, 'pady': 5}
    self.pack(**options)
    self.master.state("zoomed")
    self.master = master 
    self.master.title("Coletor de dados para o facebook")
    self.grid()
    self.set_btn_quit(master)
    self.set_btn_generate(master)

  def set_btn_quit(self, master):
    self.btn_quit = Button(self, text="Sair", command=master.destroy)
    self.btn_quit.grid(column=0, row=0)
    self.btn_quit.config(fg="white", bg="#8B0000")

  def set_btn_generate(self, master):
    self.btn_quit = Button(self, text="Coletar", command=self.function_btn_generate)
    self.btn_quit.grid(column=1, row=0)
    self.btn_quit.config(fg="black", bg="#B0E0E6")

  def function_btn_generate(master):
    with sync_playwright() as p:
      try:
        init(p)
      except ValueError:
        print(ValueError)


myapp = App(master=Tk())
myapp.mainloop()