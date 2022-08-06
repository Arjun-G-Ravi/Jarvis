                            # importing modules
import pyttsx3               
import webbrowser 
import random 
import speech_recognition as sr 
import wikipedia
import os 
import sys
import math
import time
import random
from datetime import datetime

                             # importing user defined modules
from speech import *      

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
    print("1 Interactive mode")
    print("2 Guess Game")
    print("3 Applications")
    print("5 Credits")
    print("6 Exit")

    
