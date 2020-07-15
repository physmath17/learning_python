import turtle
import math

bob = turtle.Turtle()

def pie_parts(t, n, length) :
    """ creates a pie with n parts 
    t : turtle, n : number of parts, length : side length of the pie shape 
    """
    t.lt(30)
    angle = 90 + 180/n
    for i in range(n) :
        t.fd(length/2/math.sin(math.pi/n))
        t.lt(angle)
        t.fd(length)
        t.lt(angle)
        t.fd(length/2/math.sin(math.pi/n))
        t.lt(180)
    t.rt(30)

def pos(t, dist) :
    """ position the turtle (t) forward by dist units without leaving a trail """
    t.pu()
    t.fd(dist)
    t.pd()
   
# draw the three flowers
pos(bob, -300)
pie_parts(bob, 5, 100)

pos(bob, 300)
pie_parts(bob, 6, 100)

pos(bob, 300)
pie_parts(bob, 7, 100)

bob.hideturtle()
turtle.mainloop()