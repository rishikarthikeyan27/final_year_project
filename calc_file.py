#Remember that this file is strictly for just calculations, so tkinter stuff must be going on

import numpy as np
import matplotlib.pyplot as plt

def calc_rbeam_centroid(B, H):
    centroid = H/2
    return centroid

def calc_tbeam_centroid(B,h,H, b):
    centroid_numerator = ((H+(h/2))*(B*h))+((H/2)*(b*H))
    centroid_denominator = ((B*h)+(b*H))
    centroid = centroid_numerator/centroid_denominator
    return centroid

def calc_ibeam_centroid(B, h, H, b):
    A1 = B*h 
    y1 = h+H+(h/2)

    A2 = b*H 
    y2 = h+(H/2)

    A3 = B*h 
    y3 = h+H+(h/2)

    centroid_numerator = (A1*y1)+(A2*y2)+(A3*y3)
    centroid_denominator = (A1+A2+A3)

    centroid = (centroid_numerator/centroid_denominator)

    return centroid

def calc_cbeam_centroid(B, h, H, b):
    A1 = B*h 
    y1 = h+H+(h/2)

    A2 = b*H 
    y2 = h+(H/2)

    A3 = B*h 
    y3 = h+H+(h/2)

    centroid_numerator = (A1*y1)+(A2*y2)+(A3*y3)
    centroid_denominator = (A1+A2+A3)

    centroid = (centroid_numerator/centroid_denominator)

    return centroid


def calc_obeam_centroid(r):
    pass

def calc_tbeam_i(B, h, H, b):
    centroid_numerator = ((H+(h/2))*(B*h))+((H/2)*(b*H))
    centroid_denominator = ((B*h)+(b*H))
    centroid = centroid_numerator/centroid_denominator
    I1 = (1/12)*B*(h**3)
    I2 = (1/12)*b*(H**3)
    A1 = B*h
    A2 = b*H
    d1 = (H+(h/2)) - centroid
    d2 = centroid - (H/2)
    t_i = (I1 + (A1*(d1**2))) + (I2 + (A2*(d2**2)))
    return t_i

def calc_cbeam_i(B, h, H, b):
    
    I1 = (1/12)*B*(h**3)
    A1 = B*h
    
    I2 = (1/12)*b*(H**3)
    #d1,d2
    d1 = (H/2)+(h/2)
    d2 = 0
    c_i = (2*(I1+ (A1*(d1**2)))) + I2
    return c_i


def calc_ibeam_i(B,h,H,b):
    I1 = (1/12)*B*(h**3)
    I2 = (1/12)*b*(H**3)
    A1 = B*h
    A2 = b*H
    #d1,d2
    d1 = ((h/2)+H+(h/2))/2
    d2 = 0
    i_i = (2*(I1 + (A1*(d1**2)))) + (I2 + (A2*(d2**2)))
    return i_i


def calc_rbeam_i(B,H):
    r_i = (1/12)*B*(H**3)
    return r_i

def calc_obeam_i(r):
    o_i = ((3.14)*(r**4))/4
    return o_i

def stiffness_matrix(E,I, l):
    K = []
    c = ((E*I)/L**3)
    K = [[c*12, c*6*L, -12*c, 6*L*c]
        ,[6*L*c, (4 *c* (L**2)), -6*L*c, (2*c*(L**2))]
        ,[-12*c, -6*L*c, 12*c, -6*L*c]
        ,[6*L*c, (2*c*(L**2)), -6*L*c, (4*c*(L**2))]]
    return K

def calc_static_indeterminacy(no_of_reactions):
    return (no_of_reactions - 3)

def max_shear_stress(x):
    return(x)

def calc_rbeam_shear_stress(shear_force, B, H):
    V = shear_force
    i = calc_rbeam_i(B, H)
    print("i : ", i)
    centroid = calc_rbeam_centroid(B, H)
    print("centroid : ", centroid)
    Q = 0
    y = H/2
    huge_list = []
    x = True
    while x:
        print("while true")
        if (y >= (-H/2)) and (y <= H/2):
            print("if")
            A = B*((H/2)-y)
            y_dash = (1/2)*((H/2)+y)
            Q = A * y_dash
            tou = ( (V/(2*i))*(((H**2)/4) - (y**2)) )
            tou = tou*1000
            huge_list.append(tou)
            y-=1
        else:
            x = False
    y = []
    start = int(-H/2)
    finish = (int(H/2)+1)
    for i in range(start, finish):
        y.append(i)
    x = np.array(huge_list)
    plt.title("Matplotlib demo") 
    plt.xlabel("x axis caption") 
    plt.ylabel("y axis caption") 
    plt.plot(x, y) 
    plt.show()
    print('The maximum shear stress is : ',max_shear_stress(max(huge_list)))
    return

