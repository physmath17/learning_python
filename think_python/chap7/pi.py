import math

def factorial(n) :
    """ compute n! """
    if n == 0 :
        return 1
    else :
        return n*factorial(n-1)

def estimate_pi() :
    """ uses the infinte series given by Ramanujan to estimate the value of pi """
    s = 0.0
    k = 0
    while True :
        s = s + factorial(4*k)*(1103 + 26390*k) / (pow(factorial(k),4) * pow(396, 4*k))
        pi = 9801 / (2*s*math.sqrt(2))
        
        if abs(pi - math.pi) < 1e-15 :
            break
        k += 1
    print("The value of pi is = {}".format(pi))

estimate_pi()

