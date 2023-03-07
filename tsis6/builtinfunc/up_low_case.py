string=input()
up=0
low=0
for i in string:
    if ord(i) in range(ord("A"),ord("Z")+1):
        up+=1
    elif ord(i) in range(ord("a"),ord("z")+1):
        low+=1
print("Lower case=",low)
print("Upper case=",up)