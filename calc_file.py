# This will be a file that will be able to convert the front end inputs in the form of calculations and will be able to 
#   give the answer for Vmax and Shear force diagram

import main_file as front
import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image

total_nodes = 0
total_elements = 0
for i in front.root.support_list:
    total_nodes +=1
    if i.cget("text") != "fixed" : 
        total_elements +=1
    
print("Total Nodes : " + str(total_nodes))
print("Total Elements : " + str(total_elements))