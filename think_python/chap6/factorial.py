def factorial(n) :
    """ return the value of n! """
    if n == 0 :
        return 1
    else :
        return n*factorial(n-1)


if __name__ == "__main__" :
    
    m = int(input("Enter the non-negative integer whose factorial you want to find :  "))
    print("The value of {}! is {}.".format(m, factorial(m)))
