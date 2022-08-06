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


                            # Some parameters
dt=.3   #delay time




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
    sleep(dt)
    print("1 Interactive mode")
    print("2 Guess Game")
    print("3 Applications")
    print("5 Credits")
    print("6 Exit")
    sleep(dt)
    print()
    write("Type in a choice: ")
    x=int(input)

    if x==1:
        pass
    elif x==2:
        pass
    elif x==3:
        pass
    elif x==4:
        pass
    elif x==5:
        pass
    else:
        pass


