from polygon import arc
import turtle
#import math

bob = turtle.Turtle()

def petal(t, r, angle) :
    """ creates one petal of the bob
    t : turtle, r : size of the petal, angle : angle subtended by the arc
    """
    for i in range(2) :
        arc(t, r, angle)
        t.lt(180 - angle)

def flower(t, n, r, angle) :
    """ creates a flower with n petals 
    t : turtle, n : number of petals, r : radius of arcs, angle : angle subtended by the arc 
    """
    for i in range(n) :
        t.lt(360/n)
        petal(t, r, angle)

def pos(t, dist) :
    """ position the turtle (t) forward by dist units without leaving a trail """
    t.pu()
    t.fd(dist)
    t.pd()

# draw the three flowers
pos(bob, -300)
flower(bob, 7, 60, 60)

pos(bob, 300)
flower(bob, 10, 40, 80)

pos(bob, 300)
flower(bob, 20, 140, 20)

bob.hideturtle()
turtle.mainloop()
