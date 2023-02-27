import re
string=str(input())
print(re.sub("[ .,]",":",string))