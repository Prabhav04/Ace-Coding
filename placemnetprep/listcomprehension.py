nums=[12,3,4,5,6,7,8,9,10,11]
evennums=[num for num in nums if num%2==0]
print(evennums)
nums2=[12,3,4,5,6,7,8,9,10,11]
squared=[num**2 for num in nums2]
print(squared)
sentence="This is a sample sentence"
filtered=''.join(char for char in sentence if char.lower() not in 'aeiou')
print(filtered)
word="sucessforeveryone"
char_count={char: sentence.count(char) for char in word}
print(char_count)
revsentence=" ".join([word[::-1] for word in sentence.split()])
print(revsentence)
def isprime(n):
    return n>1 and all(n%i!=0 for i in range(2,int(n**0.5)+1))
primes=[num for num in range(101) if isprime(num)]
print(primes)


def fib(n):
    a,b=0,1
    while(a>n):
        yield a
        a,b=b,a+b
    return b
fibonacci=[num for num in fib(100)]
print(fibonacci)




