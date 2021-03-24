import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import random
import calc_file as cf
import math
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

        self.submit_button = tk.Button(self.frame3,
                                text="Read Label Text", command = self.get_arrow_length)
        self.submit_button.pack()

        #Load label
        self.load_selection_lab = ttk.Label(self.frame1, text = "Please Select Loads", background = '#006665', font=("Helvetica",9, 'bold'))
        self.load_selection_lab.place(height = 30, width = 140, x=80, y=5)

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

        #Creating upside down uniform and upside down nonuniformly distributed load
        self.g_usd_uniform_pic = Image.open('images/green_usd_uniform_distributed_load.png').resize((80,50), Image.ANTIALIAS)
        self.resized_g_usd_uniform_pic = ImageTk.PhotoImage(self.g_usd_uniform_pic)
        self.g_usd_nonuniform_pic = Image.open('images/green_usd_nonuniform_distributed_load.png').resize((80,50), Image.ANTIALIAS)
        self.resized_g_usd_nonuniform_pic = ImageTk.PhotoImage(self.g_usd_nonuniform_pic)

        # Upside Down Uniform Distributed Load button
        self.usd_uniform_pic = Image.open('images/usd_uniform.png').resize((70,50), Image.ANTIALIAS)
        self.resized_usd_uniform_pic = ImageTk.PhotoImage(self.usd_uniform_pic)
        self.usd_uniform_button = tk.Button(self.win, image = self.resized_usd_uniform_pic, bg = 'black',command = self.create_usd_uniform_load)
        self.usd_uniform_button.place(height = 50, width = 80, x=70, y=170)

        # Upside Down Nonuniformly Distributed Load button
        self.usd_nonuniform_pic = Image.open('images/usd_nonuniform.png').resize((70,50), Image.ANTIALIAS)
        self.resized_usd_nonuniform_pic = ImageTk.PhotoImage(self.usd_nonuniform_pic)
        self.usd_non_uniform_button = tk.Button(self.win, image = self.resized_usd_nonuniform_pic, bg = 'black',command = self.create_usd_nonuniform_load)
        self.usd_non_uniform_button.place(height = 50, width = 80, x=150, y=170)

       
        #Creating beam support pictures
        self.beam_simple_support = Image.open('images/beamsimplesupport.png').resize((40, 30), Image.ANTIALIAS)
        self.resized_beam_simple_support = ImageTk.PhotoImage(self.beam_simple_support)
        self.beam_fixed_support = Image.open('images/beamfixedsupport.png').resize((30, 100), Image.ANTIALIAS)
        self.resized_beam_fixed_support = ImageTk.PhotoImage(self.beam_fixed_support)

        #Support label
        self.support_selection_lab = ttk.Label(self.frame1, text = "Please Select Supports", background = '#006665', font=("Helvetica",9, 'bold'))
        self.support_selection_lab.place(height = 30, width = 140, x=75, y=230)

        #Simple Support
        self.simple_support_pic = Image.open('images/simple_support.png').resize((25,25), Image.ANTIALIAS)
        self.resized_simple_support_pic = ImageTk.PhotoImage(self.simple_support_pic)
        self.simple_support_button = tk.Button(self.frame1, image = self.resized_simple_support_pic, bg = 'black', command = self.create_simple_support)
        self.simple_support_button.place(height = 40, width = 80, x=61, y=260)

        #Fixed Support
        self.fixed_support_pic = Image.open('images/fixed_support.png').resize((60,50), Image.ANTIALIAS)
        self.resized_fixed_support_pic = ImageTk.PhotoImage(self.fixed_support_pic)
        self.fixed_support_button = tk.Button(self.frame1, image = self.resized_fixed_support_pic, bg = 'black', command = self.create_fixed_support)
        self.fixed_support_button.place(height = 40, width = 80, x=141, y=260)

        #Crossection Drop Down
        self.varList = tk.StringVar(self.win)
        self.varList.set("Crossection")
        self.choice_list = ["Cross section",'Rectangular', 'I', 'T', 'C', 'O']
        self.force_type = ttk.OptionMenu(self.win, self.varList, *self.choice_list, command = self.master_crossection_function)
        self.force_type.place(height=40, width=120, x = 90, y=350)

        self.beam_length_number = tk.StringVar()
        #Beam Length Label
        self.beam_length_label = tk.Label(self.win, width = 50, height = 50, text = "Enter the beam length : ", bg = '#006665',font=("Helvetica",9, 'bold'))
        self.beam_length_label.place(height = 30, width = 142, x=20, y=490)
        #Enter length of beam
        self.beam_length = tk.Entry(self.win, text = self.beam_length_number)
        self.beam_length.place(x = 160, y = 495)
        self.submit = tk.Button(self.win, text = "Submit", command = self.add_beam_length_label)
        self.submit.place(height = 30, width = 140, x=60, y=550)

        #Create the beam picture
        self.beam_pic = Image.open('images/beam.png').resize((400, 50), Image.ANTIALIAS)
        self.resized_beam_pic = ImageTk.PhotoImage(self.beam_pic)
        self.beam_lab = tk.Label(self.frame2, width = 400, height = 50, image = self.resized_beam_pic, bg = 'black')
        self.beam_lab.place(x=150, y = 190)

        #0m
        self.beam_0 = tk.Label(self.frame2, text = "0m", bg = '#006665')
        self.beam_0.place(width = 20, height = 20, x=150, y = 250)

        
        #Bin
        self.bin_pic = Image.open('images/bin.png').resize((50, 50), Image.ANTIALIAS)
        self.resized_bin_pic = ImageTk.PhotoImage(self.bin_pic)
        self.bin_label= tk.Label(self.frame2, image = self.resized_bin_pic, bg = '#006665', borderwidth = 0)
        self.bin_label.place( width = 50, height = 50, x=600, y = 15)

        #Delete all loads
        self.delete_all_loads = ImageTk.PhotoImage(Image.open('images/delete_all_loads.png').resize((60, 60), Image.ANTIALIAS))
        self.dal_button = tk.Button(self.frame2, image = self.delete_all_loads, bg = '#006665',command = self.del_all_loads)
        self.dal_button.place(width = 60, height = 60, x = 5, y=15)

        #Delete all supports
        self.delete_all_supports = ImageTk.PhotoImage(Image.open('images/delete_all_supports.png').resize((60, 60), Image.ANTIALIAS))
        self.das_button = tk.Button(self.frame2, image = self.delete_all_supports, bg = '#006665',command = self.del_all_supports)
        self.das_button.place(width = 60, height = 60, x = 70, y=15)


        #List of all the arrows that have been added
        self.arrow_list = []

        #List of all the supports that have been added
        self.support_list = []

        #List of all inputs
        self.input_list = []

        #mainloop
        self.win.mainloop()

    def add_beam_length_label(self):
        lab_num = self.beam_length_number.get()
        self.beam_l = tk.Label(self.frame2, text = str(lab_num) + "m", bg = '#006665')
        width_ = 20+len(lab_num)+15
        self.beam_l.place(width = width_, height = 20, x=540, y = 250)


    #Widget delete
    def delete(self, e, inp):        
        if((str(self.bin_label.winfo_rootx())[0] + str(self.bin_label.winfo_rootx())[1]) == (str(e.widget.winfo_rootx())[0] + str(e.widget.winfo_rootx())[1])) and ((str(self.bin_label.winfo_rooty())[0] + str(self.bin_label.winfo_rooty())[1]) == (str(e.widget.winfo_rooty())[0] + str(e.widget.winfo_rooty())[1])):
            e.widget.destroy()
            inp.destroy()
            print("Done destroying")
    
    def del_all_loads(self):
        for i in self.arrow_list:
            i.destroy()
        self.arrow_list.clear()
        for j in self.input_list:
            j.destroy()
        self.input_list.clear()
        print(self.arrow_list)
    
    def del_all_supports(self):
        for i in self.support_list:
            i.destroy()
        self.support_list.clear()
        print(self.arrow_list)

    #Move input along with arrows (up)
    def move_input_up(self, e,txt):
        ex = e.widget.master.winfo_pointerx() - e.widget.master.winfo_rootx()
        ey = e.widget.master.winfo_pointery() - e.widget.master.winfo_rooty()
        e.widget.place(height = e.widget.winfo_height(), width = e.widget.winfo_width(), x=ex,y=ey,anchor='center')
        x = self.win.winfo_pointerx() - self.win.winfo_rootx()
        y = self.win.winfo_pointery() - self.win.winfo_rooty()
        txt.place(x=x-10 , y = y-40)
    
    #Move input along with arrows (down)
    def move_input_down(self, e, txt):
        ex = e.widget.master.winfo_pointerx() - e.widget.master.winfo_rootx()
        ey = e.widget.master.winfo_pointery() - e.widget.master.winfo_rooty()
        e.widget.place(height = e.widget.winfo_height(), width = e.widget.winfo_width(), x=ex,y=ey,anchor='center')
        x = self.win.winfo_pointerx() - self.win.winfo_rootx()
        y = self.win.winfo_pointery() - self.win.winfo_rooty()
        txt.place(x=x-10 , y = y+20)
    
    #Delete Support
    def delete_support(self, e):
        if((str(self.bin_label.winfo_rootx())[0] + str(self.bin_label.winfo_rootx())[1]) == (str(e.widget.winfo_rootx())[0] + str(e.widget.winfo_rootx())[1])) and ((str(self.bin_label.winfo_rooty())[0] + str(self.bin_label.winfo_rooty())[1]) == (str(e.widget.winfo_rooty())[0] + str(e.widget.winfo_rooty())[1])):
            e.widget.destroy()
            print("Done destroying")

    def trial(self):
            print (self.beam_length_number.get())
    
    #Move Support
    def move_support(self, e):
        ex = e.widget.master.winfo_pointerx() - e.widget.master.winfo_rootx()
        ey = e.widget.master.winfo_pointery() - e.widget.master.winfo_rooty()
        e.widget.place(height = e.widget.winfo_height(), width = e.widget.winfo_width(), x=ex,y=ey,anchor='center')
    
    #widget master up
    def widget_master_up(self, e, inp):
        # self.move(e)
        self.delete(e, inp)
        self.move_input_up(e, inp)

    #widget master down
    def widget_master_down(self, e, inp):
        # self.move(e)
        self.delete(e, inp)
        self.move_input_down(e, inp)
    
    def support_master(self, e):
        self.delete_support(e)
        self.move_support(e)
    
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
        self.to_calc(choice)

    # Creating arrows
    def create_up_arrow(self):
        self.arrow_up_lab = tk.Label(self.frame2,image = self.resized_arrow_up_pic, bg = '#006665')
        self.arrow_up_lab.place(height = 30, width = 30, x=random.randrange(130,140), y=random.randrange(260,270))
        self.arrow_list.append(self.arrow_up_lab)
        self.entry = self.Entry(self.win)
        self.arrow_up_lab.bind('<B1-Motion>', lambda event, txt = self.entry.text: self.widget_master_down(event, txt))
        self.input_list.append(self.entry.text)
        return
    def create_down_arrow(self):
        self.arrow_down_lab = tk.Label(self.frame2,image = self.resized_arrow_down_pic, bg = '#006665')
        self.arrow_down_lab.place(height = 30, width = 30, x=random.randrange(130,140), y=random.randrange(140,150), anchor = "c")
        self.arrow_list.append(self.arrow_down_lab)
        self.entry = self.Entry(self.win)
        self.arrow_down_lab.bind('<B1-Motion>', lambda event, txt = self.entry.text: self.widget_master_up(event, txt))
        self.input_list.append(self.entry.text)
        return
    def create_moment_ac(self):
        self.moment_ac_lab = tk.Label(self.frame2,image = self.resized_moment_ac_pic, bg = '#006665')
        self.moment_ac_lab.place(height = 30, width = 30, x=random.randrange(130,140), y=random.randrange(140,150))
        self.arrow_list.append(self.moment_ac_lab)
        self.entry = self.Entry(self.win)
        self.moment_ac_lab.bind('<B1-Motion>', lambda event, txt = self.entry.text: self.widget_master_up(event, txt))
        self.input_list.append(self.entry.text)
        return
    def create_moment_c(self):
        self.moment_c_lab = tk.Label(self.frame2,image = self.resized_moment_c_pic, bg = '#006665')
        self.moment_c_lab.place(height = 30, width = 30, x=random.randrange(130,140), y=random.randrange(140,150))
        self.arrow_list.append(self.moment_c_lab)
        self.entry = self.Entry(self.win)
        self.moment_c_lab.bind('<B1-Motion>', lambda event, txt = self.entry.text: self.widget_master_up(event, txt))
        self.input_list.append(self.entry.text)
        return
    def create_uniform_load(self):
        self.uniform_load_lab = tk.Label(self.frame2,image = self.resized_g_uniform_pic, bg = '#006665')
        self.uniform_load_lab.place(height = 40, width = 80, x=random.randrange(130,140), y=random.randrange(140,150))
        self.arrow_list.append(self.uniform_load_lab)
        self.entry = self.Entry(self.win)
        self.uniform_load_lab.bind('<B1-Motion>', lambda event, txt = self.entry.text: self.widget_master_up(event, txt))
        self.input_list.append(self.entry.text)
        return
    def create_nonuniform_load(self):
        self.nonuniform_load_lab = tk.Label(self.frame2,image = self.resized_g_nonuniform_pic, bg = '#006665')
        self.nonuniform_load_lab.place(height = 40, width = 80, x=random.randrange(130,140), y=random.randrange(140,150))
        self.arrow_list.append(self.nonuniform_load_lab)
        self.entry = self.Entry(self.win)
        self.nonuniform_load_lab.bind('<B1-Motion>', lambda event, txt = self.entry.text: self.widget_master_up(event, txt))
        self.input_list.append(self.entry.text)
        return
    def create_usd_uniform_load(self):
        self.usd_uniform_load_lab = tk.Label(self.frame2,image = self.resized_g_usd_uniform_pic, bg = '#006665')
        self.usd_uniform_load_lab.place(height = 40, width = 80, x=random.randrange(130,140), y=random.randrange(260,270))
        self.arrow_list.append(self.usd_uniform_load_lab)
        self.entry = self.Entry(self.win)
        self.usd_uniform_load_lab.bind('<B1-Motion>', lambda event, txt = self.entry.text: self.widget_master_down(event, txt))
        self.input_list.append(self.entry.text)
        return
    def create_usd_nonuniform_load(self):
        self.usd_nonuniform_load_lab = tk.Label(self.frame2,image = self.resized_g_usd_nonuniform_pic, bg = '#006665')
        self.usd_nonuniform_load_lab.place(height = 40, width = 80, x=random.randrange(130,140), y=random.randrange(260,270))
        self.arrow_list.append(self.usd_nonuniform_load_lab)
        self.entry = self.Entry(self.win)
        self.usd_nonuniform_load_lab.bind('<B1-Motion>', lambda event, txt = self.entry.text: self.widget_master_down(event, txt))
        self.input_list.append(self.entry.text)
        return
    
    # Creating supports
    def create_simple_support(self):
        self.simple_support_lab = tk.Label(self.frame2, text = "simple", image = self.resized_beam_simple_support)
        self.support_list.append(self.simple_support_lab)
        self.simple_support_lab.place(height = 30, width = 30, x=random.randrange(300,400), y=random.randrange(40,100))
        # print(self.support_list[0].cget("Text"))
        self.simple_support_lab.bind('<B1-Motion>', self.support_master)
        return
    def create_fixed_support(self):
        self.fixed_support_lab = tk.Label(self.frame2, text = "fixed", image = self.resized_beam_fixed_support)
        self.support_list.append(self.fixed_support_lab)
        self.fixed_support_lab.place(height = 100, width = 30, x=120, y = 170)
        self.fixed_support_lab.bind('<B1-Motion>', self.support_master)
        return
    
    def read_support_text(self):
        for i in self.support_list:
            print(i.cget('text'))
    
    def get_arrow_length(self):
        entry = int(self.beam_length_number.get())
        print(entry)
        init = 1
        for i in self.arrow_list:
            # print("In meters : " + str(math.floor((int(entry)/400)*(int(i.winfo_x())-610))))
            print("Arrow"+str(init)+" : "+str(i.winfo_x()))
            init+=1
        
        print("Label : " + str(self.beam_lab.winfo_x()))
        # we need to get x coordinate of 1 arrow
        # we need to get the length at which the arrow is in 
        # we need to get coordinates of all arrows as tuples in a list
        # we need to get 
    
    def to_calc(self, cross):
        #sending data over to calc file
        print(cf.print_test(self.beam_length_number.get(), cross))

        
    #Entry class
    class Entry:
        def __init__(self, win):
            self.text = tk.Text(win, height = 1, width = 4)
    
root = Window()


# Remember ==> 547 - 945 




# Remember down pointing arrows y = 170 - 172
# Remember up pointing arrows y = 260 - 262

