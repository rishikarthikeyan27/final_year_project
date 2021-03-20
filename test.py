import tkinter as tk
from PIL import ImageTk, Image
import random

class Dog:
    def __init__(self):
        self.win = tk.Tk()
        self.win.geometry('1000x650')
        self.puppy = ImageTk.PhotoImage(Image.open('images/puppy.png').resize((80, 50), Image.ANTIALIAS))
        self.puppy_button = tk.Button(self.win, text = "Create Puppies", command = self.create_label)
        self.puppy_button.pack()
        self.win.mainloop()
    def move(self, e):
        self.puppy = ImageTk.PhotoImage(Image.open('images/puppy.png').resize((80, 50), Image.ANTIALIAS))
        self.puppy_label = tk.Label(self.win, image = self.puppy)
        self.puppy_label.place(height = 80, width = 50, x = e.x, y = e.y)
        print(' X : '+ str(e.x) +' and '+ 'Y : ' + str(e.y))
    def create_label(self):
        self.puppy_label = tk.Label(self.win, image = self.puppy)
        self.puppy_label.place(height = 80, width = 50, x= 0, y = 0)
        self.puppy_label.bind('<B1-Motion>', self.move)
        return
    

lab = Dog()