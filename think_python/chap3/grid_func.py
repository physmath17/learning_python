def pm(n) :
	print('+', '- - - - + '*n)

def bar(n) :
	print('|', '        | '*n)

def do_twice(f, x) :
        f(x)
        f(x)

def do_four(f, x) :
        do_twice(f, x)
        do_twice(f, x)

def grid(n) :
	pm(n)
	for i in range(n) :
		do_four(bar, n)
		pm(n)

grid(1)
grid(2)
grid(3)
grid(4)
