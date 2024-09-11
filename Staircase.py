#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    tt =n-1
    for w in range(1, n+1):
     print(" "*tt, end="")
     print("#"*w)
     tt -= 1

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
