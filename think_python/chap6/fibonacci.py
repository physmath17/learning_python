def fibonacci(n) :
    """ returns the nth Fibonacci number """
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__" :
    m = int(input("Enter the number of terms of the Fibonacci sequence you want printed : "))
    for i in range(1, m+1) :
        print(fibonacci(i))
