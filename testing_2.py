from beam_details import Beam
from sympy import symbols

from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk   


root = Tk()
root.title('graphda')
root.geometry('400x200')

def graph():
    R1, R2, R3, R4 = symbols('R1, R2, R3, R4')
    b = Beam(3, 200*(10**9), 400*(10**-6))
    b.apply_load(10, 0, 0, end = 1)
    b.apply_load(10, 2.75, -1)

    b.apply_load(R1, 0, -1)
    b.apply_load(R2, 1, -1)
    b.apply_load(R3, 2, -1)
    b.apply_load(R4, 3, -1)
    # b.bc_deflection = [(0, 0), (8, 0)]
    b.bc_deflection = [(0, 0), (1,0), (2,0), (3,0)]
    b.solve_for_reaction_loads(R1, R2, R3, R4)
    fig = b.shear_force()
    print(fig)
    
    # canvas = FigureCanvasTkAgg(fig, root)
    # canvas.draw()
    # canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)

mybutton = Button(root, text = "Graph It!", command = graph)
mybutton.pack()



root.mainloop()

# win = tk.Tk()
# win.geometry('1000x650')
# win.configure(bg = 'black')






