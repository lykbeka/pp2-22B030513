line=input()
numbers=line.split()
numbers_list=[int(i) for i in numbers] 
def filter_prime(numbers_list):
    pr_list=[]
    for k in numbers_list:
        a = 0
        if(k == 2):
            pr_list.append(k)
            continue
        elif(k == 1):
            continue
        for j in range(2, k):
            if(k % j == 0):
                a += 1
        if(a == 0):
            pr_list.append(k)
    print(pr_list) 
filter_prime(numbers_list)