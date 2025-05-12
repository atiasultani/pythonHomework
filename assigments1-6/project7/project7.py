# Password Generator
import random
print(" Wellcom To Your Strong Password Generator ")
print(" ----------------------------------------- ")
chr="hello_world%python123456789."
number=(int(input("Enter a Number How Many Password You Wants : ")))
length=(int(input("Enter a Number for Password Length : ")))
print("\n___________________________________________")
print(" Here Are Your's Password : ")
for psw in range(number):
    passwords=''
    for characters in range(length):
        passwords+=random.choice(chr)
    print(passwords)