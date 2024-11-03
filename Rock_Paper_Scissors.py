import random

print("WELCOME to Rock Paper Scissors GAME\nEnter one of the options:\nRock \nPaper \nScissors ")

def new_choice():
    user = input()
    print("your choice is: " + user)
    return user

def comp_choice():
    choice = ["Rock", "Paper", "Scissors"]
    com_choice = random.randint(0, 2)
    com_choice = choice[com_choice]
    print("computer choice is: " + com_choice)
    return com_choice

user_choice = new_choice()
com_choice = comp_choice()
while com_choice == user_choice:
    user_choice = new_choice()
    com_choice = comp_choice()

if "Rock" in user_choice and "Paper" in com_choice:
    print("Computer Paper win!")
elif "Rock" in user_choice and "Scissors" is com_choice:
    print("your Rock win!")
elif "Paper" in user_choice and "Scissors" is com_choice:
    print("Computer Scissors win!")
elif "Paper" in user_choice and "Rock" is com_choice:
    print("your Paper win!")
elif "Scissors" in user_choice and "Rock" is com_choice:
    print("Computer Rock win!")
else:
    print("your Scissors win!")
