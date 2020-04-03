import random
import sys
import time

x = 0
y = 0

print("Rock") #1
print("Paper") #2
print("Scissors") #3

while True:
    choice = True
    while choice:
        player = input(("What is your choice?: "))
        if player == "rock" or player == "Rock":
            player = 1
            choice = False
            break
        if player == "paper" or player == "Paper":
            player = 2
            choice = False
            break
        if player == "scissors" or player == "scissors":
            player = 3
            choice = False
            break
        else:
            choice = True

    choose = True
    while choose:
        computer = random.randint(0,4)
        if computer == 1:
            computerchoice = "rock"
            choose = False
            break
        if computer == 2:
            computerchoice = "paper"
            choose = False
            break
        if computer == 3:
            computerchoice = "scissors"
            choose = False
            break

    print("Computer picks " + computerchoice)

    if (player == 2 and computer == 1):
        print("Winner: Player")
        x += 1
    if (player == 3 and computer == 2):
        print("Winner: Player")
        x += 1
    if (player == 1 and computer == 3):
        print("Winner: Player")
        x+=1
    if (player == 1 and computer == 2):
        print("Winner: Computer")
        y += 1
    if (player == 2 and computer == 3):
        print("Winner: Computer")
        y += 1
    if (player == 3 and computer == 1):
        print("Winner: Computer")
        y += 1
    if (player == computer):
        print("Tie")

    string = ' .'
    for letter in string:
        sys.stdout.write(letter + "\n")
        time.sleep(1)
    print("Player: " + str(x) + "\nComputer: " + str(y))
    for letter in string:
        sys.stdout.write(letter + "\n")
        time.sleep(1)