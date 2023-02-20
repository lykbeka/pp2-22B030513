import math
class square:
    def __init__(self):
        self.a=int(input())
        self.b=int(input())
    def __iter__(self):
        self.i=self.a
        return self
    def __next__(self):
        if self.i>self.b:
            raise StopIteration
        else :
            x=math.pow(self.i,2)
            self.i+=1  
            return x 
that_class=square()
that_iter=iter(that_class)
for x in that_iter:
    print(x)