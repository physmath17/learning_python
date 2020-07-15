def gcd(a, b) :
    """ returns the greatest common divisor of a, b
    a, b : non-negative integers """

    if a == 0 :
        return b
    if b == 0 :
        return a
    if a*b != 0 :
        r = a % b
        return gcd(b, r)

'''
def gcdbl(a, b) :
    print(b*(a==0) + a*(b==0) + gcdbl(b, a%b)*(a*b != 0))
'''

if __name__ == "__main__" :
    m = int(input("Enter the first positive integer : "))
    n = int(input("Enter the second positive integer : "))

    print("The greates common divisor of {} and {} is {}.".format(m, n, gcd(m, n)))
