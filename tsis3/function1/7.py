line=input()
strs=line.split()
numb=[int(i) for i in strs]
def has_33(numb):
    for i in range(0,len(numb)):
        if numb[i]==3 and numb[i+1]==3:
            return True
        else:
            continue
        if i==len(numb)-1:
            return False
print(has_33(numb))