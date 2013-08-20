'''
yapgwgen.py - yet another password generator
by Matthias Sieber

Copyright 2013 Matthias Sieber

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
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