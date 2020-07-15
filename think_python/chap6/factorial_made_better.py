def sexy_factorial(n) :
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0 :
            print(space, 'returning 1')
            return 1
    else :
        recurse = sexy_factorial(n-1)
        result = n * recurse
        print(space, 'returning', result)
        return result


sexy_factorial(10)
