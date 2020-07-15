def pm4() :
	print('+', '- - - - + '*4)

def bar4() :
	print('|', '        | '*4)

def pm2() :
	print('+', '- - - - + '*2)

def bar2() :
	print('|', '        | '*2)

def do_twice(f) :
	f()
	f()

def do_four(f) :
	do_twice(f)
	do_twice(f)

def grid4() :
	pm4()
	do_four(bar4)
	pm4()
	do_four(bar4)

def grid2() :
	pm2()
	do_four(bar2)
	pm2()
	do_four(bar2)
	pm2()

grid2()
do_twice(grid4)
pm4()

