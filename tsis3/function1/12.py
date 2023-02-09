line=input()
strs=line.split()
list=[int(i) for i in strs]
def histogram(list):
    for i in list: 
        a=0 
        l=[]
        while i>=a:
            l.append("*")
            a+=1
            if i==a:
                print(*l,sep=(""))
histogram(list)