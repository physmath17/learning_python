def in_both(w1, w2) :
    """ prints the common letters between words w1 and w2 """
    for l in w1 :
        if l in w2 :
            print(l)


in_both('applea', 'banana')
