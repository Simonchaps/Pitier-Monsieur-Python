from Dictionnaire import *
from random import *

def random_Sujet():
    return Sujet[randint(0, 3)]
 
def random_Verbe():
    return Verbe[randint(0, 4)]

def random_Complement():
    return Complement[randint(0, 8)]

