# def find_branchless(word, letter) :
#     index = 0
#     while index < len(word) :
#         return index*(word[index] == letter)
#         index = index + 1
#     return -1

def find(word, letter) :
    """ takes a character letter and finds the index in word where that character appears """
    index = 0
    while index < len(word) :
        if word[index] == letter :
            return index
        index = index + 1
    return -1

def find_modified(word, letter, index) :
    """ takes a character letter and finds the index in word where that character appears starting at index """
    while index < len(word) :
        if word[index] == letter :
            return index
        index = index + 1
    return -1

# print(find_branchless('hello', 'l'))
print(find('hello', 'l'))
print(find_modified('hello', 'l', 3))

