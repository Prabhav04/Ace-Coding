a="abcdef"
b="pq"
c=""
n=len(a)
m=len(b)
i=0
l=max(len(a),len(b))
while i<l:
    if len(a)==len(b):
        c=c+a[i]
        c=c+b[i]
        i+=1
    elif len(a)>len(b):
        while i<len(b):
            c=c+a[i]
            c=c+b[i]
            i+=1
        c=c+a[i]
        i=i+1
    elif len(a)<len(b):
        while i<len(a):
            c=c+a[i]
            c=c+b[i]
            i+=1
        c=c+b[i]
        i=i+1            

print(c)  

