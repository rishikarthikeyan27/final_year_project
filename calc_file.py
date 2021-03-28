#Remember that this file is strictly for just calculations, so tkinter stuff must be going on

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
    I2 = (1/12)*b*(H**3)
    A1 = B*h
    A2 = b*H
    #d1,d2
    d1 = ((h/2)+H+(h/2))/2
    d2 = 0
    c_i = (2*(I1 + (A1*(d1**2)))) + (I2 + (A2*(d2**2)))
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

def return_q(d):
    #d here is the distance between the line of consideration and neutral axis
    pass


    
     


