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
from agmodule import *  


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
        

        speak("These are some of the applications my  current version has.")
        while True:    
            print()
            speak("Select the required application")
            sleep(dt5)
            print("1 Calculate Body Mass Index")
            sleep(dt3)
            print("2 Multiplication table")
            sleep(dt3)
            print("3 Factorial Calculation")
            sleep(dt3)
            print("4 Solving a quadratic equation")
            sleep(dt3)
            print("5 Calculating Fibonacci Series")
            sleep(dt3)
            print("6 Pascal's triangle")
            sleep(dt3)
            print("Press Enter to exit.")
            print()
            print("You can choose any of these: ")
            ch=int(input())

            if ch==1:
                BMI()
            elif ch==1:
                mulTable()
            elif ch==1:
                factorial()
            elif ch==1:
                QE()
            elif ch==1:
                fib()
            elif ch==1:
                pasTriangle()
            else:
                break

    elif x==4:
        pass
    elif x==5:
        pass
    elif x==6:
        word=random.choice(['',"It was nice talking to you","That was a nice chat","Thanks for the chat, mate","That was fun. Talk to me when free"])
        speak(word)
        write("Good bye")
        break
    else:
        write("Wrong Choice")
        write("Good bye")
        break


