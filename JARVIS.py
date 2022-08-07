                            # importing modules
import pyttsx3               
import webbrowser 
import random 
import speech_recognition as sr 
import wikipedia
import os 
import sys
import math
from time import sleep
import random
from datetime import datetime

                             # importing user defined modules
from speech import *  
from aggame import *    


                            # Some parameters
dt3=.3   #delay time
dt5=.5
dt1=.1




                            #Program starts here
print()
print("#################################################################")
print("*****************************************************************")
print("                          JARVIS MARK V")
print("*****************************************************************")
print("#################################################################")
print()

greet()
speak("I am Jarvis. Your personal digital assistant")
while True:
    write("How may I help you?")
    sleep(dt3)
    print()
    print("1 Interactive mode")
    sleep(dt1)
    print("2 Guess Game")
    sleep(dt1)
    print("3 Applications")
    sleep(dt1)
    print("5 Credits")
    sleep(dt1)
    print("6 Exit")
    sleep(dt5)
    print()
    write("Type in a choice: ")
    x=int(input())

    if x==1:
        pass
    elif x==2:
        guessgame()
    elif x==3:
        pass
    elif x==4:
        pass
    elif x==5:
        speak("It was nice talking with you")
        write("Good bye")
        break
    else:
        
        write("Wrong Choice")
        write("Good bye")
        break


