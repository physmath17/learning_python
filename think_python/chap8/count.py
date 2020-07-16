def count(word, letter) :
	""" counts the number of times letter apears in word """
	ctr = 0
	for alph in word :
		if alph == letter :
			ctr += 1
	print(ctr)


count('banana', 'a')
