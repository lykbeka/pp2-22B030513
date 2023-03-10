import re
string=input()
x=re.search("ab{2,3}",string)
print(x)