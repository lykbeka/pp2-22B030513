class deacr:
    def __init__(self):
        self.a=int(input())
    def __iter__(self):
        self.i=self.a
        return self
    def __next__(self):
        if self.i<0:
            raise StopIteration
        else :
            x=self.i
            self.i-=1  
            return x 
that_class=deacr()
that_iter=iter(that_class)
for x in that_iter:
    print(x)