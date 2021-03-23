# import tkinter as tk
# from PIL import ImageTk, Image
# import random

# class Dog:
#     def __init__(self):
#         self.win = tk.Tk()
#         self.win.geometry('1000x650')
#         self.puppy = ImageTk.PhotoImage(Image.open('images/puppy.png').resize((80, 50), Image.ANTIALIAS))
#         self.puppy_button = tk.Button(self.win, text = "Create Puppies", command = self.create_label)
#         self.bin = ImageTk.PhotoImage(Image.open('images/bin.png').resize((80, 50), Image.ANTIALIAS))
#         self.bin_label = tk.Label(self.win, text = "bin", image = self.bin)
#         self.bin_label.place(height = 56, width = 50, x= 50, y=50)
#         self.dal = ImageTk.PhotoImage(Image.open('images/bin.png').resize((80, 50), Image.ANTIALIAS))
#         self.dal_button = tk.Button(self.win, text = 'button', command = self.delete_all)
#         self.dal_button.place(width = 50, height = 80, x = 100, y=100)
#         self.puppy_list = []
#         # print("Bin x : "+ str(self.bin_label.coords(x)), "Bin y : "+ str(self.bin_label.coords(y)))
#         self.puppy_button.pack()

#     def move(self, e, txt):
#         # print (e.x , e.y)
#         x = self.win.winfo_pointerx() - self.win.winfo_rootx()
#         y = self.win.winfo_pointery() - self.win.winfo_rooty()
#         e.widget.place(height = 60, width = 50, x=x,y=y,anchor='center')
#         txt.place(x=x-8 , y = y-50)


#     def delete(self, e):
#         if((str(self.bin_label.winfo_rootx())[0] + str(self.bin_label.winfo_rootx())[1]) == (str(e.widget.winfo_rootx())[0] + str(e.widget.winfo_rootx())[1])) and ((str(self.bin_label.winfo_rooty())[0] + str(self.bin_label.winfo_rooty())[1]) == (str(e.widget.winfo_rooty())[0] + str(e.widget.winfo_rooty())[1])):
#             e.widget.destroy()
    
    
#     def delete_all(self):
#         for i in self.puppy_list:
#             i.destroy()

#     def master_move(self, e, inp):
#         self.move(e, inp)
#         self.delete(e)
    
#     def create_label(self):
#         self.puppy_label = tk.Label(self.win, image = self.puppy, text = str(random.randint(1,3)))
#         self.puppy_label.place(height = 60, width = 50, x= random.randint(300,400), y = random.randint(300, 400))
#         self.puppy_list.append(self.puppy_label)
#         self.entry = self.Entry(self.win)
#         self.puppy_label.bind('<B1-Motion>', lambda event, txt = self.entry.text: self.master_move(event, txt))
#         return
#     class Entry:
#         def __init__(self, win):
#             self.text = tk.Text(win, height = 1, width = 2)
    
    
        
        
    
# lab = Dog()
# lab.win.mainloop()

# 
import tkinter as tk
import inspect
from PIL import ImageTk, Image

class Test():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x80")
        self.list = []
        self.frame2 = tk.Frame(self.root)
        self.frame2.pack()
        self.puppy = ImageTk.PhotoImage(Image.open('images/puppy.png').resize((80, 50), Image.ANTIALIAS))
        self.label1 = tk.Label(self.frame2,
                              text = "Text to be read", image = self.puppy)
        self.list.append(self.label1)
        self.button = tk.Button(self.frame3,
                                text="Read Label Text")
        self.button.pack()
        self.label1.place(height = 50, width = 50, x = 10, y=10)
        self.root.mainloop()

    def readLabelText(self):
        for i in self.list:
            print(type(i))
            print(i.cget('text'))
        print(self.list[0].cget('text'))
        print((self.list[0]).cget('text'))      

app=Test()
app.readLabelText()