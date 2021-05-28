def ack(m, n) :
    """ takes m and n as nonnegative integer inouts and evaluates the Ackermann function for m, n """
    if not (isinstance(m, int) and isinstance(n, int)) :
        print("Ackermann functions takes non-negative integers as input.")
        return None
    elif m < 0 or n < 0 :
        print("Ackermann functions takes non-negative integers as input.")
        return None
    elif m == 0 :
        return n + 1
    elif m > 0 and n == 0 :
        return ack(m - 1, 1)
    else :
        return ack(m - 1, ack(m, n - 1))

# print(ack(3, 4))

if __name__ == "__main__" :
    m = int(input("Enter the first non-negative integer : "))
    n = int(input("Enter the second non-negative integer : "))

    print("The Ackerman function evaluated at {}, {} is A({}, {}) = {}". format(m, n, m, n, ack(m, n)))
