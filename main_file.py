import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import random

class Window:

    #Init
    def __init__(self):
        
        #Create window
        self.win = tk.Tk()
        self.win.geometry('1000x650')
        self.win.configure(bg = 'black')

        #Create Frames
        self.frame1 = tk.Frame(master=self.win, width=280, height=630, bg='#006665')
        self.frame1.pack(fill=tk.BOTH, padx=10, pady=15,side=tk.LEFT, expand=False)
        self.frame2 = tk.Frame(master=self.win, width=680, height=315, bg="#006665")
        self.frame2.pack(fill=tk.Y, padx=5, pady=15,side=tk.TOP, expand=False)
        self.frame3 = tk.Frame(master=self.win, width=680, height=315, bg="#006665")
        self.frame3.pack(fill=tk.Y, padx=5, pady=15,side=tk.BOTTOM, expand=False)

        #Arrow down button
        self.arrow_down_pic = Image.open('images/arrow.png').resize((30, 30), Image.ANTIALIAS)
        self.resized_arrow_down_pic = ImageTk.PhotoImage(self.arrow_down_pic)
        self.arrow_down_button = tk.Button(self.win, text = "Point Force", image = self.resized_arrow_down_pic, bg = 'black', command = self.create_down_arrow)
        self.arrow_down_button.place(height = 40, width = 80, x=70, y=50)

        #Arrow up button
        self.arrow_up_pic = Image.open('images/arrow_up.png').resize((30,30), Image.ANTIALIAS)
        self.resized_arrow_up_pic = ImageTk.PhotoImage(self.arrow_up_pic)
        self.arrow_up_button = tk.Button(self.win, text = "Point Force", image = self.resized_arrow_up_pic, bg = 'black',command = self.create_up_arrow)
        self.arrow_up_button.place(height = 40, width = 80, x=70, y=90)

        #Anticlockwise Moment button
        self.moment_ac_pic = Image.open('images/moment_anticlockwise.png').resize((30,30), Image.ANTIALIAS)
        self.resized_moment_ac_pic = ImageTk.PhotoImage(self.moment_ac_pic)
        self.moment_ac_button = tk.Button(self.win, image = self.resized_moment_ac_pic, bg = 'black',command = self.create_moment_ac)
        self.moment_ac_button.place(height = 40, width = 80, x=150, y=50)

        #Clockwise Moment button
        self.moment_c_pic = Image.open('images/moment_clockwise.png').resize((30,30), Image.ANTIALIAS)
        self.resized_moment_c_pic = ImageTk.PhotoImage(self.moment_c_pic)
        self.moment_c_button = tk.Button(self.win, image = self.resized_moment_c_pic, bg = 'black',command = self.create_moment_c)
        self.moment_c_button.place(height = 40, width = 80, x=150, y=90)

        #Uniform Distributed Load button
        self.uniform_pic = Image.open('images/uniform.png').resize((80,50), Image.ANTIALIAS)
        self.resized_uniform_pic = ImageTk.PhotoImage(self.uniform_pic)
        self.uniform_button = tk.Button(self.win, image = self.resized_uniform_pic, bg = 'black',command = self.create_uniform_load)
        self.uniform_button.place(height = 40, width = 80, x=70, y=130)

        #Nonuniformly Distributed Load button
        self.nonuniform_pic = Image.open('images/nonuniform.png').resize((80,50), Image.ANTIALIAS)
        self.resized_nonuniform_pic = ImageTk.PhotoImage(self.nonuniform_pic)
        self.non_uniform_button = tk.Button(self.win, image = self.resized_nonuniform_pic, bg = 'black',command = self.create_nonuniform_load)
        self.non_uniform_button.place(height = 40, width = 80, x=150, y=130)

        #Creating uniform and nonuniformly distributed load
        self.g_uniform_pic = Image.open('images/green_uniform_distributed_load.png').resize((80,50), Image.ANTIALIAS)
        self.resized_g_uniform_pic = ImageTk.PhotoImage(self.g_uniform_pic)
        self.g_nonuniform_pic = Image.open('images/green_nonuniform_distributed_load.png').resize((80,50), Image.ANTIALIAS)
        self.resized_g_nonuniform_pic = ImageTk.PhotoImage(self.g_nonuniform_pic)

        #Creating beam support pictures
        self.beam_simple_support = Image.open('images/beamsimplesupport.png').resize((40, 30), Image.ANTIALIAS)
        self.resized_beam_simple_support = ImageTk.PhotoImage(self.beam_simple_support)
        self.beam_fixed_support = Image.open('images/beamfixedsupport.png').resize((30, 100), Image.ANTIALIAS)
        self.resized_beam_fixed_support = ImageTk.PhotoImage(self.beam_fixed_support)

        #Simple Support
        self.simple_support_pic = Image.open('images/simple_support.png').resize((60,50), Image.ANTIALIAS)
        self.resized_simple_support_pic = ImageTk.PhotoImage(self.simple_support_pic)
        self.simple_support_button = tk.Button(self.frame1, image = self.resized_simple_support_pic, bg = 'black', command = self.create_simple_support)
        self.simple_support_button.place(height = 40, width = 80, x=70, y=250)

        #Fixed Support
        self.fixed_support_pic = Image.open('images/fixed_support.png').resize((60,50), Image.ANTIALIAS)
        self.resized_fixed_support_pic = ImageTk.PhotoImage(self.fixed_support_pic)
        self.fixed_support_button = tk.Button(self.frame1, image = self.resized_fixed_support_pic, bg = 'black', command = self.create_fixed_support)
        self.fixed_support_button.place(height = 40, width = 80, x=150, y=250)

        #Crossection Drop Down
        self.varList = tk.StringVar(self.win)
        self.varList.set("Force Type")
        self.force_type = ttk.OptionMenu(self.win, self.varList, "Cross section",'Rectangular', 'I', 'T', 'C', 'O', command = self.master_crossection_function)
        self.force_type.place(height=40, width=120, x= 80, y=340)

        #Create the beam picture
        self.beam_pic = Image.open('images/beam.png').resize((400, 50), Image.ANTIALIAS)
        self.resized_beam_pic = ImageTk.PhotoImage(self.beam_pic)
        self.beam_lab = tk.Label(self.frame2, width = 400, height = 50, image = self.resized_beam_pic, bg = 'black')
        self.beam_lab.place(x=150, y = 200)

        #Bin
        self.bin_pic = Image.open('images/bin.png').resize((50, 50), Image.ANTIALIAS)
        self.resized_bin_pic = ImageTk.PhotoImage(self.bin_pic)
        self.bin_label= tk.Label(self.frame2, image = self.resized_bin_pic, bg = '#006665', borderwidth = 0)
        self.bin_label.place( width = 50, height = 50, x=600, y = 15)

        #List of all the arrows that have been added
        self.arrow_list = []

        #mainloop
        self.win.mainloop()

    #Widget move
    def move(self, e):
        x = e.widget.master.winfo_pointerx() - e.widget.master.winfo_rootx()
        y = e.widget.master.winfo_pointery() - e.widget.master.winfo_rooty()
        e.widget.place(height = e.widget.winfo_height(), width = e.widget.winfo_width(), x=x,y=y,anchor='center')

    #Widget delete
    def delete(self, e):        
        if((str(self.bin_label.winfo_rootx())[0] + str(self.bin_label.winfo_rootx())[1]) == (str(e.widget.winfo_rootx())[0] + str(e.widget.winfo_rootx())[1])) and ((str(self.bin_label.winfo_rooty())[0] + str(self.bin_label.winfo_rooty())[1]) == (str(e.widget.winfo_rooty())[0] + str(e.widget.winfo_rooty())[1])):
            e.widget.destroy()
            print("Done destroying")
    
    #widget master
    def widget_master(self, e):
        self.move(e)
        self.delete(e)
    
    # Displays crossection picture  
    def display_crossection_picture(self, c):
        if(c == "Rectangular"):
            #add Rectangle cross section picture
            img = Image.open('images/r.png').resize((60, 60), Image.ANTIALIAS)
            img = img
            resized_image = ImageTk.PhotoImage(img)
            self.win.resized_image = resized_image
            print('width : ' + str(resized_image.width()), 'height : ' + str(resized_image.height()))
            img_label = tk.Label(self.win, width = 60, height = 60)
            img_label.configure(image = resized_image)
            img_label.update()
            print("hello")
            img_label.place(x= 100, y=400)
            # img_canvas.create_image(40, 30, image = resized_image, tag = "R")
        if(c == "I"):
            #add I cross section picture
            img = Image.open('images/i_beam.png').resize((60, 60), Image.ANTIALIAS)
            img = img
            resized_image = ImageTk.PhotoImage(img)
            self.win.resized_image = resized_image
            img_canvas = tk.Canvas(self.win, width = resized_image.width(), height = resized_image.height())
            print('width : ' + str(resized_image.width()), 'height : ' + str(resized_image.height()))
            img_canvas.place(x= 100, y=400)  
            img_canvas.create_image(40, 30, image = resized_image, tag = "I")
        if(c == "T"):
            #add T cross section picture
            img = Image.open('images/t.png').resize((60, 60), Image.ANTIALIAS)
            img = img
            resized_image = ImageTk.PhotoImage(img)
            self.win.resized_image = resized_image
            img_canvas = tk.Canvas(self.win, width = resized_image.width(), height = resized_image.height())
            print('width : ' + str(resized_image.width()), 'height : ' + str(resized_image.height()))
            img_canvas.place(x= 100, y=400)  
            img_canvas.create_image(40, 30, image = resized_image, tag = "T")
        if(c == "C"):
            #add C cross section picture
            img = Image.open('images/c.png').resize((60, 60), Image.ANTIALIAS)
            img = img
            resized_image = ImageTk.PhotoImage(img)
            self.win.resized_image = resized_image
            img_canvas = tk.Canvas(self.win, width = resized_image.width(), height = resized_image.height()+2)
            print('width : ' + str(resized_image.width()), 'height : ' + str(resized_image.height()))
            img_canvas.place(x= 100, y=400)  
            img_canvas.create_image(40, 30, image = resized_image, tag = "C")
        if(c == "O"):
            #add O cross section picture
            img = Image.open('images/o.png').resize((60, 60), Image.ANTIALIAS)
            img = img
            resized_image = ImageTk.PhotoImage(img)
            self.win.resized_image = resized_image
            img_canvas = tk.Canvas(self.win, width = resized_image.width(), height = resized_image.height())
            print('width : ' + str(resized_image.width()), 'height : ' + str(resized_image.height()))
            img_canvas.place(x= 100, y=400)  
            img_canvas.create_image(28, 32, image = resized_image, tag = "O")
    
    # Crossection OptionMenu master function
    def master_crossection_function(self, choice):
        self.display_crossection_picture(choice) 

    # Creating arrows
    def create_up_arrow(self):
        self.arrow_up_lab = tk.Label(self.frame2,image = self.resized_arrow_up_pic, bg = '#006665')
        self.arrow_up_lab.place(height = 30, width = 30, x=random.randrange(300,400), y=random.randrange(40,100))
        self.arrow_list.append(self.arrow_up_lab)
        self.arrow_up_lab.bind('<B1-Motion>', self.widget_master)
        return
    def create_down_arrow(self):
        self.arrow_down_lab = tk.Label(self.frame2,image = self.resized_arrow_down_pic, bg = '#006665')
        self.arrow_down_lab.place(height = 30, width = 30, x=random.randrange(300,400), y=random.randrange(40,100))
        self.arrow_list.append(self.arrow_down_lab)
        self.arrow_down_lab.bind('<B1-Motion>', self.widget_master)
        return
    def create_moment_ac(self):
        self.moment_ac_lab = tk.Label(self.frame2,image = self.resized_moment_ac_pic, bg = '#006665')
        self.moment_ac_lab.place(height = 30, width = 30, x=random.randrange(300,400), y=random.randrange(40,100))
        self.arrow_list.append(self.moment_ac_lab)
        self.moment_ac_lab.bind('<B1-Motion>', self.widget_master)
        return
    def create_moment_c(self):
        self.moment_c_lab = tk.Label(self.frame2,image = self.resized_moment_c_pic, bg = '#006665')
        self.moment_c_lab.place(height = 30, width = 30, x=random.randrange(300,400), y=random.randrange(40,100))
        self.arrow_list.append(self.moment_c_lab)
        self.moment_c_lab.bind('<B1-Motion>', self.widget_master)
        return
    def create_uniform_load(self):
        self.uniform_load_lab = tk.Label(self.frame2,image = self.resized_g_uniform_pic, bg = '#006665')
        self.uniform_load_lab.place(height = 40, width = 80, x=random.randrange(300,400), y=random.randrange(40,100))
        self.arrow_list.append(self.uniform_load_lab)
        self.uniform_load_lab.bind('<B1-Motion>', self.widget_master)
        return
    def create_nonuniform_load(self):
        self.nonuniform_load_lab = tk.Label(self.frame2,image = self.resized_g_nonuniform_pic, bg = '#006665')
        self.nonuniform_load_lab.place(height = 40, width = 80, x=random.randrange(300,400), y=random.randrange(40,100))
        self.arrow_list.append(self.nonuniform_load_lab)
        self.nonuniform_load_lab.bind('<B1-Motion>', self.widget_master)
        return
    
    # Creating supports
    def create_simple_support(self):
        self.simple_support_lab = tk.Label(self.frame2, image = self.resized_beam_simple_support)
        self.simple_support_lab.place(height = 30, width = 30, x=random.randrange(300,400), y=random.randrange(40,100))
        return
    def create_fixed_support(self):
        self.fixed_support_lab = tk.Label(self.frame2, image = self.resized_beam_fixed_support)
        self.fixed_support_lab.place(height = 100, width = 30, x=120, y = 180)
        return
    
        
    # Print arrow_list
    def print_arrow_list(self):
        print(self.arrow_list)
    
root = Window()
