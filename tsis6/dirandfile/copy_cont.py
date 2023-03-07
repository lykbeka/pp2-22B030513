import os
file1=input("Input file name or path that will be copied:")
file2=input("Input file name or path that will be appended:")
if not os.path.exists(file1) or not os.path.exists(file2):
    print("Incorrect paths or file names")
    exit()
op=open(file1)
op2=open(file2,"a")
try:
    op2.write(op.read())
finally:
    op.close()
    op2.close()