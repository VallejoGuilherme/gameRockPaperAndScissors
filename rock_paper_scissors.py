# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random

rock = 1
paper = 2
scissor = 3

you = input("Choose 1 = Rock, 2 = Paper, 3 = Scissor ")
adversary = random.randint(1, 3)
you = int(you)

if you == 1 and adversary == 2:
    print("You lost")
elif you == 1 and adversary == 3:
    print("You win")
elif you == 2 and adversary == 1:
    print("You win")
elif you == 2 and adversary == 3:
    print("You lost")
elif you == 3 and adversary == 1:
    print("You lost")
elif you == 3 and adversary == 2:
    print("You win")
else:
    print("Its a draw!")

if adversary == 1:
    adversary = "Rock"
elif adversary == 2:
    adversary = "Paper"
else:
    adversary = "Scissor"
print(f"Adversary choice is {adversary}")
