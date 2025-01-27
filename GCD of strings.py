from math import gcd
def gcdofstrings(str1,str2):
    if str1 + str2 !=str2 + str1:
        return ""
    gcd_length=gcd(len(str1),len(str2))
    
    return str1[:gcd_length]

str1="abcabc"
str2="abcabc"
print(gcdofstrings(str1,str2))
