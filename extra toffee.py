extra_toffee=4
childarr=[1,6,3,2,5,3,1]
boolarr=[True]*len(childarr)
j=0
a=max(childarr)
for i in childarr:
    if a>(i+extra_toffee):
        boolarr[j]=False
        j=j+1
    elif a<=(i+extra_toffee):
        boolarr[j]=True
        j=j+1
    
print(boolarr)