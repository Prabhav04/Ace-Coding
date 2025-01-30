input=["a","a","b","b","c","c","c"]
out=[]
cur=0
for i in range(0,len(input)):
    if cur!=input[i]:
        m=0
        cur=input[i]
        for j in input:
            if j == input[i]:
                m=m+1
        out.append(input[i])
        out.append(str(m))
if out[1]==str(1) and len(out)==2:
    print(out[0])
elif out[1]==str(1) and len(out)!=2:
    print(out[0],end="")
    for j in range(2,len(out)):
        print(out[j],end="")
else:
    print(out)

