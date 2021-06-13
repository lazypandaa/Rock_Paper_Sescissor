# Rock Paper Scissor game

import random
a = ["rock","paper","scissor"]
"""
rock vs paper : paper
rock vs scissor : rock
paper vs scissor : scissor
"""
# iv = 0  at first I got an error so i add this variable
tie = 0
no = 0
n = 10
print("\n \t \t Game starts now:\n")
while(n>0):
    n = n-1
    # print(n)
    c = random.choice(a)
    i = input("Select: rock, paper or scissor\nYou choose: ").lower()
    # print(a)
    if i == c: 
        print("Tie\n")
        tie = tie + 1
    elif i == "paper" and c =="rock":
        print("You won\n")
        no = no +1
    elif i == "rock" and c == "scissor":
        print("You won\n")
        no = no +1
    elif i == "scissor" and c == "paper":
        print("You Won\n")
        no = no +1

    elif c =="paper"and i == "rock":
        print("Opponent wins\n")
    elif c =="scissor"and i == "paper": 
        print("Opponent wins\n")
    elif c =="rock"and i == "scissor" :
        print("Opponent wins\n")
    else:
        print("Enter valied input")
        # iv = iv + 1 at first I got an error so i add this variable
o = 10 - no - tie
print("Game Over")    
print(f"No of mathches you won : {no}\nNo of Tie brakes : {tie}\nNo of mathches opponent wins : {o}")
