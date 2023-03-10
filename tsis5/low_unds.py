import re
string=input()
x=re.search("([a-z]_)+[a-z]",string)
print(x)