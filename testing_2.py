from beam_details import Beam
from sympy import symbols
from sympy.core import S, Symbol, diff, symbols
from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk   
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import random
import calc_file as cf
import math
import time

#Create window
win = tk.Tk()
win.geometry('1000x650')
win.configure(bg = 'black')

frame1 = tk.Frame(master=win, width=280, height=630, bg='#006665')
frame1.pack(fill=tk.BOTH, padx=10, pady=15,side=tk.LEFT, expand=False)
frame2 = tk.Frame(master=win, width=680, height=315, bg="#006665")
frame2.pack(fill=tk.Y, padx=5, pady=15,side=tk.TOP, expand=False)
frame3 = tk.Frame(master=win, width=680, height=315, bg="#006665")
frame3.pack(fill=tk.Y, padx=5, pady=15,side=tk.BOTTOM, expand=False)

entry = 3

#Graph init
graph_canvas = tk.Canvas(frame3, bg = '#006665',highlightthickness=0, highlightbackground="#006665")
graph_canvas.place(width = 440, height = 250, x = 40, y=10)
graph_canvas.create_line(0,125, 400, 125, fill = "black")
graph_canvas.create_line(0,0, 0, 250, fill = "black")

x = 0
y = 0

beam_length = 3.0

def graph():
    R1,R2, R3, R4 = symbols('R1, R2, R3, R4') #  
    b = Beam(beam_length, 200*(10**9), 400*(10**-6))
    b.apply_load(10, 0, 0, end = 3)
    # b.apply_load(10, 2.75, -1)

    b.apply_load(R1, 0, -1)
    b.apply_load(R2, 1, -1)
    b.apply_load(R3, 2, -1)
    b.apply_load(R4, 3, -1)
    # b.bc_deflection = [(0, 0), (8, 0)]
    b.bc_deflection = [(0, 0),(1,0), (2,0), (3,0)] #
    b.solve_for_reaction_loads(R1,R2, R3, R4) # 
    shear_force = b.shear_force()
    shear_force = str(shear_force)
    give_shear_force_list(shear_force)

def give_shear_force_list(shear_force):

    nosp_shear_force = shear_force.translate({ord(' '): None})
    shear_force_list = nosp_shear_force.split(")")
    shear_force_list.remove(shear_force_list[-1])
    for i in range(0, len(shear_force_list)):
        shear_force_list[i] = shear_force_list[i]+")"
    sf_dict_list(shear_force_list)

def sf_dict_list(sf_list):
    beam_shear_list = []
    nums = 0
    for i in sf_list:
        nums+=1
        dict = {}

        if i[0] =='+':
            #Then it means it is +
            if ",0)" in i:
                # Point Load from down
                dict['name'] = str(nums)

                j = i
                templist = j.split("*")
                point_load_magnitude = round(float(templist[0]), 2)
                dict["shear_magnitude"] = point_load_magnitude

                #Location
                tl1 = i.split(',')
                dict["location"] = tl1[1]

                #Type
                dict["type"] = "point"
  
            elif ",1)" in i:
                # Distributed Load is beginning

                dict['name'] = str(nums)


                j = i
                templist = j.split("*")
                point_load_magnitude = round(float(templist[0]), 2)
                dict["shear_magnitude"] = point_load_magnitude

                #Location
                tl1 = i.split(',')
                dict["location"] = tl1[1]

                #Type
                dict["type"] = "distributed"
    
        elif i[0] == "-":
            #Then it means it is -
            if ",0)" in i:
                #Point Load from up
                dict['name'] = str(nums)


                j = i
                templist = j.split("*")
                point_load_magnitude = round(float(templist[0]), 2)
                dict["shear_magnitude"] = point_load_magnitude

                #Location
                tl1 = i.split(',')
                dict["location"] = tl1[1]

                #Type
                dict["type"] = "point"
            elif ",1)" in i:
                #Distributed Load is ending

                dict['name'] = str(nums)

                j = i
                templist = j.split("*")
                point_load_magnitude = round(float(templist[0]), 2)
                dict["shear_magnitude"] = point_load_magnitude

                #Location
                tl1 = i.split(',')
                dict["location"] = tl1[1]

                #Type
                dict["type"] = "distributed"
        
        else : 
            #Then it means this is the absolute first shear force
            if ",0)" in i:
                # Point Load from down
                dict['name'] = str(nums)

                j = i
                templist = j.split("*")
                point_load_magnitude = round(float(templist[0]), 2)
                dict["shear_magnitude"] = point_load_magnitude

                #Location
                tl1 = i.split(',')
                dict["location"] = tl1[1]

                #Type
                dict["type"] = "point"

            
              
            elif ",1)" in i:
                # Distributed Load is beginning
                dict['name'] = str(nums)

                j = i
                templist = j.split("*")
                point_load_magnitude = round(float(templist[0]), 2)
                dict["shear_magnitude"] = point_load_magnitude

                #Location
                tl1 = i.split(',')
                dict["location"] = tl1[1]

                #Type
                dict["type"] = "distributed"
        beam_shear_list.append(dict)

    convert_to_coordinates(beam_shear_list)        

def convert_to_coordinates(list):
    #Remember that the dict is already in the exact order you want it, just start converting each dict to a line
    print(list)
    coordinate_x = np.arange(0, beam_length+0.01, 0.01)
    coordinate_x = coordinate_x.tolist()
    for i in range(0, len(coordinate_x)):
        coordinate_x[i] = round(float(coordinate_x[i]), 2)
    print(len(coordinate_x))
    coordinate_y = []
    '''
        This is what I am expecting
            We need to loop through the list, but in a correct order. We need to be able to get the location of the first shear
            and create the necessary coordinates and then add them to the lists.

            Now remember, x_coordinate => location of impact, y_coordinate => shear

            Now your shear depends on the previous shears as well. That is why it is very important to recognize the forces.
            If there is a pin force at x, then the coordinate will be x1,x1 in the coordinate_x list and it will be (y1, shear_magnitude)

    '''
    '''
        These are some cases :-
        1) No shear
        2) No change in shear
        3) Point load enters
        4) Distributed load begins
        5) Distributed load 

    '''
    i = 0
    j = 0
    y = 0 
    for j in range(0, len(list)):
        for i in range(0, len(coordinate_x)):
            if float(list[j]["location"]) == coordinate_x[i]:
                print("load location : " + str(coordinate_x[i]) + "=" + list[j]["location"])
                print ("load type at that location : ", list[j]["type"])
                print("load magnitude at the location : ", list[j]["shear_magnitude"])
                coordinate_x.insert(i, coordinate_x[i])
                # y = y + float(list[j]["shear_magnitude"])
                # coordinate_y.append(y)
                print("location: ", coordinate_x[i], "y", y, " ")
                print('\n')
                break
    
    for i in range(0, len(coordinate_x)):
        pass
        
        
    print("length of coordinate_x : ",len(coordinate_x))
    print ("length of coordinate_y : ",len(coordinate_y))

    
    
    
    # fig, ax = plt.subplots()
    # ax.plot(coordinate_x, coordinate_y)

    # ax.grid()

    # fig.savefig("test.png")
    # plt.show()

    # print(coordinate_x)
    # print(coordinate_y)
        




        


    
    # canvas = FigureCanvasTkAgg(fig, root)
    # canvas.draw()
    # canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)


mybutton = Button(frame1, text = "Graph It!", command = graph)
mybutton.place(width = 70, height = 20, x = 40, y = 10)



win.mainloop()

# win = tk.Tk()
# win.geometry('1000x650')
# win.configure(bg = 'black')






