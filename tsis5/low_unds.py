import re
string=str(input())
x=re.search("([a-z]_)+[a-z]",string)
print(x)