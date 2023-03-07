line=input().split()
t=tuple(int(i) for i in line)
if all( t ):
    print("true")
else :
    print("false")