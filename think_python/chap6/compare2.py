def is_between(x, y, z) :
    """ returns true if x is less than or equal to y and y is less than or equal to z """
    if x<= y and y<=z :
        return True
    else :
        return False


print(is_between(1, 2, 3))
print(is_between(0, 0, 0))
print(is_between(0.5, 0.9, 0.9))
print(is_between(1.233, 1.232999999999999, 1.2329999999999999999999))
print(is_between(2,1,5))
print(is_between(1,1,0))
