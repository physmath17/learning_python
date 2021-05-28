# python-turtle code for Archimedean Spiral
'''
references:
http://en.wikipedia.org/wiki/Spiral
https://en.wikipedia.org/wiki/Archimedean_spiral


Archimedean Spiral ---> It is the locus of points corresponding to the locations over time of a point moving away from a fixed point with a constant speed along a line that rotates with constant angular velocity

r = a + b*theta

two parameters : a ---> moves the centerpoint of the spiral outward from the origin (positive a toward theta = 0 and negative a toward theta = pi)
b ---> controls the distance between loops
'''

import turtle
# from swampy.TurtleWorld import *

def Archimedean_spiral(t, a, b, n, l) :
    """ draws an Archimedean spiral with parameters a, b using line segments of length l
    t : turtle, n : number of line segments to be drawn
    """
    theta = 0.0

    for i in range(n) :
        r = a + b*theta
        t.fd(l)
        dtheta = 1 / r

        t.lt(dtheta)
        theta += dtheta


# create the turle
bob = turtle.Turtle()
Archimedean_spiral(bob, 0.05, 0.0007, 1000, 3)
bob.hideturtle()
turtle.mainloop()

