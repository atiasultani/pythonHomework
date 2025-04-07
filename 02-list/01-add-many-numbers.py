# Problem Statement
# Write a function that takes a list of numbers and returns the sum of those numbers.

# Starter Code


def add_many_numbers(numbers)->int:
        a:int=0
        for number in numbers:
            a+=number
        return a

def main():

    print("Add Many Numbers ")
    numbers:list[int]=[1,2,3,4,5,6]
    print(numbers)
    sumOfNumber:int= add_many_numbers(numbers)
    print("Sum of number is :",sumOfNumber)
    
# Python file to call the main() function.
if __name__ == '__main__':
    main()


