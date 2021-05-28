import turtle
import time

t1 = time.time()

bob = turtle.Turtle()
# lob = turtle.Turtle()

def koch(t, x) :
    """ draws a Koch curve of length x """
    if x < 3 :
        t.fd(x)
        return
    koch(t, x/3)
    t.lt(60)
    koch(t, x/3)
    t.rt(120)
    koch(t, x/3)
    t.lt(60)
    koch(t, x/3)


def snowflake(t, n) :
    """ draws a (Koch) snowflake (a triangle with a Koch curve for each side) """
    for i in range(3) :
        koch(t, n)
        t.rt(120)

def pos(t, x, y) :
    t.pu()
    t.goto(x, y)
    t.pd()

#koch(bob, 300)
bob.speed(0)
#lob.speed(0)
bob.color('blue')
#lob.color('blue')
'''
for i in range(4) :
    pos(bob, -300, 200 - i*150)
    snowflake(bob, 100)
    pos(bob, 150, 200 - i*150)
    snowflake(bob, 100)
    pos(lob, 350, 200 - i*150)
    snowflake(lob, 100)

pos(bob, -150, -50)
snowflake(bob, 100)
pos(bob, 0, -50)
snowflake(bob, 100)
'''


snowflake(bob, 300)

bob.hideturtle()
#lob.hideturtle()
turtle.mainloop()


t2 = time.time()
print(t2 - t1)
