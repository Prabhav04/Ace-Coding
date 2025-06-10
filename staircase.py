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
    for i in range(1, n+1):
        # Print spaces
        print(' ' * (n - i), end='')
        # Print hashes
        print('#' * i)

if __name__ == '__main__':
    n = int(input("enter num5").strip())

    staircase(n)