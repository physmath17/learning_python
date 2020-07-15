'''
def do_twice(f) :
	f()
	f()

def print_spam() :
	print('spam')

do_twice(print_spam)
'''

def do_twice(f, x) :
        f(x)
        f(x)

def print_twice(a) :
        print(a)
        print(a)

# do_twice(print_twice, 'spam')

def do_four(g, y) :
	do_twice(g, y)
	do_twice(g, y)

do_four(print_twice, 'spam')
