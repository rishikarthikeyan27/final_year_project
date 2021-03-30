import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import random
import calc_file as cf
import math
import time
class Window:

    #Init
    def __init__(self):
        
        #Create window
        self.win = tk.Tk()
        self.win.geometry('1000x650')
        self.win.configure(bg = 'black')

        self.win.wm_attributes('-transparentcolor', 'red')
        #Create Frames
        self.frame1 = tk.Frame(master=self.win, width=280, height=630, bg='#006665')
        self.frame1.pack(fill=tk.BOTH, padx=10, pady=15,side=tk.LEFT, expand=False)
        self.frame2 = tk.Frame(master=self.win, width=680, height=315, bg="#006665")
        self.frame2.pack(fill=tk.Y, padx=5, pady=15,side=tk.TOP, expand=False)
        self.frame3 = tk.Frame(master=self.win, width=680, height=315, bg="#006665")
        self.frame3.pack(fill=tk.Y, padx=5, pady=15,side=tk.BOTTOM, expand=False)


        #Load label
        self.load_selection_lab = ttk.Label(self.frame1, text = "Please Select Loads", background = '#006665', font=("Helvetica",9, 'bold'))
        self.load_selection_lab.place(height = 30, width = 140, x=80, y=105)

        #Arrow down button
        self.arrow_down_pic = Image.open('images/arrow.png').resize((15, 15), Image.ANTIALIAS)
        self.resized_arrow_down_pic = ImageTk.PhotoImage(self.arrow_down_pic)
        self.arrow_down_button = tk.Button(self.win, text = "Point Force", image = self.resized_arrow_down_pic, bg = 'black', command = self.create_down_arrow)
        self.arrow_down_button.place(height = 30, width = 30, x=27, y=150)

        #Arrow up button
        self.arrow_up_pic = Image.open('images/arrow_up.png').resize((15,15), Image.ANTIALIAS)
        self.resized_arrow_up_pic = ImageTk.PhotoImage(self.arrow_up_pic)
        self.arrow_up_button = tk.Button(self.win, text = "Point Force", image = self.resized_arrow_up_pic, bg = 'black',command = self.create_up_arrow)
        self.arrow_up_button.place(height = 30, width = 30, x=57, y=150)

        #Anticlockwise Moment button
        self.moment_ac_pic = Image.open('images/moment_anticlockwise.png').resize((15, 15), Image.ANTIALIAS)
        self.resized_moment_ac_pic = ImageTk.PhotoImage(self.moment_ac_pic)
        self.moment_ac_button = tk.Button(self.win, image = self.resized_moment_ac_pic, bg = 'black',command = self.create_moment_ac)
        self.moment_ac_button.place(height = 30, width = 30, x = 87, y=150)

        #Clockwise Moment button
        self.moment_c_pic = Image.open('images/moment_clockwise.png').resize((15,15), Image.ANTIALIAS)
        self.resized_moment_c_pic = ImageTk.PhotoImage(self.moment_c_pic)
        self.moment_c_button = tk.Button(self.win, image = self.resized_moment_c_pic, bg = 'black',command = self.create_moment_c)
        self.moment_c_button.place(height = 30, width = 30, x = 117, y=150)

        #Uniform Distributed Load button
        self.uniform_pic = Image.open('images/uniform.png').resize((20,20), Image.ANTIALIAS)
        self.resized_uniform_pic = ImageTk.PhotoImage(self.uniform_pic)
        self.uniform_button = tk.Button(self.win, image = self.resized_uniform_pic, bg = 'black',command = self.create_uniform_load)
        self.uniform_button.place(height = 30, width = 30, x=147, y=150)

        #Nonuniformly Distributed Load button
        self.nonuniform_pic = Image.open('images/nonuniform.png').resize((20,20), Image.ANTIALIAS)
        self.resized_nonuniform_pic = ImageTk.PhotoImage(self.nonuniform_pic)
        self.non_uniform_button = tk.Button(self.win, image = self.resized_nonuniform_pic, bg = 'black',command = self.create_nonuniform_load)
        self.non_uniform_button.place(height = 30, width = 30, x=177, y=150)

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
        self.usd_uniform_pic = Image.open('images/usd_uniform.png').resize((20,20), Image.ANTIALIAS)
        self.resized_usd_uniform_pic = ImageTk.PhotoImage(self.usd_uniform_pic)
        self.usd_uniform_button = tk.Button(self.win, image = self.resized_usd_uniform_pic, bg = 'black',command = self.create_usd_uniform_load)
        self.usd_uniform_button.place(height = 30, width = 30, x=207, y=150)

        # Upside Down Nonuniformly Distributed Load button
        self.usd_nonuniform_pic = Image.open('images/usd_nonuniform.png').resize((20,20), Image.ANTIALIAS)
        self.resized_usd_nonuniform_pic = ImageTk.PhotoImage(self.usd_nonuniform_pic)
        self.usd_non_uniform_button = tk.Button(self.win, image = self.resized_usd_nonuniform_pic, bg = 'black',command = self.create_usd_nonuniform_load)
        self.usd_non_uniform_button.place(height = 30, width = 30, x=237, y=150)

       
        #Creating beam support pictures
        self.beam_simple_support = Image.open('images/beamsimplesupport.png').resize((40, 30), Image.ANTIALIAS)
        self.resized_beam_simple_support = ImageTk.PhotoImage(self.beam_simple_support)
        self.beam_fixed_support = Image.open('images/beamfixedsupport.png').resize((30, 100), Image.ANTIALIAS)
        self.resized_beam_fixed_support = ImageTk.PhotoImage(self.beam_fixed_support)

    
        #Crossection Drop Down
        self.varList = tk.StringVar(self.win)
        self.varList.set("Crossection")
        self.choice_list = ["Cross section",'Rectangular', 'I', 'T', 'C', 'O']
        self.force_type = ttk.OptionMenu(self.win, self.varList, *self.choice_list, command = self.master_crossection_function)
        self.force_type.place(height=40, width=120, x = 30, y=200)

        # Support Drop Down
        self.varsupport = tk.StringVar(self.win)
        self.varsupport.set("Support")
        self.support_list = ["Support", "Fixed Left",'Fixed Right', 'Fixed Ended', 'No Fixed Support']
        self.support_type = ttk.OptionMenu(self.win, self.varsupport, *self.support_list, command = self.master_support)
        self.support_type.place(height=40, width=120, x = 150, y=200)

        #Support label
        self.support_selection_lab = ttk.Label(self.frame1, text = "Please Select Supports", background = '#006665', font=("Helvetica",9, 'bold'))
        self.support_selection_lab.place(height = 30, width = 140, x=70, y=250)

        #Simple Support
        self.simple_support_pic = Image.open('images/simple_support.png').resize((20,20), Image.ANTIALIAS)
        self.resized_simple_support_pic = ImageTk.PhotoImage(self.simple_support_pic)
        self.simple_support_button = tk.Button(self.frame1, image = self.resized_simple_support_pic, bg = 'black', command = self.create_simple_support)
        self.simple_support_button.place(height = 30, width = 50, x=90, y=280)

        #Roller Support
        self.roller_support_pic = Image.open('images/roller_support.png').resize((20,20), Image.ANTIALIAS)
        self.resized_roller_support_pic = ImageTk.PhotoImage(self.roller_support_pic)
        self.roller_support_button = tk.Button(self.frame1, image = self.resized_roller_support_pic, bg = 'black', command = self.create_roller_support)
        self.roller_support_button.place(height = 30, width = 50, x=140, y=280)

        #Beam Length
        self.beam_length_number = tk.StringVar()
        #Beam Length Label
        self.beam_length_label = tk.Label(self.win, width = 50, height = 50, text = "Beam Length : ", bg = '#006665',font=("Helvetica",9, 'bold'))
        self.beam_length_label.place(height = 30, width = 142, x=20, y=50)
        #Enter length of beam
        self.beam_length = tk.Entry(self.win, text = self.beam_length_number)
        self.beam_length.place(x = 160, y = 55)

        #Youngs modulus input
        self.e = tk.StringVar()
        #Youngs Modulus Label
        self.e_label = tk.Label(self.win, width = 50, height = 50, text = "Youngs Modulus : ", bg = '#006665',font=("Helvetica",9, 'bold'))
        self.e_label.place(height = 30, width = 142, x=20, y= 75)
        #Entery for Youngs modulus
        self.e_val = tk.Entry(self.win, text = self.e)
        self.e_val.place(x = 160, y = 80)

        # Length Label List
        self.len_lab_list = []

        #Submit Button
        self.submit = tk.Button(self.win, text = "Submit", command = lambda listt = self.len_lab_list: self.master_submit(listt))
        self.submit.place(height = 30, width = 140, x=80, y=350)

        #Create the beam picture
        self.beam_pic = Image.open('images/beam.png').resize((400, 50), Image.ANTIALIAS)
        self.resized_beam_pic = ImageTk.PhotoImage(self.beam_pic)
        self.beam_lab = tk.Label(self.frame2, width = 400, height = 50, image = self.resized_beam_pic, bg = 'black')
        self.beam_lab.place(x=40, y = 190)

        #Crossection Canvas
        self.cross_canvas = tk.Canvas(self.frame2, highlightthickness = 0)
        self.cross_canvas.place(width = 100, height = 100, x= 500, y = 160)

        #Crossection Label 
        self.cross_label = tk.Label(self.frame2, bg = '#006665', text = 'Crossection', fg = 'white', font=("Helvetica",9, 'bold'))
        self.cross_label.place(width = 100, height = 50, x = 500, y = 270)


        #0m
        self.beam_0 = tk.Label(self.frame2, text = "0m", bg = '#006665')
        self.beam_0.place(width = 20, height = 20, x=40, y = 270)


        #Bin
        self.bin_pic = Image.open('images/bin.png').resize((50, 50), Image.ANTIALIAS)
        self.resized_bin_pic = ImageTk.PhotoImage(self.bin_pic)
        self.bin_label= tk.Label(self.frame2, image = self.resized_bin_pic, bg = '#006665', borderwidth = 0)
        self.bin_label.place( width = 50, height = 50, x=150, y = 25)

        #Delete all loads
        self.delete_all_loads = ImageTk.PhotoImage(Image.open('images/delete_all_loads.png').resize((60, 60), Image.ANTIALIAS))
        self.dal_button = tk.Button(self.frame2, image = self.delete_all_loads, bg = '#006665',command = self.del_all_loads)
        self.dal_button.place(width = 60, height = 60, x = 5, y=15)

        #Delete all supports
        self.delete_all_supports = ImageTk.PhotoImage(Image.open('images/delete_all_supports.png').resize((60, 60), Image.ANTIALIAS))
        self.das_button = tk.Button(self.frame2, image = self.delete_all_supports, bg = '#006665',command = self.del_all_supports)
        self.das_button.place(width = 60, height = 60, x = 70, y=15)

        self.alert_lab = tk.Label(self.frame1, text= "Please enter beam length first")


        
        #List of all the arrows that have been added
        self.arrow_list = []

        #List of all the supports that have been added
        self.support_list = []

        #List of all inputs
        self.input_list = []

        #crossection canvas list
        self.cross_canvas_list = []

        #crossection entry fields
        self.cross_entry = []
        
        #support choice list
        self.support_choice_list = []

        #Arrow load list
        self.arrow_load = []

        #Dimensions Done button list
        self.done_button_list = []

        #final load list
        self.final_load_list = []

        #grand load list
        self.grand_load_list = []

        #grand support list
        self.grand_support_list = []

        #mainloop
        self.win.mainloop()

    def add_beam_length_label(self):
        lab_num = self.beam_length_number.get()
        self.beam_l = tk.Label(self.frame2, text = str(lab_num) + "m", bg = '#006665')
        width_ = 20+len(lab_num)+15
        self.beam_l.place(width = width_, height = 20, x=410, y = 270)
        # x = 0
        # if len(self.support_list)>=1:
        #     for i in self.support_list:
        #         if (i.cget('text') == 'fixed'):
        #             x+=1
        # else:
        #     x=0
        # print('No.of fixed supports : ' + str(x))
        self.calc_reactions()


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
        for k in self.len_lab_list:
            k.destroy()
        self.len_lab_list.clear()
        
    
    def del_all_supports(self):
        for i in self.support_list:
            i.destroy()
        self.support_list.clear()
    
        


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
    def widget_master_up(self, e, inp, lab):
        # self.move(e)
        self.delete(e, inp)
        self.move_input_up(e, inp)
        self.add_dist_lab_up(e, lab)

    #widget master down
    def widget_master_down(self, e, inp, lab):
        # self.move(e)
        self.delete(e, inp)
        self.move_input_down(e, inp)
        self.add_dist_lab_down(e,lab)
    
    def support_master(self, e, lab):
        self.delete_support(e)
        self.move_support(e)
        self.add_dist_lab_down(e,lab)


    
    # Displays crossection picture  
    def display_crossection_picture(self, c):
        if(c == "Rectangular"):
            
            #add Rectangular cross section picture on frame 2
            self.rect_canvas = tk.Canvas(self.frame2, highlightthickness = 0)
            self.rect_canvas.place(width = 130, height = 130, x = 500, y = 160)
            self.rect = ImageTk.PhotoImage(Image.open('images/r_crossection.png').resize((130, 130), Image.ANTIALIAS))
            self.rect_canvas.create_image(65, 65,image = self.rect)
            self.cross_canvas_list.append(self.rect_canvas)

            #add necessary fields of input
            if (len(self.cross_entry)!=0):
                for i in self.cross_entry:
                    i.destroy()
                self.cross_entry.clear()

            self.entry_r_B_lab = tk.Label(self.frame2, text = 'B: ', bg = '#006665', fg = 'white', font=("Helvetica",9, 'bold'))
            self.entry_r_B_lab.place(width = 25, height = 25, x = 430, y = 25)
            self.entry_r_B = self.Entry(self.frame2)
            self.entry_r_B.text.place(x = 450, y = 27)
            self.cross_entry.extend([self.entry_r_B.text, self.entry_r_B_lab])

            self.entry_r_H_lab = tk.Label(self.frame2, text = 'H: ', bg = '#006665', fg = 'white', font=("Helvetica",9, 'bold'))
            self.entry_r_H_lab.place(width = 25, height = 25, x = 500, y = 25)
            self.entry_r_H = self.Entry(self.frame2)
            self.entry_r_H.text.place(x = 520, y = 27)
            self.cross_entry.extend([self.entry_r_H.text, self.entry_r_H_lab])
            
            if len(self.done_button_list)>=1:
                for i in self.done_button_list:
                    i.destroy()
                self.done_button_list.clear()
                
            self.done_dimensions = tk.Button(self.frame2, text = 'Done', command = self.get_dimensions_r)
            self.done_dimensions.place(width = 40, height = 20, x=570, y = 30)
            self.done_button_list.append(self.done_dimensions)

            
        if(c == "I"):
            

            #add I cross section picture on frame 2
            self.i_canvas = tk.Canvas(self.frame2, highlightthickness = 0)
            self.i_canvas.place(width = 130, height = 130, x = 500, y = 160)
            self.i = ImageTk.PhotoImage(Image.open('images/i_crossection.png').resize((130, 130), Image.ANTIALIAS))
            self.i_canvas.create_image(65, 65,image = self.i)
            self.cross_canvas_list.append(self.i_canvas)

            #add necessary fields of input
            if len(self.cross_entry):
                for i in self.cross_entry:
                    print(i)
                    i.destroy()
                self.cross_entry.clear()
                
            self.entry_i_B_lab = tk.Label(self.frame2, text = 'B: ', bg = '#006665', fg = 'white', font=("Helvetica",9, 'bold'))
            self.entry_i_B_lab.place(width = 25, height = 25, x = 400, y = 25)
            self.entry_i_B = self.Entry(self.frame2)
            self.entry_i_B.text.place(x = 420, y = 27)
            self.cross_entry.extend([self.entry_i_B.text, self.entry_i_B_lab])

            self.entry_i_H_lab = tk.Label(self.frame2, text = 'H: ', bg = '#006665', fg = 'white', font=("Helvetica",9, 'bold'))
            self.entry_i_H_lab.place(width = 25, height = 25, x = 470, y = 25)
            self.entry_i_H = self.Entry(self.frame2)
            self.entry_i_H.text.place(x = 490, y = 27)
            self.cross_entry.extend([self.entry_i_H.text, self.entry_i_H_lab])

            self.entry_i_b_lab = tk.Label(self.frame2, text = 'b: ', bg = '#006665', fg = 'white', font=("Helvetica",9, 'bold'))
            self.entry_i_b_lab.place(width = 25, height = 25, x = 540, y = 25)
            self.entry_i_b = self.Entry(self.frame2)
            self.entry_i_b.text.place(x = 560, y = 27)
            self.cross_entry.extend([self.entry_i_b.text, self.entry_i_b_lab])

            self.entry_i_h_lab = tk.Label(self.frame2, text = 'h: ', bg = '#006665', fg = 'white', font=("Helvetica",9, 'bold'))
            self.entry_i_h_lab.place(width = 25, height = 25, x = 610, y = 25)
            self.entry_i_h = self.Entry(self.frame2)
            self.entry_i_h.text.place(x = 630, y = 27)
            self.cross_entry.extend([self.entry_i_h.text, self.entry_i_h_lab])

            if len(self.done_button_list)>=1:
                for i in self.done_button_list:
                    i.destroy()
                self.done_button_list.clear()

            self.done_dimensions = tk.Button(self.frame2, text = 'Done', command = self.get_dimensions_i)
            self.done_dimensions.place(width = 40, height = 20, x=570, y = 60)
            self.done_button_list.append(self.done_dimensions)
        
        if(c == "T"):
            

            #add T cross section picture on frame 2
            self.t_canvas = tk.Canvas(self.frame2, highlightthickness = 0)
            self.t_canvas.place(width = 130, height = 130, x = 500, y = 160)
            self.t = ImageTk.PhotoImage(Image.open('images/t_crossection.png').resize((130, 130), Image.ANTIALIAS))
            self.t_canvas.create_image(65, 65,image = self.t)
            self.cross_canvas_list.append(self.t_canvas)

            #add necessary fields of input
            if len(self.cross_entry):
                for i in self.cross_entry:
                    print(i)
                    i.destroy()
                self.cross_entry.clear()
                
            self.entry_t_B_lab = tk.Label(self.frame2, text = 'B: ', bg = '#006665', fg = 'white', font=("Helvetica",9, 'bold'))
            self.entry_t_B_lab.place(width = 25, height = 25, x = 400, y = 25)
            self.entry_t_B = self.Entry(self.frame2)
            self.entry_t_B.text.place(x = 420, y = 27)
            self.cross_entry.extend([self.entry_t_B.text, self.entry_t_B_lab])

            self.entry_t_H_lab = tk.Label(self.frame2, text = 'H: ', bg = '#006665', fg = 'white', font=("Helvetica",9, 'bold'))
            self.entry_t_H_lab.place(width = 25, height = 25, x = 470, y = 25)
            self.entry_t_H = self.Entry(self.frame2)
            self.entry_t_H.text.place(x = 490, y = 27)
            self.cross_entry.extend([self.entry_t_H.text, self.entry_t_H_lab])

            self.entry_t_b_lab = tk.Label(self.frame2, text = 'b: ', bg = '#006665', fg = 'white', font=("Helvetica",9, 'bold'))
            self.entry_t_b_lab.place(width = 25, height = 25, x = 540, y = 25)
            self.entry_t_b = self.Entry(self.frame2)
            self.entry_t_b.text.place(x = 560, y = 27)
            self.cross_entry.extend([self.entry_t_b.text, self.entry_t_H_lab])

            self.entry_t_h_lab = tk.Label(self.frame2, text = 'h: ', bg = '#006665', fg = 'white', font=("Helvetica",9, 'bold'))
            self.entry_t_h_lab.place(width = 25, height = 25, x = 610, y = 25)
            self.entry_t_h = self.Entry(self.frame2)
            self.entry_t_h.text.place(x = 630, y = 27)
            self.cross_entry.extend([self.entry_t_h.text, self.entry_t_h_lab])

            if len(self.done_button_list)>=1:
                for i in self.done_button_list:
                    i.destroy()
                self.done_button_list.clear()

            self.done_dimensions = tk.Button(self.frame2, text = 'Done', command = self.get_dimensions_t)
            self.done_dimensions.place(width = 40, height = 20, x=570, y = 60)
            self.done_button_list.append(self.done_dimensions)

        if(c == "C"):
            
            #add C cross section picture on frame 2
            self.c_canvas = tk.Canvas(self.frame2, highlightthickness = 0)
            self.c_canvas.place(width = 130, height = 130, x = 500, y = 160)
            self.c = ImageTk.PhotoImage(Image.open('images/c_crossection.png').resize((130, 130), Image.ANTIALIAS))
            self.c_canvas.create_image(65, 65,image = self.c)
            self.cross_canvas_list.append(self.c_canvas)

            #add necessary fields of input
            if len(self.cross_entry):
                for i in self.cross_entry:
                    print(i)
                    i.destroy()
                self.cross_entry.clear()
                
            self.entry_c_B_lab = tk.Label(self.frame2, text = 'B: ', bg = '#006665', fg = 'white', font=("Helvetica",9, 'bold'))
            self.entry_c_B_lab.place(width = 25, height = 25, x = 400, y = 25)
            self.entry_c_B = self.Entry(self.frame2)
            self.entry_c_B.text.place(x = 420, y = 27)
            self.cross_entry.extend([self.entry_c_B.text, self.entry_c_B_lab])

            self.entry_c_H_lab = tk.Label(self.frame2, text = 'H: ', bg = '#006665', fg = 'white', font=("Helvetica",9, 'bold'))
            self.entry_c_H_lab.place(width = 25, height = 25, x = 470, y = 25)
            self.entry_c_H = self.Entry(self.frame2)
            self.entry_c_H.text.place(x = 490, y = 27)
            self.cross_entry.extend([self.entry_c_H.text, self.entry_c_H_lab])

            self.entry_c_b_lab = tk.Label(self.frame2, text = 'b: ', bg = '#006665', fg = 'white', font=("Helvetica",9, 'bold'))
            self.entry_c_b_lab.place(width = 25, height = 25, x = 540, y = 25)
            self.entry_c_b = self.Entry(self.frame2)
            self.entry_c_b.text.place(x = 560, y = 27)
            self.cross_entry.extend([self.entry_c_b.text, self.entry_c_b_lab])

            self.entry_c_h_lab = tk.Label(self.frame2, text = 'h: ', bg = '#006665', fg = 'white', font=("Helvetica",9, 'bold'))
            self.entry_c_h_lab.place(width = 25, height = 25, x = 610, y = 25)
            self.entry_c_h = self.Entry(self.frame2)
            self.entry_c_h.text.place(x = 630, y = 27)
            self.cross_entry.extend([self.entry_c_h.text, self.entry_c_h_lab])

            if len(self.done_button_list)>=1:
                for i in self.done_button_list:
                    i.destroy()
                self.done_button_list.clear()

            self.done_dimensions = tk.Button(self.frame2, text = 'Done', command = self.get_dimensions_c)
            self.done_dimensions.place(width = 40, height = 20, x=570, y = 60)
            self.done_button_list.append(self.done_dimensions)

        if(c == "O"):
           
            #add C cross section picture on frame 2
            self.o_canvas = tk.Canvas(self.frame2, highlightthickness = 0)
            self.o_canvas.place(width = 130, height = 130, x = 500, y = 160)
            self.o = ImageTk.PhotoImage(Image.open('images/o_crossection.png').resize((130, 130), Image.ANTIALIAS))
            self.o_canvas.create_image(65, 65,image = self.o)
            self.cross_canvas_list.append(self.o_canvas)

            #add necessary fields of input
            if len(self.cross_entry):
                for i in self.cross_entry:
                    print(i)
                    i.destroy()
                self.cross_entry.clear()
                
            self.entry_o_r_lab = tk.Label(self.frame2, text = 'r: ', bg = '#006665', fg = 'white', font=("Helvetica",9, 'bold'))
            self.entry_o_r_lab.place(width = 25, height = 25, x = 500, y = 25)
            self.entry_o_r = self.Entry(self.frame2)
            self.entry_o_r.text.place(x = 520, y = 27)
            self.cross_entry.extend([self.entry_o_r.text, self.entry_o_r_lab])

            if len(self.done_button_list)>=1:
                for i in self.done_button_list:
                    i.destroy()
                self.done_button_list.clear()
            
            self.done_dimensions = tk.Button(self.frame2, text = 'Done', command = self.get_dimensions_o)
            self.done_dimensions.place(width = 40, height = 20, x=570, y = 60)
            self.done_button_list.append(self.done_dimensions)
    
    # Crossection OptionMenu master function
    def master_crossection_function(self, choice):
        self.display_crossection_picture(choice)
        self.to_calc(choice)

    # Creating arrows
    def create_up_arrow(self):
        x = self.beam_length.get()
        if x:
            self.arrow_up_lab = tk.Label(self.frame2,image = self.resized_arrow_up_pic, bg = '#006665', text = "up_arrow")
            self.arrow_up_lab.place(height = 30, width = 30, x=random.randrange(130,140), y=random.randrange(260,270))
            self.arrow_list.append(self.arrow_up_lab)
            self.entry = self.Entry(self.win)
            self.arrow_len = self.len_lab(self.frame2)
            self.arrow_up_lab.bind('<B1-Motion>', lambda event, txt = self.entry.text, lab = self.arrow_len.arrow_rel_len_lab: self.widget_master_down(event, txt, lab))
            self.input_list.append(self.entry.text)
            self.len_lab_list.append(self.arrow_len.arrow_rel_len_lab)
            print(self.len_lab_list)
            self.grand_load_list.append([self.arrow_up_lab, self.entry.text,self.arrow_len.arrow_rel_len_lab])
        else:
            self.alert_lab.place(width = 200, height = 30, x = 30, y = 10)
            self.alert_lab.destroy()
        return
    def create_down_arrow(self):
        x = self.beam_length.get()
        if x:
            print("Yeah")
        self.arrow_down_lab = tk.Label(self.frame2,image = self.resized_arrow_down_pic, bg = '#006665', text = "down_arrow")
        self.arrow_down_lab.place(height = 30, width = 30, x=random.randrange(130,140), y=random.randrange(140,150), anchor = "c")
        self.arrow_list.append(self.arrow_down_lab)
        self.entry = self.Entry(self.win)
        self.arrow_len = self.len_lab(self.frame2)
        self.arrow_down_lab.bind('<B1-Motion>', lambda event, txt = self.entry.text, lab = self.arrow_len.arrow_rel_len_lab: self.widget_master_up(event, txt , lab))
        self.input_list.append(self.entry.text)
        self.len_lab_list.append(self.arrow_len.arrow_rel_len_lab)
        self.grand_load_list.append([self.arrow_down_lab, self.entry.text,self.arrow_len.arrow_rel_len_lab])
        return
    def create_moment_ac(self):
        self.moment_ac_lab = tk.Label(self.frame2,image = self.resized_moment_ac_pic, bg = '#006665', text = "moment_ac_arrow")
        self.moment_ac_lab.place(height = 30, width = 30, x=random.randrange(130,140), y=random.randrange(140,150))
        self.arrow_list.append(self.moment_ac_lab)
        self.entry = self.Entry(self.win)
        self.arrow_len = self.len_lab(self.frame2)
        self.moment_ac_lab.bind('<B1-Motion>', lambda event, txt = self.entry.text, lab = self.arrow_len.arrow_rel_len_lab: self.widget_master_up(event, txt, lab))
        self.input_list.append(self.entry.text)
        self.len_lab_list.append(self.arrow_len.arrow_rel_len_lab)
        self.grand_load_list.append([self.moment_ac_lab , self.entry.text,self.arrow_len.arrow_rel_len_lab])
        return
    def create_moment_c(self):
        self.moment_c_lab = tk.Label(self.frame2,image = self.resized_moment_c_pic, bg = '#006665', text = "moment_c_arrow")
        self.moment_c_lab.place(height = 30, width = 30, x=random.randrange(130,140), y=random.randrange(140,150))
        self.arrow_list.append(self.moment_c_lab)
        self.entry = self.Entry(self.win)
        self.arrow_len = self.len_lab(self.frame2)
        self.moment_c_lab.bind('<B1-Motion>', lambda event, txt = self.entry.text, lab = self.arrow_len.arrow_rel_len_lab: self.widget_master_up(event, txt, lab))
        self.input_list.append(self.entry.text)
        self.len_lab_list.append(self.arrow_len.arrow_rel_len_lab)
        self.grand_load_list.append([self.moment_c_lab, self.entry.text,self.arrow_len.arrow_rel_len_lab])
        return
    def create_uniform_load(self):
        self.uniform_load_lab = tk.Label(self.frame2,image = self.resized_g_uniform_pic, bg = '#006665', text = "uniform_load_arrow")
        self.uniform_load_lab.place(height = 40, width = 80, x=random.randrange(130,140), y=random.randrange(140,150))
        self.arrow_list.append(self.uniform_load_lab)
        self.entry = self.Entry(self.win)
        self.arrow_len = self.len_lab(self.frame2)
        self.uniform_load_lab.bind('<B1-Motion>', lambda event, txt = self.entry.text, lab = self.arrow_len.arrow_rel_len_lab: self.widget_master_up(event, txt, lab))
        self.input_list.append(self.entry.text)
        self.len_lab_list.append(self.arrow_len.arrow_rel_len_lab)
        self.grand_load_list.append([self.uniform_load_lab, self.entry.text,self.arrow_len.arrow_rel_len_lab])
        return
    def create_nonuniform_load(self):
        self.nonuniform_load_lab = tk.Label(self.frame2,image = self.resized_g_nonuniform_pic, bg = '#006665', text = "nonuniform_load_arrow")
        self.nonuniform_load_lab.place(height = 40, width = 80, x=random.randrange(130,140), y=random.randrange(140,150))
        self.arrow_list.append(self.nonuniform_load_lab)
        self.entry = self.Entry(self.win)
        self.arrow_len = self.len_lab(self.frame2)
        self.nonuniform_load_lab.bind('<B1-Motion>', lambda event, txt = self.entry.text, lab = self.arrow_len.arrow_rel_len_lab: self.widget_master_up(event, txt, lab))
        self.input_list.append(self.entry.text)
        self.len_lab_list.append(self.arrow_len.arrow_rel_len_lab)
        self.grand_load_list.append([self.nonuniform_load_lab, self.entry.text,self.arrow_len.arrow_rel_len_lab])
        return
    def create_usd_uniform_load(self):
        self.usd_uniform_load_lab = tk.Label(self.frame2,image = self.resized_g_usd_uniform_pic, bg = '#006665')
        self.usd_uniform_load_lab.place(height = 40, width = 80, x=random.randrange(130,140), y=random.randrange(260,270))
        self.arrow_list.append(self.usd_uniform_load_lab)
        self.entry = self.Entry(self.win)
        self.arrow_len = self.len_lab(self.frame2)
        self.usd_uniform_load_lab.bind('<B1-Motion>', lambda event, txt = self.entry.text, lab = self.arrow_len.arrow_rel_len_lab: self.widget_master_down(event, txt, lab))
        self.input_list.append(self.entry.text)
        self.len_lab_list.append(self.arrow_len.arrow_rel_len_lab)
        self.grand_load_list.append([self.usd_uniform_load_lab, self.entry.text,self.arrow_len.arrow_rel_len_lab])
        return
    def create_usd_nonuniform_load(self):
        self.usd_nonuniform_load_lab = tk.Label(self.frame2,image = self.resized_g_usd_nonuniform_pic, bg = '#006665')
        self.usd_nonuniform_load_lab.place(height = 40, width = 80, x=random.randrange(130,140), y=random.randrange(260,270))
        self.arrow_list.append(self.usd_nonuniform_load_lab)
        self.entry = self.Entry(self.win)
        self.arrow_len = self.len_lab(self.frame2)
        self.usd_nonuniform_load_lab.bind('<B1-Motion>', lambda event, txt = self.entry.text, lab = self.arrow_len.arrow_rel_len_lab: self.widget_master_down(event, txt, lab))
        self.input_list.append(self.entry.text)
        self.len_lab_list.append(self.arrow_len.arrow_rel_len_lab)
        self.grand_load_list.append([self.usd_nonuniform_load_lab, self.entry.text,self.arrow_len.arrow_rel_len_lab])
        return
    
    # Creating supports
    def create_simple_support(self):
        self.simple_support_lab = tk.Label(self.frame2, text = 'pinned', image = self.resized_beam_simple_support)
        self.simple_support_lab.place(height = 30, width = 30, x=random.randrange(300,400), y=random.randrange(40,100))
        self.arrow_len = self.len_lab(self.frame2)
        # print(self.support_list[0].cget("Text"))
        self.simple_support_lab.bind('<B1-Motion>', lambda event , lab = self.arrow_len.arrow_rel_len_lab : self.support_master(event, lab))
        self.support_list.append(self.simple_support_lab)
        return

    def create_roller_support(self):
        self.roller_support_lab = tk.Label(self.frame2, text = 'roller', image = self.resized_roller_support_pic, bg = "#006665")
        self.roller_support_lab.place(height = 25, width = 25, x=random.randrange(300,400), y=random.randrange(40,100))
        # print(self.support_list[0].cget("Text"))
        self.roller_support_lab.bind('<B1-Motion>', self.support_master)
        self.support_list.append(self.roller_support_lab)
        return
    
    def create_fixed_support_left(self):
        if(len(self.support_list)):
            for i in self.support_list:
                if (i.cget('text') == 'fixed'):
                    self.support_list.remove(i)
        if(len(self.support_choice_list)):
            for i in self.support_choice_list:
                i.destroy()
            self.support_choice_list.clear()
        self.fixed_support_lab_left = tk.Label(self.frame2, text = "fixed", image = self.resized_beam_fixed_support)
        self.fixed_support_lab_left.place(height = 100, width = 30, x=10, y = 170)
        self.support_list.append(self.fixed_support_lab_left)
        # self.fixed_support_lab.bind('<B1-Motion>', self.support_master)
        self.support_choice_list.append(self.fixed_support_lab_left)
        return
    def create_fixed_support_right(self):
        if(len(self.support_list)):
            for i in self.support_list:
                if (i.cget('text') == 'fixed'):
                    self.support_list.remove(i)
        if(len(self.support_choice_list)):
            for i in self.support_choice_list:
                i.destroy()
            self.support_choice_list.clear()
        self.fixed_support_lab_right = tk.Label(self.frame2, text = "fixed", image = self.resized_beam_fixed_support)
        self.fixed_support_lab_right.place(height = 100, width = 30, x=445, y = 170)
        self.support_list.append(self.fixed_support_lab_right)
        self.support_choice_list.append(self.fixed_support_lab_right)
        return
    def create_fixed_support_end(self):
        if(len(self.support_list)):
            for i in self.support_list:
                if (i.cget('text') == 'fixed'):
                    self.support_list.remove(i)
        if(len(self.support_choice_list)):
            for i in self.support_choice_list:
                i.destroy()
            self.support_choice_list.clear()

        self.fixed_support_lab_1 = tk.Label(self.frame2, text = "fixed", image = self.resized_beam_fixed_support)
        self.fixed_support_lab_1.place(height = 100, width = 30, x=10, y = 170)
        self.support_list.append(self.fixed_support_lab_1)
        self.support_choice_list.append(self.fixed_support_lab_1)

        self.fixed_support_lab_2 = tk.Label(self.frame2, text = "fixed", image = self.resized_beam_fixed_support)
        self.fixed_support_lab_2.place(height = 100, width = 30, x=445, y = 170)
        self.support_list.append(self.fixed_support_lab_2)
        self.support_choice_list.append(self.fixed_support_lab_2)
        # self.fixed_support_lab.bind('<B1-Motion>', self.support_master)
        return

    def create_no_fixed_support(self):
        if(len(self.support_list)):
            for i in self.support_list:
                if (i.cget('text') == 'fixed'):
                    self.support_list.remove(i)
        if(len(self.support_choice_list)):
            for i in self.support_choice_list:
                i.destroy()
            self.support_choice_list.clear()
        return

    def master_support(self, choice):
        if choice == "Fixed Left":
            self.create_fixed_support_left()
        elif choice == "Fixed Right":
            self.create_fixed_support_right()
        elif choice == "Fixed Ended":
            self.create_fixed_support_end()
        elif choice == "No Fixed Support":
            self.create_no_fixed_support()
    
    def read_support_text(self):
        for i in self.support_list:
            print(i.cget('text'))
    


    def get_arrow_length(self, wid):
        entry = int(self.beam_length_number.get())
        print(entry)
        init = 1
        # print("In meters : " + str(math.floor((int(entry)/400)*(int(i.winfo_x())-610))))
        return (int(entry)/400)*(int(wid.winfo_x())-40)

    def get_support_length(self):
        entry = int(self.beam_length_number.get())
        print(entry)
        init = 1
        for i in self.support_list:
            # print("In meters : " + str(math.floor((int(entry)/400)*(int(i.winfo_x())-610))))
            print("In meters : " + str(int((int(entry)/400)*(int(i.winfo_x())-150))))
            print("Support"+str(init)+" : "+str(i.winfo_x()))
            init+=1
        
        print("Label : " + str(self.beam_lab.winfo_x()))
    
    def nodes(self):
        self.nodes = 1
        for i in self.support_list:
            if i.cget("text") != "fixed":
                self.nodes +=1
        return self.nodes
    
    def elements(self):
        self.elements = 1
        for i in self.support_list:
            if i.cget("text") != "fixed":
                self.elements +=1
        return self.elements
        

    def length_in_meters(self):
        self.get_arrow_length()
        self.get_support_length()
        self.print_nodes_and_elements()

    def add_dist_lab_up(self, e, lab):
        
        self.lenn = round(self.get_arrow_length(e.widget), 2)
        if self.lenn > (int(self.beam_length_number.get())+0.3):
            self.lenn = self.lenn+0.3
        lab.config(text = str(self.lenn+0.5))
        ex = e.widget.master.winfo_pointerx() - e.widget.master.winfo_rootx()
        ey = e.widget.master.winfo_pointery() - e.widget.master.winfo_rooty()
        if self.lenn <= int(self.beam_length_number.get()):
            lab.place(height = e.widget.winfo_height(), width = e.widget.winfo_width(), x=ex+7,y=ey-55,anchor='center')
        return self.lenn

    def add_dist_lab_down(self, e, lab):
        
        self.lenn = round(self.get_arrow_length(e.widget), 2)
        if self.lenn > (int(self.beam_length_number.get())+0.3):
            self.lenn = self.lenn+0.3
        lab.config(text = str(self.lenn+0.5))
        ex = e.widget.master.winfo_pointerx() - e.widget.master.winfo_rootx()
        ey = e.widget.master.winfo_pointery() - e.widget.master.winfo_rooty()
        if self.lenn <= int(self.beam_length_number.get()):
            lab.place(height = e.widget.winfo_height(), width = e.widget.winfo_width(), x=ex+27,y=ey,anchor='center')
    
    def calc_reactions(self):
        self.no_of_reactions = 0
        if len(self.support_list)>=1:
            print("Length of support list : " + str(len(self.support_list)))
            for i in self.support_list:
                print(i.cget('text'))
                if (i.cget('text') == 'fixed'):
                    self.no_of_reactions +=3
                elif (i.cget('text') == 'pinned'):
                    self.no_of_reactions += 2 
                elif (i.cget('text') == 'roller'):
                    self.no_of_reactions +=1
        self.static_indeterminacy = cf.calc_static_indeterminacy(self.no_of_reactions)
        print("Total no.of reactions : " + str(self.no_of_reactions))
        print("Static indeterminacy : " + str(self.static_indeterminacy))
    
    
        
    def add_manual_arrow_location(self):
        pass

    def get_dimensions_r(self):
        
        self.dimensions_dict = {"B" : self.entry_r_B.text.get(1.0, "end-1c"), "H" : self.entry_r_H.text.get(1.0, "end-1c")}
        return self.dimensions_dict
    
    def get_dimensions_i(self):
        
        self.dimensions_dict = {"B" : self.entry_i_B.text.get(1.0, "end-1c"), "h": self.entry_i_h.text.get(1.0, "end-1c"), "H" : self.entry_i_H.text.get(1.0, "end-1c"), "b" : self.entry_i_b.text.get(1.0, "end-1c")}
        return self.dimensions_dict
        
    
    def get_dimensions_t(self):
        
        self.dimensions_dict = {"B" : self.entry_t_B.text.get(1.0, "end-1c"), "h": self.entry_t_h.text.get(1.0, "end-1c"), "H" : self.entry_t_H.text.get(1.0, "end-1c"), "b" : self.entry_t_b.text.get(1.0, "end-1c")}
        return self.dimensions_dict
        

    def get_dimensions_c(self):

        self.dimensions_dict = {"B" : self.entry_c_B.text.get(1.0, "end-1c"), "h": self.entry_c_h.text.get(1.0, "end-1c"), "H" : self.entry_c_H.text.get(1.0, "end-1c"), "b" : self.entry_c_b.text.get(1.0, "end-1c")}
        return self.dimensions_dict
        
    
    def get_dimensions_o(self):
        
        self.dimensions_dict = {"r" : self.entry_o_r.text.get(1.0, "end-1c")}
        return self.dimensions_dict
    
    def get_arrow_final_length(self, lis):
        print(lis)
    
    
          
    def master_submit(self, lis):
        self.add_beam_length_label()
        self.get_arrow_final_length(lis)
        print("Arrow details : ")
        for i in range(0, len(self.grand_load_list)):
            for j in range(0, len(self.grand_load_list[i])):
                if j == 0:
                    print(self.grand_load_list[i][j].cget('text'))
                elif j == 1:
                    print(self.grand_load_list[i][j].get(1.0, "end-1c"))
                elif j == 2:
                    print(self.grand_load_list[i][j].cget('text'))
            

        # #generating dictionary
        # # The dictionary will include the arrow position relative to the beam as the key
        # # and it will

        # for i in self.input_list:
        #     print(i.get(1.0, "end-1c"))
    
    
    
    
    
    #Entry class
    class Entry:
        def __init__(self, win):
            self.text = tk.Text(win, height = 1, width = 4)
    class len_lab:
        def __init__(self, win):
            self.arrow_rel_len_lab = tk.Label(win, bg = "#006665")
            print("new label")
            
    
root = Window()


# If the x coordinate of the arrow is below 150 and above 130 take it as 150. 
#That is the only slight problem

# If the x coordinate of the arrow is below 550 and above 530 take it as 550. 
#That is the only slight problem

