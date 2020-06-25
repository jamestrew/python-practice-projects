import math


""" Q1 - Function Translation """
def cylinder_volume(r, h):
    """ returns the volume of a cylinder for a given cylinder with radius r and height h """
    return math.pi * pow(r, 2) * h

def future_value(p, r, t):
    return p * pow(1+r, t)

def height(v, t):
    g = 9.81
    return v * t - (1/2)*(g * pow(t, 2))

""" Q2 - Conversions """
def ounce2ml(ounce):
    gallon = ounce / 128
    return gallon / 3.78541 * 1000

""" Q3 Course Grade """
def cs135_gade(midterm1, midterm2, final):
    """ grade allocation:
            midterm1, midterm2  = 30%
            final = 40% """
    return (midterm1*0.3)+(midterm2*0.3)+(final*0.4)

print(cs135_gade(80, 80, 100))
