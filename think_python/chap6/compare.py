m = float(input("Enter the first number : "))
n = float(input("Enter the seoncd number : "))

def compare(x, y) :
    """ returns 1 if x > y, 0 if x = y, and -1 if x < y """
    if x > y :
        return 1
    elif x == y :
        return 0
    else :
        return -1

result = compare(m, n)
print(result)
