# Problem Statement
# Write a program which continuously asks the user to enter values which 
# are added one by one into a list. When the user presses 
# enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: 
# Here's the list: ['1', '2', '3']

# Starter Code
def main():
    print("GET LIst)")

    lst=[]
    value=input("Enter your value : ") #get individule value

    while value:
         lst.append(value) #add values in list 
         value = input("Enter a value: ")  # Get the next value to add

         print("Here's the list:", lst)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
