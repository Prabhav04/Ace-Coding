a=[1,12,-5,-6,50,3]
k=4
l=0
for i in range(len(a)-k):
    sum=0
    for j in range(0,k):
        sum=sum+a[j+i]
    if sum>l:
        l=sum

print(l)
print(l/k)
