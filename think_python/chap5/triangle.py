def is_triangle(a, b, c) :
    """ takes a, b, c as the inputs and converts them to integers, these are the side lengths of the triangle """
    if int(a) + int(b) > int(c) and int(c) + int(b) > int(a) and int(c) + int(a) > int(b) :
        print("Yes, the given side lengths form a triangle.")
    elif int(a) + int(b) == int(c) and int(b) + int(c) >= int(a) and int(c) + int(a) >= int(b) :
        print("We have a degenerate triangle.")
    elif int(b) + int(c) == int(a) and int(c) + int(a) >= int(b) and int(a) + int(b) >= int(c) :
        print("We have a degenerate triangle.")
    elif int(c) + int(a) == int(b) and int(a) + int(b) >= int(c) and int(b) + int(c) >= int(a) :
        print("We have a degenerate triangle.")
    else :
        print("No, the given side lengths do not forma triangle.")


x = float(input('enter the first side : '))
y = float(input('enter the second side : '))
z = float(input('enter the third side : '))

is_triangle(x, y, z)
