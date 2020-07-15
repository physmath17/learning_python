import math

def eval_loop() :
    """ iteratively prompts the user, takes the resulting input and evaluates it using eval, and prints the result until the user enters 'done' """
    while True :
        inp = input('> ')
        if inp == 'done' :
            break
        print(eval(inp))

    print('DONE!')

eval_loop()
