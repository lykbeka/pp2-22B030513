import re
string=str(input())
x=re.findall("([a-z]_)+[a-z]",string)
print(x)