import re
string=str(input())
x=re.findall('[A-Z][^A-Z]*', string)
l=[]
for i in x:
    i=i[0].lower()+i[1:]
    l.append(i)
print("_".join(l))