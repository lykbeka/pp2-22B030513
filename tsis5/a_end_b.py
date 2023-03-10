import re
string=input()
x=re.search("a.*b$",string)
print(x)