# Problem Statement
# Write a program that doubles each element in a list of numbers. 
# For example, if you start with this list:
# numbers = [1, 2, 3, 4]
# You should end with this list:
# numbers = [2, 4, 6, 8]

# Starter Code
def main():
    print("Make Digit Double in List")
    numberList:list[int]=[1,2,3,4]
    print("List of numbers \n",numberList)
    for i in range(len(numberList)):        #use for loop to make digits double
        indexElement=numberList[i]
        numberList[i]=indexElement*2
    
    print("Make its double \n",numberList)
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
