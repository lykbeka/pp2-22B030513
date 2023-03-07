nums=input().split()
l=list(float(i) for i in nums)
mult=1
for i in l:
    mult*=i
print(mult)