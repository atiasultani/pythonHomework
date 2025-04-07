# Problem Statement
# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

# Starter Code

def get_last_element(lst):
    # Takes the length of the list and minuses 1 since they are zero-indexed 
    # (we start counting at 0)
    print(lst[len(lst)-1])


def get_list():
    lst=[]
    element=input("Enter list elements and press enter to stop : ")
    while lst!="":
        lst.append(element)
        element=input("Enter list elements and press enter to stop : ")
        return lst

def main():
    lst = get_list() 
    print(lst)
    get_last_element(lst)


if __name__ == '__main__':
    main()
