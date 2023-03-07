string=input()
for i in range(0,round(len(string)/2)):
    if string[i]==string[len(string)-i-1]:
        continue
    else :
        print("Not palindrom")
        exit()
print("Palindrom")