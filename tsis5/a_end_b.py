import re
string=str(input())
x=re.search("a.*b$",string)
print(x)