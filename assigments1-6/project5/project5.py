# HangMan
import random

# Word list for the game
words = ["python", "hangman", "kylie", "developer", "tutorial", "keyboard", "function"]

def get_valid_word(word_list):
    word = random.choice(word_list)
    while '-' in word or ' ' in word:
        word = random.choice(word_list)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # Letters in the word
    alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    used_letters = set()  # What the user has guessed

    lives = 6

    # Game loop
    while len(word_letters) > 0 and lives > 0:
        # Show current progress
        print(f"\nYou have {lives} lives left. Used letters: {' '.join(sorted(used_letters))}")
        
        # Show word with blanks
        word_display = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", ' '.join(word_display))

        # Get user guess
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Correct!")
            else:
                lives -= 1
                print("Incorrect!")
        elif user_letter in used_letters:
            print("You already guessed that letter.")
        else:
            print("Invalid character. Please enter a letter.")

    # End of game
    if lives == 0:
        print(f"\nYou died! The word was {word}")
    else:
        print(f"\nCongratulations! You guessed the word: {word}")

if __name__ == '__main__':
    hangman()
    