# Mad-Libs

def main():
    print(" MAD LABS PYTHON PROJECT ")
adjective=input("Enter Adjective : ")
noun=input("Enter Noun : ")
verb=input("Enter Verb : ")
animal=input("Enter Animal : ")
place=input("Enter Place : ")
adverb=input("Enter Adverb : ")
food=input("Enter Food : ")
exclamation=input("Enter Exclamatiom ! : ")
mad_labs:str=f"\n Under a {adjective} sky, the {noun} suddenly {verb}ed {adverb}, tripping over a {adjective} {animal} while racing toward {place}.\n Chaos erupted, scattering {food} everywhere—until a {noun} shouted, '{exclamation}!'"

print(mad_labs)
if "__name__"=="__main__" :
     main()