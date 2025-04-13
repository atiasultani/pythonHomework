import random

def main():
    flg = ("israel", "u.s.a", "india")
    
    # Randomly choose a target
    rand_choice = random.choice(flg)
    print(f"Target acquired: {rand_choice}")
    
    def shoot(target):
        try:
            if target == "israel" or "india" or "u.s.a":
                print("Shoot!")
            else:
                print("Don't shoot!")
        except Exception as e:
            print(f"Error during targeting: {e}")
        finally:
            print("Game over. We win.")
    
    shoot(rand_choice)

if __name__ == '__main__':
    main()
