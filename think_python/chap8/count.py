def count(word, letter) :
	""" counts the number of times letter apears in word """
	ctr = 0
	for alph in word :
		if alph == letter :
			ctr += 1
	print(ctr)

def count_modified(word, letter, ind) :
    """ counts the number of times letter appears in word starting at index ind"""
    ctr = 0
    while ind < len(word) :
        if word[ind] == letter :
            ctr += 1
        ind += 1
    print(ctr)


count('banana', 'a')
count_modified('banana', 'a', 2)
