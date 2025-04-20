#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos = 0
    neg = 0
    zer = 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        elif i == 0:
            zer += 1
    a = float(pos / len(arr))
    b = float(neg / len(arr))
    c = float(zer / len(arr))
    return a, b, c


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    a, b, c = plusMinus(arr)
    print(f"{a:.6f}")
    print(f"{b:.6f}")
    print(f"{c:.6f}")