def calc_ibeam_shear_stress(shear_force, B, h, H, b):
    V = shear_force
    i = calc_ibeam_i(B, h, H, b)
    print("i", i)
    centroid = calc_ibeam_centroid(B, h, H, b)
    y=(H/2)+h
    huge_list = []
    x = True
    D = (H)+(2*h)
    d = H
    while x:
        if ((y<=((H/2)+h)) and (y>H/2)):
            breadth = h-(y-(H/2))
            Area = B*breadth
            y_dash = (breadth/2)+y
            Q = Area * y_dash
            tou = (V/(i*B))*(Q)
            tou = tou*1000
            huge_list.append(tou)
            y-=1

        elif ((y <= H/2) and (y >= 0)):
            tou = (V/(i*b))*(((B*((D**2)-(d**2)))/(8))+((b/2)*(((d**2)/4) - (y**2))))
            tou = tou*1000
            huge_list.append(tou)
            y-=1
        
        elif ((y < 0) and (y >= (-H/2))):
            tou = (V/(i*b))*(((B*((D**2)-(d**2)))/(8))+((b/2)*(((d**2)/4) - ((-y)**2))))
            tou = tou*1000
            huge_list.append(tou)
            y-=1

        elif ((y>=(-((H/2)+h))) and (y<(-H/2))):

            breadth = h-((-y)-(H/2))
            Area = B*breadth
            y_dash = (breadth/2)+(-y)
            Q = Area * y_dash
            tou = (V/(i*B))*(Q)
            tou = tou*1000
            huge_list.append(tou)
            y-=1

        else:
            print(y)
            x = False
    y = []
    start = int((H/2)+h)
    finish = -(int((H/2)+h))-1
    for i in range(start, finish, -1):
        y.append(i)
    y = np.array(y)
    x = np.array(huge_list)
    print("X : ", len(x))
    print("Y : ", len(y))

    plt.title("Matplotlib demo") 
    plt.xlabel("Shear Stress in MPa") 
    plt.ylabel("Beam height in mm") 

    plt.plot(x, y) 
    plt.show()
    print('The maximum shear stress is : ',max_shear_stress(max(huge_list)))
    
    return

def calc_cbeam_shear_stress(shear_force, B, h, H, b):
    V = shear_force
    i = calc_cbeam_i(B, h, H, b)
    print("i", i)
    centroid = calc_cbeam_centroid(B, h, H, b)
    y=(H/2)+h
    huge_list = []
    x = True
    D = (H)+(2*h)
    d = H
    while x:
        if ((y<=((H/2)+h)) and (y>H/2)):
            breadth = h-(y-(H/2))
            Area = B*breadth
            y_dash = (breadth/2)+y
            Q = Area * y_dash
            tou = (V/(i*B))*(Q)
            tou = tou*1000
            huge_list.append(tou)
            y-=1

        elif ((y <= H/2) and (y >= 0)):
            tou = (V/(i*b))*(((B*((D**2)-(d**2)))/(8))+((b/2)*(((d**2)/4) - (y**2))))
            tou = tou*1000
            huge_list.append(tou)
            y-=1
        
        elif ((y < 0) and (y >= (-H/2))):
            tou = (V/(i*b))*(((B*((D**2)-(d**2)))/(8))+((b/2)*(((d**2)/4) - ((-y)**2))))
            tou = tou*1000
            huge_list.append(tou)
            y-=1

        elif ((y>=(-((H/2)+h))) and (y<(-H/2))):

            breadth = h-((-y)-(H/2))
            Area = B*breadth
            y_dash = (breadth/2)+(-y)
            Q = Area * y_dash
            tou = (V/(i*B))*(Q)
            tou = tou*1000
            huge_list.append(tou)
            y-=1

        else:
            print(y)
            x = False
    y = []
    start = int((H/2)+h)
    finish = -(int((H/2)+h))-1
    for i in range(start, finish, -1):
        y.append(i)
    y = np.array(y)
    x = np.array(huge_list)
    print("X : ", len(x))
    print("Y : ", len(y))

    plt.title("Matplotlib demo") 
    plt.xlabel("Shear Stress in MPa") 
    plt.ylabel("Beam height in mm") 

    plt.plot(x, y) 
    plt.show()
    print('The maximum shear stress is : ',max_shear_stress(max(huge_list)))
    
    return

