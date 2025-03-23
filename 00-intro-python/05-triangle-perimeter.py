""" Problem Statement
Prompt the user to enter the lengths of each side of a triangle 
and then calculate and print the perimeter of the triangle
 (the sum of all of the side lengths).

Here's a sample run of the program (user input is in bold italics):

What is the length of side 1? 3

What is the length of side 2? 4

What is the length of side 3? 5.5

The perimeter of the triangle is 12.5
"""

#  Starter Code
def main():
    
    print("**** PERIMETER OF TRIANGLE *****")
    
    from rich.console import Console
    side1:float=float(input("What is the length of side 1?"))
    side2:float=float(input("What is the length of side 2?"))
    side3:float=float(input("What is the length of side 3?"))
    console=Console()
    print("\n")
    console.print(f"The length of side 1 = [bold]{side1}[/bold]")
    console.print(f"The length of side 2 = [bold]{side2}[/bold]")
    console.print(f"The length of side 3 = [bold]{side3}[/bold]")
    perimeter= side1+side2+side3
    console.print(f"The Perimeter of triangle is = [bold]{perimeter}[/bold]")

# Python file to call the main() function.
if __name__ == '__main__':
    main()
