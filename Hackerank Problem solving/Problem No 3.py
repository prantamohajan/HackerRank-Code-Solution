#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def findSubstring(s, k):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    max_vowels = 0
    current_vowels = 0
    best_start_idx = -1
    for i in range(k):
        if s[i] in vowels:
            current_vowels += 1
            
    max_vowels = current_vowels
    if max_vowels > 0:
        best_start_idx = 0
        
    for i in range(k, len(s)):
        if s[i] in vowels:
            current_vowels += 1
        if s[i - k] in vowels:
            current_vowels -= 1
        if current_vowels > max_vowels:
            max_vowels = current_vowels
            best_start_idx = i - k + 1
    if best_start_idx == -1:
        return "Not found!"
    else:
        return s[best_start_idx : best_start_idx + k]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    k = int(input().strip())

    result = findSubstring(s, k)

    fptr.write(result + '\n')

    fptr.close()