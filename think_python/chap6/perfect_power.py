def is_power(a, b) :
    """ returns True if 'a' is a perfect power of 'b'
    a and b are positive integers """
    if a/b == 1 and b > 1 :
        return True
    
    if b == 1 :
        if a == 1 :
            return True
        else :
            return False

    if a % b != 0 :
        return False
    
    return is_power(a/b, b)

if __name__ == "__main__" :
    m = int(input(" Enter the positive number whose powers are to be checked : "))
    n = int(input(" Enter the positive number which we have to check is a power of {} : ".format(m)))
    print(is_power(n, m))
