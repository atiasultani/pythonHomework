
def get_last_element(lst):
    print(lst[len(lst) - 1])

# The line below works too!!
# print(lst[-1]) 
# There is no need to edit code beyond this point
def get_lst():
     lst = [] 
     elem = input("Please enter an element of the list or press enter to stop. ") 
     while elem != "": 
        lst.append(elem) 
        elem = input("Please enter an element of the list or press enter to stop. ") 
        return lst

def main(): 
    lst = get_lst()
    get_last_element(lst)
if __name__ == '__main__':
    main()