from random import randint
num=int(randint(1,20))
guess=0
def game(num):
    pnum=int(input())
    
    if pnum>num:
        return 2
    elif pnum<num:
        return 0
    else:
        return 1
print("Hello! What is your name?")
name=str(input())
print("Well,",name,", I am thinking of a number between 1 and 20.",sep=(""))
print("Take a guess.")
while True:
    a=game(num)
    guess=guess+1
    if a>0:
        print("Your guess is too high.")
        print("Take a guess.")

    elif a<0:
        print("Your guess is too low.")
        print("Take a guess.")
    else:
        print("Good job, ",name,"! You guessed my number in ",guess," guesses!",sep=(""))
        break


