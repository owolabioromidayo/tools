import math
def complex_to_phasor(c):
    """Complex class to phasor tuple"""
    r = round((c.real**2 + c.imag**2)**0.5 , 4)
    ang = round(math.atan(c.imag/c.real) * ((180/math.pi)), 2) #conv to degree
    return r, ang

def phasor_to_complex(p):
    r = p[0]; ang=p[1]
    x = round(r*math.cos(ang), 4)
    y = round(r*math.sin(ang), 4)

    return complex(x,y)
