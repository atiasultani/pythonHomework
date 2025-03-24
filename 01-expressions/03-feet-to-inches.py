# Problem Statement
# Converts feet to inches. 
# Feet is an American unit of measurement. 
# There are 12 inches per foot. 
# Foot is the singular, and feet is the plural.

# Starter Code
inchesInFoot:int=12
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"  # Resets formatting

def main():

    print("\tConverts feet to inches")
    print("\t***********************")
    feet: float = float(input("\n \tEnter number of feet: "))  
    inches: float = feet * inchesInFoot  # formula to convert feet into inches
    print("\tThat is", f"{BOLD}{inches}{RESET}", "inches!")


# Python file to call the main() function.
if __name__ == '__main__':
    main()
