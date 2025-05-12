# Guess the Number Game Python Project (computer)
import random


def guess(x):
        random_no=random.randint(1,x)
        guess=0
        while guess != random_no:
            guess=int(input(f"Pass guessing rang between 1 to {x} : "))
            if guess < random_no:
                print ("Sorry Pass Again.You Too Low ")
            elif guess > random_no:
                print ("Sorry pass Again. You Too High")
        
        print(f"You Win You Guess The Correct No {random_no}")
    
def main():
        a=guess(10)
        print(a)
if __name__ == '__main__':
        main()