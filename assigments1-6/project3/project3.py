# Guess the Number Game Python Project (user)
import random

def guess(user):
    user=0
    comp=random.randint(1,10)
   
    while user != comp:
        
        user=int(input(f"Enter 1 to {user} number : " ))
        
        if comp > user:
           print(f"computer you are guess high number try again : {comp}")
        
        elif comp < user:
            print(f"computer you are guess low number try again :{comp} ")
        
        print(f"Computer guess right number user no is : {user}")
    
def main():
        a=guess(10)
        print(a)
if __name__ == '__main__' :
        main()


