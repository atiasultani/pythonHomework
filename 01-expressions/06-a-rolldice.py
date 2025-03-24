# Problem Statement
# Simulate rolling two dice, and prints results of each roll as well as the total.

# Starter Code
def main():
    print("Rolling Dice")

import random

# Number of sides on each die to roll
diceSides: int = 6

def main():
   
    # Roll die
    dice1: int = random.randint(1, diceSides)
    dice2: int = random.randint(1, diceSides)
    
    # Get their total
    total: int = dice1 + dice2
    
    # Print out the results
    print("Dice have", diceSides, "sides each.")
    print("First die:", dice1)
    print("Second die:", dice2)
    print("Total of two dice:", total)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

