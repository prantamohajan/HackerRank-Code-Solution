#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'decryptPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def decryptPassword(s):
    s = list(s)
    res = []
    numbers = []
    i = 0

    while i < len(s) and s[i].isdigit() and s[i] != '0':
        numbers.append(s[i])
        i += 1
        
    while i < len(s):
        if s[i] == '0':
            res.append(numbers.pop())
            i += 1
        elif i + 2 < len(s) and s[i+2] == '*':
            res.append(s[i+1])
            res.append(s[i])
            i += 3 
        else:
            res.append(s[i])
            i += 1
            
    return "".join(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = decryptPassword(s)

    fptr.write(result + '\n')

    fptr.close()