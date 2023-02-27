import re
string=str(input())
x=re.split("[_]",string)
l=[]
for i in x:
    i=i[0].upper()+i[1:]
    l.append(i)
print("".join(l))