def calc_tbeam_shear_stress(shear_force, B, h, H, b):
    V = shear_force
    i = calc_tbeam_i(B, h, H, b)
    print("i", i)
    centroid = calc_tbeam_centroid(B, h, H, b)
    y = H+h-centroid
    huge_list = []
    x = True
    print("y",y)
    while x:
        print("While true")

        if (y>(H-centroid)):
            print("1st if")
            print("y= ", y)
            print("H-c=", H-centroid)
            breadth = H+h-centroid-y
            A = B*breadth
            y_dash = (breadth/2)+y
            Q = A*y_dash
            tou = (V/(i*B))*(Q)
            tou = tou*1000
            huge_list.append(tou)
            y-=1
            print(y)

        elif (y<=(H-centroid)) and y>0:
            print("2nd if")
            print("y= ", y)
            A1 = B*h 
            y1 = H-centroid+(h/2)
            A2 = ((H-centroid)-y)*b 
            y2 = y+(((H-centroid)-y)/2)
            Q = (A1*y1)+(A2*y2)
            tou = (V/(i*b))*Q
            tou = tou*1000
            huge_list.append(tou)
            y-=1
            print(y)
        elif(y<=0) and y >= (-centroid) :
            print("3rd if")
            breadth = centroid+y
            Area = breadth*b 
            y_dash = (breadth/2)-y
            Q = Area*y_dash
            tou = (V/(i*b))*Q
            tou = tou*1000
            huge_list.append(tou)
            y-=1
            print(y)
        else:
            x = False
    y = []
    start = H+h
    finish = -1
    for i in range(start, finish, -1):
        y.append(i)
    y = np.array(y)
    x = np.array(huge_list)
    print("X : ", len(x))
    print("Y : ", len(y))

    plt.title("Matplotlib demo") 
    plt.xlabel("Shear Stress in MPa") 
    plt.ylabel("Beam height in mm") 

    plt.plot(x, y) 
    plt.show()
    print('The maximum shear stress is : ',max_shear_stress(max(huge_list)))
    
    return


def calc_obeam_shear_stress(shear_force, r):
    V = shear_force
    i = calc_obeam_i(r)
  
    print("i", i)
    y=r
    huge_list = []
    x = True
    print("y",y)
    while x:
        print("While true")
        if (y>0):
            tou = (4*shear_force*((r**2)-(y**2)))/(3*3.14*(r**4))
            huge_list.append(tou)
            y-=1
        elif ((y<=0) and (y>= (-r))):
            tou =  (4*shear_force*((r**2)-((-y)**2)))/(3*3.14*(r**4))  
            huge_list.append(tou)
            y-=1
        else:
            x = False
    y = []
    start = r
    finish = -r-1
    for i in range(start, finish, -1):
        y.append(i)
    y = np.array(y)
    x = np.array(huge_list)
    print("X : ", len(x))
    print("Y : ", len(y))

    plt.title("Matplotlib demo") 
    plt.xlabel("Shear Stress in MPa") 
    plt.ylabel("Beam height in mm") 

    plt.plot(x, y) 
    plt.show()
    print('The maximum shear stress is : ',max_shear_stress(max(huge_list)))
    
    return

# helps interpret the whole front end

def get_results(loads_list, supports_list, dimensions_dict, static_indeterminacy, support_type_name):

    if static_indeterminacy <= 0:
        print("Statically Determinate")
        if support_type_name == "Fixed Right": 
            #How to deal with this when it is statically determinate
            all_loads = []
            up_arrow_sum = 0
            down_arrow_sum = 0
            for load_dict in loads_list:
                if load_dict['load_type'] == "down_arrow":
                    down_arrow_sum += load_dict['load_magnitude']
                    all_loads.append(load_dict['load_magnitude'])
                elif load_dict['load_type'] == "up_arrow":
                    up_arrow_sum += load_dict['load_magnitude']
                    all_loads.append(load_dict['load_magnitude'])
            Ra = up_arrow_sum - down_arrow_sum
            all_loads.append(Ra)
            max_shear_force = max(all_loads)
        elif support_type_name == "Fixed Left":
            #How to deal with this when it is statically determinate
            all_loads = []
            up_arrow_sum = 0
            down_arrow_sum = 0
            for load_dict in loads_list:
                if load_dict['load_type'] == "down_arrow":
                    down_arrow_sum += load_dict['load_magnitude']
                    all_loads.append(load_dict['load_magnitude'])
                elif load_dict['load_type'] == "up_arrow":
                    up_arrow_sum += load_dict['load_magnitude']
                    all_loads.append(load_dict['load_magnitude'])
            Ra = up_arrow_sum - down_arrow_sum
            all_loads.append(Ra)
            max_shear_force = max(all_loads) 
        elif support_type_name == "No Fixed Support":
            #how to deal with this when it is statically determinate
            pass
    elif static_indeterminacy >0:
        print("Statically Indeterminate")
        if support_type_name == "Fixed Right": 
            #How to deal with this when it is statically indeterminate
            pass
        elif support_type_name == "Fixed Left":
            #How to deal with this when it is statically indeterminate
            pass
        elif support_type_name == "Fixed Ended":
            #how to deal with this when it is statically indeterminate
            pass
        elif support_type_name == "No Fixed Support":
            #how to deal with this when it is statically indeterminate
            pass

        
    pass



