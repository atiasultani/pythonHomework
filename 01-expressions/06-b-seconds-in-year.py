# Problem Statement
# Use Python to calculate the number of seconds in a year, and 
# tell the user what the result is in a nice print statement 
# that looks like this (of course the value 5 should be 
# the calculated number instead):

# There are 5 seconds in a year!

# You should use constants for this exercise -- there 
# are 365 days in a year, 24 hours in a day,
# 60 minutes in an hour, and 60 seconds per minute.

# Starter Code
daysInYear=365
hourInDay=24
minInHour=60
secInMin=60
def main():

    print("\n**How Many Seconds in a Year**")
    print(f"\nthere are {daysInYear} days in a year,\n{hourInDay} hours in a day,",
    f"\n{minInHour} minutes in an hour,", f"\nand {secInMin} seconds per minute.")
    secInYear=daysInYear*hourInDay*minInHour*secInMin
    print(f"\nSo There are {secInYear} seconds in a year!\n")
# Python file to call the main() function.
if __name__ == '__main__':
    main()