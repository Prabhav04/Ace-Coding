a=[1,0,9,0,4,0,6,8,9,10,323,0,22,6,2,0,2,5,2]

for i in range(0,len(a)-1):
    for j in range(0,len(a)-i-1):
        if a[j]==0:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)

