import re
string=str(input())
x=re.search("([A-Z][a-z])+",string)
print(x)