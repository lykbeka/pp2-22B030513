line=input()
def reverse(line): 
    words=line.split()
    words_l=[str(i) for i in words]
    words_l.reverse()
    print(*words_l)
reverse(line)