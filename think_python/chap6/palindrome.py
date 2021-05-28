def first(word) :
    return word[0]

def last(word) :
    return word[-1]

def middle(word) :
    return word[1:-1]

def is_palindrome(word) :
    """ returns True if word is a paindrome """
    if len(word) <= 1 :
        return True

    if first(word) != last(word) :
            return False
    
    return is_palindrome(middle(word))


if __name__ == "__main__" :
    w = input("Enter the word you want to check : ")
    print(is_palindrome(w))
