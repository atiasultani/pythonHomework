import time

def countdown(t):
    while t:
        min,sec=divmod(t,60)
        timer='{:02d}:{:02d}'.format(min,sec)
        print(timer,end='\n')
        time.sleep(1)
        t-=1
    print("Times Up !")


t=input("Enter time in seconds : ")
countdown(int(t))