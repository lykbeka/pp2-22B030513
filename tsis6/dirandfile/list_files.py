import os
path=input("Please input path:")
l=[ name for name in os.listdir(path)]
print("List of directories and files:")
for x in l:  
    print(x)