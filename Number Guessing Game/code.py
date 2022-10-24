import time
import random
print("\n\n        ~~~~~Welcome to Guess the Number Game~~~~~\n")
print("I am Jarvis and I will be managing the game.")
time.sleep(1)
print("Please Enter you Name :")
name = input()
time.sleep(1)
print(f"\n\nSo, {name} let me tell you the rules first:\n")
time.sleep(1)
print("\n1) When the game start I will choose a number from 1 to 100 both inclusive.")
time.sleep(1)
print("\n2) You will have 6 chances to guess that nummber. ")
time.sleep(1)
print("\n3.Also you will be given 4 hints which you can use after every guess.\n")
time.sleep(0)
print(f"{name} are you ready to play ?\n 1. Yes\n 2. No")
time.sleep(1)
print("Enter your choice number :")
check = int(input())
y=6
z=4
x=1
flag = True
if check==1:
    time.sleep(2)
    print("\n\nI have choosen a number:")
    n = random.randrange(1,100)
    while y>0 and flag==True:
        guess = int(input(f"\nEnter your Guess number {x} :\n"))
        y=y-1
        x=x+1
        if guess!=n:
            time.sleep(1)
            print("Wrong Choice\n")
            time.sleep(1)
            if z>0:    
                print(f"You have {z} Hints left")
                print("Do you want to use it")
                print("Press: \n 1.Yes\n 2.No")
                tt = int(input())
                if tt==1:
                    if guess < n:
                        time.sleep(2)
                        print(f"\nYour Choice was : {guess}")
                        if n-guess>=50:
                            print("So,Your Choosen number is very low")
                        elif n-guess>=20:
                            print("So,Your Choosen number is a bit low")
                        else:
                            print("So,Your Choose number is lower than mine and also you are very close to my number")
                    if guess > n:
                        time.sleep(2)
                        print(f"Your Choice was : {guess}")
                        if guess-n>=50:
                            print("So,Your Choosen number is very High")
                        elif guess-n>=20:
                            print("So,Your Choosen number is a bit high")
                        else:
                            print("So,Your Choose number is Higher than mine and also you are very close to my number")
                    z=z-1
                else:
                    print("Okay, Let's Continue ")
            else:
                print("You have used all your Hints")
        else:
            time.sleep(2)
            print(f"Congratulation {name}!!\nYou Won the Game.\n\n")
            flag=False        
else:
    time.sleep(2)
    print(f"\nAs You wish, \nGoodBye {name}\n")
    flag=False

