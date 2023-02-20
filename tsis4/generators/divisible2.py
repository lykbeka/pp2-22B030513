class Gener:
    def __init__(self):
        self.N=int(input())
    def __iter__(self):
        self.a=0
        return self
    def __next__(self):
        if self.a>self.N:
            raise StopIteration
        else :
            if self.a%3==0 or self.a%4==0:
                x=self.a
                self.a+=1  
                return x 
            else:
                self.a+=1
that_class=Gener()
that_iter=iter(that_class)
l=[]
for x in that_iter:
    if x!=None:
        l.append(x)
print(l,sep=",")