from tkinter import *
from Automats import Automates

class GUI(Frame):
    def __init__(self, master=None, graph = None):
        Frame.__init__(self, master, bg="red")
        self.sv = StringVar()
        self.text = Text(self, width = 15)
        self.entry = Entry(self, textvariable = self.sv)
        self.entry.bind("<KeyRelease>", self.on_entry)
        self.entry.pack(fill=X)
        self.pack()

        self.automates = graph

    def on_entry(self, event):
        words = self.entry.get()
        self.automates.backToStart()
        words = words.split(' ')[-1]
        for l in words:
            self.automates.nextNode(l)
        self.text.replace(1.0, END, self.automates.printFromCurrentNode(words))
        self.text.pack()
