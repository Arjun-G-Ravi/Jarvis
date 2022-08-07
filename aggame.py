import random
import time
from speech import *
def guessgame():
    write("""This is a guess game where I will think of a  number between 1 and 100
                                  and you will have to guess that in 6 chances.""")
    print()
    flag=0
   
    n=random.randint(1,100)
    ctr=0
    while ctr<=5:
        speak("Now make a guess")
        g=int(input("Enter a number between 1 and 100:-"))
        if g==n:
            print()
            time.sleep(2)
            print("YOU WIN!!!!!!!!!!!!!!")
            time.sleep(0.3)
            print("$$$$$$$$$$$$$$$$$$$$$_____WONDERFULL_____$$$$$$$$$$$$$$$$$$$$$$")
            time.sleep(0.3)
            word4="You won with "+str(5-ctr) +" chance to spare"
            write(word4)
            time.sleep(.6)
            flag=1
            break
        else:
            if ctr!=5:
                if g>n:
                    word="No, my number is LESS than "+str(g)
                    write(word)
                    ctr+=1
                else:
                    word2="No, my number is MORE than "+str(g)
                    write(word2)
                    ctr+=1
                word3="You have " + str(6-ctr) + " more chance"
                print(word3)
                print()
            else:
                break
    if flag==0:
        print()
        time.sleep(2)
        write("Better luck next time...")
        time.sleep(0.3)
        # write("YOU LOST")
        # time.sleep(0.3)
        print()
        word5="The number I was thinking was "+str(n)
        write(word5)

            
