# Problem Statement
# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

# Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

# What's your favorite animal? cow

# My favorite animal is also cow!

# Starter Code

def main():
    print("\n")
    print("**** AGREEMENT BOT **** \n")
    # ANSI escape codes for formatting
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"  # Resets formatting

    # Get user input
    favorite_animal = input("What's your favorite animal? ")
    print("\n")
    # Print formatted output
    print(f"My favorite animal is  {BOLD}{favorite_animal}{RESET}!\n")   # Bold
    print(f"My favorite animal is  {ITALIC}{favorite_animal}{RESET}!\n")  # Italic
    print(f"My favorite animal is  {UNDERLINE}{favorite_animal}{RESET}!\n")  # Underline
    
    print("**** Second Method for use rich.console Library to bold,italic or underline text****** \n")
    # to install library run pip install rich in cmd
    from rich.console import Console

    console=Console()
    animal:str = input("Enter Your Favourit Animal: ")
    console.print(f"My favorite animal is also [bold]{animal} [/bold]! \n")   # Bold here are [bold] is open tag and [/bold] is closing tag
    console.print(f"My favorite animal is also [italic]{animal}[/italic]! \n")  # Italic
    console.print(f"My favorite animal is also [underline]{animal}[/underline]! \n")  # Underline
 




# Python file to call the main() function.
if __name__ == '__main__':
    main()