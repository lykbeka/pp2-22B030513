import re
string=input()
x=re.search("([A-Z][a-z])+",string)
print(x)