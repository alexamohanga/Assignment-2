from Interpreter import Interpreter
from sys import argv
import os


if __name__ == "__main__":
    argv.append("Alex")
    # Created by Jignesh
    if len(argv) == 2:
        interpreter = Interpreter(argv[1])
        interpreter.cmdloop()
    # Created by Suman
    elif len(argv) == 3:
        if os.path.isdir(argv[2]):
            interpreter = Interpreter(argv[1], argv[2])
            interpreter.cmdloop()
        else:
            print('Please provide\
            a valid path to a directory and try again!!!')

    # Created by Bikrant
    elif len(argv) == 4:
        if os.path.isdir(argv[2]):
            if os.path.isfile('./Database/' + argv[3] + '.db'):
                interpreter = Interpreter(argv[1], argv[2], argv[3])
                interpreter.cmdloop()
            else:
                print('Database ' + argv[3] + ' not found!!! Try again')
        else:
            print('Please provide \
            a valid path to a directory and try again!!!')
    else:
        print('Please use the command "python main.py your name"')
