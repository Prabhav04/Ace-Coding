m,n=map(int,input("Enter the numbers").split())
outarr = []


keypad = {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']
}



def lettercomb(m, n):
    for i in keypad[m]:
        for j in keypad[n]:
            outarr.append(i + j)
    return outarr

print(lettercomb(m, n))
# print(keypad[m])
