vow=["a","e","i","o","u"]
vow2=["A","E","I","O","U"]
v=[]
s=("leetcode")
for i in s:
    if i in vow or i in vow2:
        v.append(i)
v.reverse()
print(v)
s1=list(s)
l=0
for i in range(0,len(s1)):
    if s1[i] in vow or s1[i] in vow2:
        s1[i]=v[l]
        l=l+1
r=''.join(s1)
print(r)