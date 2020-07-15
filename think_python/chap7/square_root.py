import math

def mysqrt(a) :
    """ computes the square root of 'a' using the Newton's method """
    x = 5
    while True :
        y = (x + a/x) / 2
        if y == x :
            break
        x = y
    return y

def test_square_root(n) :
    print('a    mysqrt(a)            math.sqrt(a)         difference')
    print('---------------------------------------------------------')
    for a in range(1, n + 1) :
        print(a, "  ", '%-20.12f' % mysqrt(a), '%-20.12f' % math.sqrt(a), abs(mysqrt(a) - math.sqrt(a)))


if __name__ == "__main__" :
    m = int(input("Enter the number up to which you want to calculate the square root : "))
    test_square_root(m)
