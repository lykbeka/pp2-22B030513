string=str(input())
list=[char for char in string]
def palindrome(list):
    for i in range(0,int(len(list)/2)):
        if list[i]==list[int(len(list)-1-i)]:
            if i==int(len(list)/2-1):
                return "Palindrome"
            continue
        else :
            return "Not palindrome"
print(palindrome(list))