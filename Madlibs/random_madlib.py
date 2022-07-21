# A madlib is like using string concatnation and replace in a paragraph with the help of user input. Like fill in the blanks. Lets create some random madlibs and then call them 

import random
from random_madlibs import Apocalypse_madlib, Spy_madlib

if __name__ == "__main__":
    m = random.choice([Spy_madlib,Apocalypse_madlib])
    m.madlib()


