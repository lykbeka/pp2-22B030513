import re
string=str(input())
x=re.search("ab{2,3}",string)
print(x)