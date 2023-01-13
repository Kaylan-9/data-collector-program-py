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
    self.master.config(bg= "#1C1C1C")
    self.config(bg= "#1C1C1C")
    self.set_menu()
    self.grid(row = 100, padx=(10, 10), pady=(10, 10))
    self.set_btn_generate()
    self.set_input_email_and_lbl()
    self.set_input_password_and_lbl()
    self.data_user = {
      "email": "",
      "password": ""
    }

  def set_btn_generate(self):
    self.btn_generate = Button(self, text="Coletar", command=self.function_btn_generate)
    self.btn_generate.grid(column=1, row=4)
    self.btn_generate.config(
      fg="black", 
      bg="#B0E0E6", 
      borderwidth=0, 
      padx=9, 
      pady=9
    )

  def set_input_email_and_lbl(self):
    self.input_email = Entry(self, width=33)
    self.label_email = Label(self)
    self.label_email.grid(column=0, row=0, padx=10, pady=10)
    self.input_email.grid(column=1, row=0)
    self.label_email.config(
      fg = "white",
      text = "*e-mail",
      bg= "#1C1C1C",
      font = ("Arial", 12, "bold"),
    )
    self.input_email.config(
      fg="black", 
      bg="white", 
      borderwidth=0, 
      font = ("Arial", 18),
      justify="center"
    )

  def set_input_password_and_lbl(self):
    self.input_password = Entry(self, width=33)
    self.label_password = Label(self)
    self.label_password.grid(column=0, row=1, padx=10, pady=10)
    self.input_password.grid(column=1, row=1)
    self.label_password.config(
      fg = "white",
      text = "*senha",
      bg= "#1C1C1C",
      font = ("Arial", 12, "bold"),
    )
    self.input_password.config(
      fg="black", 
      bg="white", 
      borderwidth=0, 
      font = ("Arial", 18),
      justify="center"
    )

  def set_menu(self):
    self.menu = Menu(self.master)
    self.master.config(menu=self.menu)
    self.optionsMenu = Menu(self.menu)
    self.menu.add_cascade(label="opções", menu=self.optionsMenu)
    self.optionsMenu.add_command(label="Sair", command=self.master.destroy)

  def function_btn_generate(self):
    self.data_user['email'] = self.input_email.get()
    self.data_user['password'] = self.input_password.get()
    with sync_playwright() as p:
      try:
        init(p, self.data_user)
      except ValueError:
        print(ValueError)


mywindow = Tk()
mywindow.wm_attributes("-transparentcolor", 'grey')
myapp = App(master=mywindow)
myapp.mainloop()