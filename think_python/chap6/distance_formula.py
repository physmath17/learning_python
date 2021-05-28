from math import sqrt

def distance(a1, b1, a2, b2) :
    """ calculates the Euclidean distance between points (a1, b1) and (a2, b2) """
    dx = a1 - a2
    dy = b1 - b2
    dsq = dx**2 + dy**2
    result = sqrt(dsq)
    return result

if __name__ == '__main__' :
    x1 = float(input("Enter x-coordinate of first point : "))
    y1 = float(input("Enter y-coordinate of first point : "))
    x2 = float(input("Enter x-coordinate of the second point : "))
    y2 = float(input("Enter y-coordinate of the second point : "))

    print("The distance between ({}, {}) and ({}, {}) is {}".format(x1, y1, x2, y2, distance(x1, y1, x2, y2)))
