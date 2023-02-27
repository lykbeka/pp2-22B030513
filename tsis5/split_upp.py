import re
string=str(input())
x= re.findall('[A-Z][^A-Z]*', string)
print(" ".join(x))