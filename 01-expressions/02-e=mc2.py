# Problem Statement 
# Write a program that continually reads in mass from 
# the user and then outputs the equivalent energy using 
# Einstein's mass-energy equivalence formula 
# (E stands for energy, m stands for mass, and C is the speed of light:
# E = m * c**2
# Almost 100 years ago, Albert Einstein famously discovered that 
# mass and energy are interchangeable and are related by the above equation. 
# You should ask the user for mass (m) in kilograms and 
# use a constant value for the speed of light -- C = 299792458 m/s.

# Here's a sample run of the program (user input is in bold italics):

# Enter kilos of mass: 100

# e = m * C^2...

# m = 100.0 kg

# C = 299792458 m/s

# 8.987551787368176e+18 joules of energy!

# Starter Code


def main():

    print("** Einstein's mass-energy equivalence formula **")

BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"  # Resets formatting

m:float=float(input(f"Enter Kilos Mass:{BOLD}")) # mass in kilos
print(f"{RESET}")
c:float = 299792458 
print(f"{c} m/s") #speed of light
e = m*c**2          #formula of mass energy equivalence
print(f"{e} joules of energy!") #result

# Python file to call the main() function.
if __name__ == '__main__':
    main()
