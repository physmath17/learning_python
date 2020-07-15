import turtle
import math

# creating a turtle object
# bob = turtle.Turtle()
'''
print(bob)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
bob.lt(90)
bob.fd(100)
'''

# encapsulation - wrapping a piece of code like the above
def square(t, length) :
    for i in range(4) :
        t.fd(length)
        t.lt(90)
# square(bob, 200)

# generalization - adding a parameter to function
def polygon(t, n, length) :
    for i in range(n) :
        t.fd(length)
        t.lt(float(360/n))
'''
----------------------------------------------------------------------------
n and length are keyword arguments because they include the parameter names as “keywords”
----------------------------------------------------------------------------

bob.pu()
bob.rt(90)
bob.fd(490)
bob.rt(90)
bob.fd(100)
bob.lt(180)
bob.pd()
for i in range(15) :
    polygon(3 + i, bob, (40 + i*10))

n = int(input('enter the number of sides :'))
length = int(input('enter the side length : '))

def my_circle(t, r) :
    circumference = 2*math.pi*r
    if n*length == int(circumference) :
        polygon(t, n, length)
    else :
        print('change the number of sides or length of each side')

bob = turtle.Turtle()

def my_circle2(t, n, r) :
    circumference = 2*math.pi*r
    length = circumference/n
    t.color('green')
    polygon(t, n, length)
    t.color('blue')
    t.circle(r)

----------------------------------------------------------------------------interface of a function is a summary of how it is used - parameters, what it does, return value... and interface is "clean" if it allows the caller to do what they want without  dealing with unnecessary details.

In this example, r belongs in the interface because it specifies the circle to be drawn. n is less appropriate because it pertains to the details of how the circle should be rendered. Rather than clutter up the interface, it is better to choose an appropriate value of n depending on circumference :
----------------------------------------------------------------------------
'''

def circle(t, r) :
    circumference = 2*math.pi*r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)

# circle(bob, 100)

def polyline(t, n, angle, length) :
    for i in range(n) :
        t.fd(length)
        t.lt(angle)

'''
def my_arc(t, r, angle) :
    t.color('red')
    t.lt(120)
    arc_length = 2*math.pi*angle*r/360
    n = 50
    length = arc_length/n
    
    polyline(t, n, angle/n, length)
'''

def arc(t, r, angle) :
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_angle, step_length)
'''
for i in range(n):
        t.fd(step_length)
        t.lt(step_angle) '''

# arc(bob, 100, 60)
    
# turtle.mainloop()

'''
we could define polygon and circle as follows:

def polygon(t, n, length) :
    angle = 360.0 / n
    polyline(t, n, length, angle)

def circle(t, r) :
    arc(t, r, 360)
---------------------------------------------------------------------------
the process of rearranging a program to improve interfaces and facilitate code reuse is called refactoring
----------------------------------------------------------------------------
'''
