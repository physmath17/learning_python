from math import sqrt

b = float(input("Enter the base of the right triangle : "))
h = float(input("Enter the height of the right triangle : "))

def hypotenuse(c, d) :
    """ c, d are the non-hypotenuse sides of the right triangle """
    l = sqrt(c**2 + d**2)
    return l

print("The hypotenuse of the right triangle with base {} and height {} is {}".format(b, h, hypotenuse(b, h)))
