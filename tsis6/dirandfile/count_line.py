import os
txt=input("File name or path:")
if not os.path.exists(txt):
    print("Incorrect name or path:")
    exit()
cont=open(txt)
print("Lines:",sum(1 for line in cont))