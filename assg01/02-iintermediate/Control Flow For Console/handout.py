## Problem: High Low
 
# We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

# Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!

# You make a guess, saying your number is either higher than or lower than the computer's number

# If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!

# These steps make up one round of the game. The game is over after all rounds have been played.

# We've provided a sample run below. 


# Welcome to the High-Low Game!
# --------------------------------
# Round 1
# Your number is 8
# Do you think your number is higher or lower than the computer's?: lower
# You were right! The computer's number was 35
# Your score is now 1



# Round 2
# Your number is 88
# Do you think your number is higher or lower than the computer's?: higher
# Aww, that's incorrect. The computer's number was 100
# Your score is now 1

# Round 3
# Your number is 63
# Do you think your number is higher or lower than the computer's?: higher
# You were right! The computer's number was 5
# Your score is now 2

# Round 4
# Your number is 57
# Do you think your number is higher or lower than the computer's?: lower
# Aww, that's incorrect. The computer's number was 57
# Your score is now 2

# Round 5
# Your number is 22
# Do you think your number is higher or lower than the computer's?: lower
# Aww, that's incorrect. The computer's number was 1
# Your score is now 2

# Thanks for playing!

# Here are some milestones to guide you through the problem:

### Milestone #1: Generate the random numbers

# Generate the random numbers for you and the computer. For now, print both of them out to help you test the logic in later milestones.

# Welcome to the High-Low Game!
# --------------------------------
# The computer's number is 23
# Your number is 82


### Milestone #2: Get the user choice

# Get user input for their choice of whether they think their number is higher or lower than the computer's number.

# Welcome to the High-Low Game!
# --------------------------------
# The computer's number is 7
# Your number is 17
# Do you think your number is higher or lower than the computer's?: higher

# ### Milestone #3: Write the game logic

# Write code that maps out all the ways to win the round and prints out the results. When does the user win? How might we check for this? (Note: If you and the computer share the same number, the computer should win since your number wouldn't be higher nor lower.)

# Welcome to the High-Low Game!
# --------------------------------
# The computer's number is 79
# Your number is 3
# Do you think your number is higher or lower than the computer's?: lower
# # You were right! The computer's number was 79

### Milestone #4: Play multiple rounds

# Milestones 1-3 make up a single round of the game. Now that your game logic is sound, you can remove the line printing out the computer's number. Next, write code to play multiple rounds of the game! How many rounds should they play you ask? We've provided you with the NUM_ROUNDS constant. NUM_ROUNDS is the number of rounds you should have the user play. For reference, in the first example, we had NUM_ROUNDS = 3. After each round, add a blank line to separate the rounds visually. Make sure to print out the round number as well!


# Welcome to the High-Low Game!
# --------------------------------
# Round 1
# Your number is 22
# Do you think your number is higher or lower than the computer's?: lower
# You were right! The computer's number was 23

# Round 2
# Your number is 76
# Do you think your number is higher or lower than the computer's?: higher
# Aww, that's incorrect. The computer's number was 81

#  (more rounds are played)


### Milestone #5: Adding a points system

# Keep track of the player's score! You should print out the player's score after each round. After this step, you will have coded up the entire game!

#### Extension #1: Safeguard user input

# Get user input for their choice of whether they think their number is higher or lower than the computer's number.

# Welcome to the High-Low Game!
# --------------------------------
# Round 1
# Your number is 1
# Do you think your number is higher or lower than the computer's?: even
# Please enter either higher or lower: lower
# You were right! The computer's number was 6
# Your score is now 1


 # Simple Solution


# import random

# NUM_ROUNDS = 5

# def main():
#     print("Welcome to the High-Low Game!")
#     print('--------------------------------')

#     # Milestone 5: keep track of your score
#     your_score = 0

#     # Milestone 4: Play multiple rounds
#     for i in range(NUM_ROUNDS):
#         print("Round", i + 1)
#         # Milestone 1: Generate the random numbers and print them out
#         computer_num: int = random.randint(1, 100)
#         your_num: int = random.randint(1, 100)
#         print("Your number is", your_num)

#         # Milestone 2: Get user input for their choice
#         choice: str = input("Do you think your number is higher or lower than the computer's?: ")

#         # Milestone 3: Map out all the ways to win the round
#         higher_and_correct: bool = choice == "higher" and your_num > computer_num
#         lower_and_correct: bool = choice == "lower" and your_num < computer_num

#         if higher_and_correct or lower_and_correct:
#             print("You were right! The computer's number was", computer_num)
#             # Milestone 5: keep track of your score
#             your_score += 1 
#         else: 
#             print("Aww, that's incorrect. The computer's number was", computer_num)

#         # Milestone 5: keep track of your score
#         print("Your score is now", your_score)
#         print()

#     print("Thanks for playing!")

# if __name__ == "__main__":
#     main()

#### Extension #2: Conditional ending messages

# Add conditional messages at the end which gauge players on how they performed! For ours, we evaluated the player and gave them separate messages if:

# they had a perfect game


# Your score is now 5

# Wow! You played perfectly!

# they won at least half the rounds (rounded down)

# Your score is now 2

# Good job, you played really well!

# they won less than half the rounds

# Your score is now 1

# Better luck next time!

### Solution (with extensions):


import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')

    # Milestone 5: keep track of your score
    your_score = 0

    # Milestone 4: Play multiple rounds
    for i in range(NUM_ROUNDS):
        print("Round", i + 1)
        # Milestone 1: Generate the random numbers and print them out
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        print("Your number is", your_num)

        # Milestone 2: Get user input for their choice
        choice = input("Do you think your number is higher or lower than the computer's?: ")

        # Extension 1: Make sure the player inputs a valid choice (higher or lower)
        while choice != "higher" and choice != "lower":
            choice = input("Please enter either higher or lower: ")

        # Milestone 3: Map out all the ways to win the round
        higher_and_correct = choice == "higher" and your_num > computer_num
        lower_and_correct = choice == "lower" and your_num < computer_num

        if higher_and_correct or lower_and_correct:
            print("You were right! The computer's number was", computer_num)
            # Milestone 5: keep track of your score
            your_score += 1 
        else: 
            print("Aww, that's incorrect. The computer's number was", computer_num)

        # Milestone 5: keep track of your score
        print("Your score is now", your_score)
        print()
    
    # Extension 2: Conditional ending messages based on performance
    print("Your final score is", your_score)

    if your_score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif your_score > NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
