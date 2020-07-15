from distance_formula import distance
import math

def area(r) :
    return math.pi*r**2

def circle_area(xc, yc, xp, yp) :
    """ (xc, yc) are the coordinates of the center of the circle and (xp, yp) are the coordinates of a point on the circle """
    return area(distance(xc, yc, xp, yp))


if __name__ == "__main__" :
    cx = float(input("Enter the x-coordinate of the center : "))
    cy = float(input("Enter the y-coordinate of the center : "))
    px = float(input("Enter the x-coordinate of the point on the circle : "))
    py = float(input("Enter the y-coordinate of the point on the circle : "))


    a = circle_area(cx, cy, px, py)
    print("The area of the circle is {}.".format(a))

