def collatz_sequence(n) :
    """ prints the Collatz sequence for a given positive integer n """
    while n!= 1 :
        print(n)
        if n % 2 == 0 :     # n is even
            n = int(n/2)
        else :              # n is odd
            n = int(3*n + 1)

if __name__ == "__main__" :
    n = int(input("Enter the positive integer : "))
    collatz_sequence(n)
    
