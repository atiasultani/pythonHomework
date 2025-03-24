# Problem Statement
# Simulate rolling two dice, three times. Prints the results of each die roll.
# This program is used to show how variable scope works.

# Starter Code
import random
NUM_SIDES = 6

def rollDices():

    print("***** Dice-Simulator ******")
    print("\n")
    dice1:int =random.randint(1,NUM_SIDES)
    dice2:int =random.randint(1,NUM_SIDES)

    print(f"Dice 1 Number : {dice1}")
    print(f"Dice 2 Number : {dice2}")
    total:int = dice1 + dice2
    print(f"Total Number We Get  : {total}")

def main():
    print("\n\tGAME START")
    print("\n")
    die1:int = 3
    rollDices()
    print("\n")
    rollDices()
    print("\n")
    rollDices()
            
    print(f"\ndie1 in main() is: {die1}")
# Python file to call the main() function.
if __name__ == '__main__':
    main()

