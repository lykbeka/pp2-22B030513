import os
file=input("Input file name or path:")
if not os.path.exists(file):
    print("Incorrect path or name")
    exit()
openf=open(file,"r")
print(openf.read())
openf.close()
opena=open(file,"a")
try :
    print("List to file:")
    opena.write(input())
finally:
    opena.close()