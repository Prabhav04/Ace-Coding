#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if s.endswith("AM"):
        h,m,se=s.split(":")
        if int(h)==12:
            h="00"
    elif s.endswith("PM"):
        h,m,se=s.split(":")
        if int(h)!=12:
            h=str(int(h)+12)
    se=se.rstrip(" AM").rstrip(" PM")
    res=h+":"+m+":"+se
    return res
if __name__ == '__main__':

    s = input("Enter Time in 12 Hour Format: ")

    result = timeConversion(s)
    print(result)