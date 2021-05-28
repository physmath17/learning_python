def recurse(n, s) :
    """ takes non-negative integer n and a number s as arguments and returns the sum of s and non-negative intgers from n through 0"""
    if n == 0 :
        print(s)
    else :
        recurse(n-1, n + s)

recurse(3, 0.5)
recurse(2, -1)
recurse(10, 0)
recurse(-1, 0.5)