numheads=int(35)
numlegs=int(94)
def solve(numheads, numlegs):
    x=(4*numheads-numlegs)/2
    print("Rabbits=",x," Chickens=",numheads-x)
solve(numheads,numlegs)