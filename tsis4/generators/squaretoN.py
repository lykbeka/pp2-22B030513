class Gener:
    def __init__(self):
        self.N=int(input())
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a>self.N:
            raise StopIteration
        else :
            x=pow(self.a,2)
            self.a+=1
            return x
that_class=Gener()
that_iter=iter(that_class)
for x in that_iter:
    print(x)