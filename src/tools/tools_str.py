"""
This module contains code for handling or manipulating strings.

"""
import random


#Generates a string  with random characters from one already supplied and with the specified length.
def rannewstr(str_length:int,characters:str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890%$#@'):
    le:int = len(characters)
    new_str:str = ''
    ctr:chr = ''
    i:int = 0

    while(i < str_length):
        i = i + 1
        ctr = characters[random.randint(0,le - 1)]
        new_str += ctr
        
    return new_str