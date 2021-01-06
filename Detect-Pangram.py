'''
Created on Dec 3, 2020

@author: Salzaidy
'''

import string

def is_pangram(s):
    
    allLetters = string.ascii_lowercase
    
    for letter in allLetters:
        if letter not in s.lower():
            return False
    return True
    



pangram = "The quick, brown fox jumps over the lazy dog!"
s = is_pangram(pangram)
print(s)