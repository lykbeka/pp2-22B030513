import os
path=input("Input path:")
if not os.path.exists(path):
    print("Path does not exist")
    exit()
os.remove(path)
print("File was removed")