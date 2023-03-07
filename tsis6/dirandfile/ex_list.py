import os
path=input("Please input path:")
if not os.path.exists(path):
    print("Incorrect path")
    exit()
l=[ name for name in os.listdir(path)]
print("List of directories and files:")
for x in l:  
    print(x)