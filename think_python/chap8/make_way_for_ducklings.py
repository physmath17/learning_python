prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes :

    print(letter + 'u'*(letter == 'O' or letter == 'Q') + suffix)
