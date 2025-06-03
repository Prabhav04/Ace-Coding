m, n = map(int, input().split())

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def mthprime(m, n):
    count = 0
    num = 2
    while count < m:
        if prime(num):
            count += 1
            if count == m:
                return num
        num += 1
    return -1

def digisum(number):
    while number >= 10:
        total = 0
        temp = number
        while temp > 0:
            total += temp % 10
            temp //= 10
        number = total
    return number

mp = mthprime(m, n)
if mp != -1:
    result = digisum(mp)
    print(result)
else:
    print("No prime found")