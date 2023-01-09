import random
import time
def guessgame():
    print("This is a guess game where you have to guess a number between 1 and 100")
    print("You have 6 CHANCES")
    print()
    print()
    n=random.randint(1,100)
    ctr=0
    while ctr<6:
        g=int(input("Enter a number between 1 and 100:-"))
        if g==n:
            print()
            print("YOU WIN!!!!!!!!!!!!!!")
            time.sleep(0.3)
            print("$$$$$$$$$$$$$$$$$$$$$_____WONDERFULL_____$$$$$$$$$$$$$$$$$$$$$$")
            time.sleep(0.3)
            print("You won with",5-ctr,"chance(s) to spare")
            time.sleep(0.3)
            break
        else:
            if g>n:
                print("The required number is LESS than",g)
                ctr+=1
            else:
                print("The required number is MORE than",g)
                ctr+=1
            print("You have",6-ctr,"more chance")
            print()
    if not ctr<6:
        print()
        print("Better luck next time...")
        time.sleep(0.3)
        print("YOU LOST")
        time.sleep(0.3)
        print()
        print("The orginal number was",n)

            
