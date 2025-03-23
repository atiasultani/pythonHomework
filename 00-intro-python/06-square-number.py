"""Problem Statement
Ask the user for a number and print its square (the product of the number times itself).
Here's a sample run of the program (user input is in bold italics):
Type a number to see its square: 4
4.0 squared is 16.0"""

# Starter Code

def main():
    BOLD = "\033[1m"
    ITALIC = "\033[3m"
    RESET = "\033[0m"  # Resets formatting

    print(" Square Of Number")

    num: float = float(input(f"Type a number to see its square:{BOLD}" ))
    print(f"{RESET}")
    print(f"{BOLD}{num}{RESET}" + " squared is " + f"{BOLD}{num ** 2}{RESET}")

if __name__ == '__main__':
    main()