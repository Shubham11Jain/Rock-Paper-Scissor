import random

def rps():
    comp_choice = random.randint(1,3)
    if comp_choice==1:
        rock()
    elif comp_choice==2:
        paper()
    else:
        scissor()

def rock():
    user_choice = input("Type 1 for Rock, 2 for Paper, and 3 for Scissor: ")
    if user_choice=="1":
        print("Match TIED. You choose Rock and computer choose Rock.")
        try_again()
    elif user_choice=="2":
        print("YOU WIN. You choose Paper and computer choose Rock.")
        try_again()
    elif user_choice=="3":
        print("YOU LOSE. You choose Scissor and computer choose Rock.")
        try_again()
    else:
        print("Invalid Input")
        rock()

def paper():
    user_choice = input("Type 1 for Rock, 2 for Paper, and 3 for Scissor: ")
    if user_choice=="1":
        print("YOU LOSE. You choose Rock and computer choose Paper.")
        try_again()
    elif user_choice=="2":
        print("Match TIED. You choose Paper and computer choose Paper.")
        try_again()
    elif user_choice=="3":
        print("YOU WIN. You choose Scissor and computer choose Paper.")
        try_again()
    else:
        print("Invalid Input")
        paper()

def scissor():
    user_choice = input("Type 1 for Rock, 2 for Paper, and 3 for Scissor: ")
    if user_choice=="1":
        print("YOU WIN. You choose Rock and computer choose Scissor.")
        try_again()
    elif user_choice=="2":
        print("YOU LOSE. You choose Paper and computer choose Scissor.")
        try_again()
    elif user_choice=="3":
        print("Match TIED. You choose Scissor and computer choose Scissor.")
        try_again()
    else:
        print("Invalid Input")
        scissor()

def try_again():
    choice=input("Would you like to play again. Click y/n :")
    if choice=="y" or choice=="yes" or choice=="Y" or choice=="YES":
        rps()
    elif choice=="n" or choice=="no" or choice=="N" or choice=="NO":
        print("<<<--- THANKS FOR PLAYING --->>>")
        quit()
    else:
        try_again()

rps()