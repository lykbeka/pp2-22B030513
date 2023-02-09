line=input()
strs=line.split()
list=[int(i) for i in strs] 
l=[]
def uniq(list):
    for i in list:
        if i not in l:
            l.append(i)
        else :
            continue
    return l
print(uniq(list))