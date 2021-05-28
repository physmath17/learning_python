def check_fermat(a, b, c, n) :
    """ takes a, b, c as the inputs and converts them to integers. 
    n is the power. Verifies Fermat's last theorem for integers a, b, c and power n > 2
    """

    if int(a)**n + int(b)**n == int(c)**n and n > 2 and a > 0 and b > 0 and c > 0 :
        print("Holy smokes, Fermat was wrong!")
    elif n < 2 or a <= 0 or b <= 0 or c <= 0 :
        print("The integers must be positive integers only and the power should be greater than or equal to 2!")
    elif int(a)**n + int(b)**n == int(c)**n and n == 2 and a > 0 and b > 0 and c > 0 :
        print("Hooray! You have got yourself a Pythagorean Triplet.")
    else :
        print("No that doesn’t work, Fermat was right!")


x = float(input('enter the first positive integer : '))
y = float(input('enter the second positive integer : '))
z = float(input('enter the third positive integer : '))
n = int(input('enter the power : '))


check_fermat(x, y, z, n)
