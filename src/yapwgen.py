'''
yapgwgen.py - yet another password generator
by Matthias Sieber
'''

import random
import string

def generateRandomPassword(minlength=8, maxlength=12, digits=True):
    '''generates a random password'''
    pw = ''
    length = random.randrange(minlength, maxlength+1)
    for i in range(0, length):
        if digits == True:
            num = random.choice([0, 1])
            if num == 1:
                pw += str(random.randint(0, 9))
            else:
                pw += random.choice(string.ascii_letters)
        else:
            pw += random.choice(string.ascii_letters)
    return pw

if __name__ == "__main__":
    print(generateRandomPassword())