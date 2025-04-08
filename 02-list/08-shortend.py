MAX_LENGTH:int=3
def shortend(lst):
    while len(lst)>MAX_LENGTH:
        last_elemt=lst.pop()
        print(last_elemt)

def get_lst():
    lst=[]
    element=input("enter your items of list")
    while element != "" :
        lst.append(element)
        element=input("Enter you value")
        return lst


def main():
    print("Shortend ")
    
    lst=get_lst()
    ans=shortend(lst)
    print(ans)
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()