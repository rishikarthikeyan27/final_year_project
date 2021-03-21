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

    def move(self, e):
        print (e.x , e.y)
        x = self.win.winfo_pointerx() - self.win.winfo_rootx()
        y = self.win.winfo_pointery() - self.win.winfo_rooty()
        e.widget.place(height = 80, width = 50, x=x,y=y,anchor='center')
        print(' X : '+ str(e.x) +' and '+ 'Y : ' + str(e.y))

    def create_label(self):
        self.puppy_label = tk.Label(self.win, image = self.puppy, text = str(random.randint(1,3)))
        self.puppy_label.place(height = 80, width = 50, x= random.randint(300,400), y = random.randint(300, 400))
        self.label_list.append(self.puppy_label)
        print("All the labels : ", self.label_list)
        self.puppy_label.bind('<B1-Motion>', self.move)
        return
    
lab = Dog()
lab.win.mainloop()