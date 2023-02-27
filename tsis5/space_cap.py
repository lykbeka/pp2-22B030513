import re
string=str(input())
print(re.sub(r"(\w)([A-Z])", r"\1 \2", string))