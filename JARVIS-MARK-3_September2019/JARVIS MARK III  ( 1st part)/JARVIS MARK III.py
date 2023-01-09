import pyttsx3 
import webbrowser 
import smtplib 
import random 
import speech_recognition as sr 
import wikipedia 
import datetime 
import wolframalpha 
import os 
import sys
import aggame                #ME
import math
import agmodule               #ME
import time
import random
import speech                  #ME
t1=time.time()
print()
print("#################################################################")
print("*****************************************************************")
print("                          JARVIS MARK III")
print("*****************************************************************")
print("#################################################################")
print()
speech.greetMe()
speech.speak('I am JARVIS, your digital assistant')
speech.speak("What may I call you ,sir?")
name=input()
speech.speech("So I will call you")
speech.speech(name)
speech.speak("HOW MAY I HELP YOU")
again="Y"
while again.upper()=="Y":
    print()
    speech.speak("1 Top Secret")
    speech.speak("2 Program info")
    speech.speak("3 Free talk")
    speech.speak("4 Applications")
    speech.speak("5 Games")
    print()
    time.sleep(0.3)
    choice1=input("Type 1 or 2 or 3 or 4 or 5:-")
    print("                 -----")
    if choice1=="1":
        password=input("Enter password:")            #I am inevitable
        Tony_Stark="Ironman_forever"                                 # And................. I am Ironman
        virus=open("9446707052.txt",'r')
        _blastoise=virus
        thanos=_blastoise.read()
        if password==thanos:               #imported password from file to increase security
            speech.speak("Acess granted.Welcome,sir")
            speech.speak("Info on the Avengers")
            print("_______________________________________________________________")
            print()
            f=open("AR_tech.txt",'r')          #import file into this___________read on the program\\\
            print(f.read())
            print()
            print("________________________________________________________________")
            input()      
        else:
            speech.speak("PASSWORD INCORRECT!!!!!!!!!!!!!!!!!!!")
            time.sleep(0.3)
            speech.speech("\n Aborting....................")
            speech.speech("\n Aborting....................")
            speech.speech("\n Aborting....................")
            time.sleep(0.3)
            speech.speak("CLOSING PROGRAM ............................")
            time.sleep(0.3)
            speech.speak("Press Enter key.....")
            input()
            break
    elif choice1=="2":
        speech.speak("This is the third part of Jarvis")
        speech.speech("JARVIS MARK 3")
        time.sleep(1)
    elif choice1=="3":
        print("The full access to the program requires an active internet connection")
        time.sleep(1)
        speech.speak("Are you online,sir?")
        online=input("Type{Y/N}:")
        if online.upper()=="Y":
            if __name__ == '__main__': 
                 while True: 
                     query = speech.myCommand(); 
                     query = query.lower() 
                      
                     if 'open youtube' in query: 
                         speech.speak('okay') 
                         webbrowser.open('www.youtube.com') 
             
             
                     elif 'open google' in query: 
                         speech.speak('okay') 
                         webbrowser.open('www.google.co.in') 
             
             
                     elif 'open gmail' in query: 
                         speech.speak('okay') 
                         webbrowser.open('www.gmail.com') 
             
             
                     elif "what\'s up" in query or 'how are you' in query: 
                         stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy'] 
                         speech.speak(random.choice(stMsgs)) 
             
             
                     elif 'nothing' in query or 'abort' in query or 'stop' in query: 
                         speech.speak('okay') 
                         speech.speak('Bye Sir, have a good day.') 
                         sys.exit() 
                         
                     elif 'hello' in query: 
                         speech.speak('Hello Sir') 
             
             
                     elif 'bye' in query: 
                         speech.speak('Bye Sir, have a good day.') 
                         sys.exit() 
                                                  
                     elif 'play music' in query: 
                         music_folder =Music
                         music = [music1, music2, music3, music4, music5] 
                         random_music = music_folder + random.choice(music) + '.mp3' 
                         os.system(random_music) 
                         speech.speak('Okay, here is your music! Enjoy!')
                     elif 'I wanna type' in query:
                         c3=input("What do you want to search:")
                         res = client.query(c3) 
                         results = next(res.results).text 
                         speech.speak('WOLFRAM-ALPHA says - ') 
                         speech.speak('Got it.') 
                         speech.speak(results) 
                         
                         
                     else: 
                         query = query 
                         speech.speak('Searching...') 
                         try: 
                             try: 
                                 res = client.query(query) 
                                 results = next(res.results).text 
                                 speech.speak('WOLFRAM-ALPHA says - ') 
                                 speech.speak('Got it.') 
                                 speech.speak(results) 
                               
                             except: 
                                 results = wikipedia.summary(query, sentences=5) 
                                 speech.speak('Got it.') 
                                 speech.speak('WIKIPEDIA says - ') 
                                 speech.speak(results) 
                      
                         except: 
                             webbrowser.open('www.google.com') 
                      
                     speech.speak('Next Command! Sir!')

                     
        elif online.upper()=="N":
            c1=input("Type your command")
            c1=c1.upper()
            if c1=="HOW ARE YOU":
             stMsgs = ['I am fine!', 'Nice!', 'I am nice and full of energy'] 
             speech.speak(random.choice(stMsgs)) 


            elif 'nothing' in c1 or 'abort' in c1 or 'stop' in c1 or 'bye' in c1: 
             speech.speak('okay') 
             speech.speak('Bye Sir, have a good day.') 
             sys.exit() 
             
            elif 'hello' in query: 
             speech.speak('Hello Sir')
             speech.speak("Hope you are having a fine time")

            elif 'play music' in c1: 
             music_folder =Music
             music = [music1, music2, music3, music4, music5] 
             random_music = music_folder + random.choice(music) + '.mp3' 
             os.system(random_music) 
             speech.speak('Okay, here is your music! Enjoy!')
            else:
             speech.speak("Sorry sir, activate the internet connection for the pefect functioning of the program")
             speech.speak("Type 'bye' to quit")

            speech.speak('Next Command! Sir!')
        else:
            speech.speak("ERROR")
            print("Wrong command")
            
    elif choice1=="4":
        speech.speak("Select the required application")
        speech.speak("1 Calculate BMI")
        speech.speak("2 Simple calculator")
        speech.speak("3 Multiplication table")
        speech.speak("4 Factorial Calculation")
        speech.speak("5 Solving a quadratic equation")
        speech.speak("6 Calculating Simple interest")
        speech.speak("7 Calculating Compound interest")
        speech.speak("8 Calculating Fibonacci Series")
        speech.speak("9 Power calculation")
        speech.speak("10 Pascals triangle")
        choice2=input("Choose (1-10):-")                     #pg no 34 + pyplot to improve
        if choice2=="1":                                                                                                                                   #100
            agmodule.BMI()
            input()
        elif choice2=="2":                                          #Calculator
            speech.speak("This is a simple calculator to operate 2 numbers")
            N1=float(input("Enter number one:"))
            N2=float(input("Enter number two:"))
            operator=input("Choose + - * /:")
            if operator=="+":
                print(N1+N2)
            elif operator=="-":
                print(N1-N2)
            elif operator=="*":
                print(N1*N2)
            elif operator=="/":
                print(N1/N2)
            else:
                print("Incorrect operator")
            input()
        elif choice2=="3":
            agmodule.multable()
            input()
        elif choice2=="4":
            agmodule.fact()
            input()
        elif choice2=="5":
            agmodule.quadeqn()
            input()
        elif choice2=="6":
            agmodule.Simint()
        elif choice2=="8":
            agmodule.Fibonacci()
        elif choice2=="9":
            b=int(input("Enter the base:"))
            p=int(input("Enter the exponent:"))
            an=math.pow(b,p)
            ans=int(an)
            print("The result is",ans)
        elif choice2=="10":
            n=int(input("Enter the number of rows for the triangle:"))
            agmodule.pastrl(n)
        else:
            speech.speak("ERROR")
            input()
    elif choice1=="5":
        speech.speak("Select the required game")
        speech.speak("1 Guess game")                 #add more games
        speech.speak("2 Lottery")
        choice2=input("ENter Enter choice:")
        if choice2=="1":
            game.guessgame()
        elif choice2=="2":                   #Lottery
            x=random.randint(1,6)
            y=int(input("enter a number between 1 and 6[includes 1 and 6 ]:"))
            speech.speak("Your selection ....................")
            time.sleep(1)
            print(".....")
            time.sleep(1)
            speech.speak("is........")
            time.sleep(2)
            print("...................")
            time.sleep(0.5)
            speech.speak("perfectly............")
            time.sleep(3)
            if x==y:
                speech.speak("CORRECT!!!")
                speech.speak("You won the lot")
                time.sleep(0.3)
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            else:
                print("                   INCORRECT!!!")
                speech.speak("You lost")
                speech.speak("Better luck next time")
                time.sleep(0.3)
                print("The lucky number was",x)
        else:
            speech.speak("SORRY")
            input()
    else:
        speech.speak("SORRY WRONG CHOICE")
        input("Press Enter key")
    print()
    print("DO YOU WANT TO CONTINUE",name,"?{y/n}")
    again=input()
    print("                 ----------------------------")    
print()
t2=time.time()
t3=t2-t1
time.sleep(0.3)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("                              THANK YOU")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
speech.speech("Thank you sir")
speech.speech("Hope to see you again")
time.sleep(2)
print()
print("____________________________________________________________________")
print()
print()
time.sleep(0.6)                                                                                                                                           #200
speech.speech("The total time spend by you on the program is :")
speech.speech(t3)
speech.speech("seconds")
print()
time.sleep(1)
print("Press Enter key to close......")
input()
                #includes
                    #2 modules:-game,agmodule
                    #file AR_tech
                    #files Virus,password,9447430529,9446707053,8547309965
                    #      4545454545,1234567890,incorrect_password


