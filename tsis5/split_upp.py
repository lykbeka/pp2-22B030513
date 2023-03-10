import re
string=input()
x= re.findall('[A-Z][^A-Z]*', string)
print(" ".join(x))