from Automats import Automates
from GUI import GUI
from tkinter import *
#Note: il faut s'assurer d'avoir la librairie (doit être installé sur linux)

auto = Automates("lexique6.txt")
root = Tk()
root.geometry('300x300')
gui = GUI(root, auto)
gui.mainloop()