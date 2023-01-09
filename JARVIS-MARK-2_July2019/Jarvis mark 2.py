import aggame
import math
import agmodule
import time
import random
print()
t1=time.time()
print("____________________________WELCOME______________________________")                      # Slow mo for effect
time.sleep(1)
print()
print()
print("#################################################################")
print("*****************************************************************")
print("                          JARVIS MARK II")
print("*****************************************************************")
print("#################################################################")
print()
print()
time.sleep(1)
print("Hello")
time.sleep(0.3)
print("I'm JARVIS")
time.sleep(0.3)
name=input("What can I call you:-")
print("I'm happy to see you,",name)
time.sleep(0.5)
again="y"
while again=="y":
    print()
    print("What do you want me to do,",name)
    time.sleep(1)
    print("1.The Arc reactor")
    time.sleep(0.3)
    print("2.Program info")
    time.sleep(0.3)
    print("3.Free talk")
    time.sleep(0.3)
    print("4.Applications")
    time.sleep(0.3)
    print("5.Games")
    time.sleep(0.3)
    choice1=input("Choose 1 or 2 or 3 or 4 or 5:-")
    print("                 -----")
    if choice1=="1":
        password=input("Enter password:")            #I am inevitable
        thanos = "password"
        if password==thanos:               #imported password from file to increase security
            print("Acess granted.Welcome,",name)
            print("Info on the AR tech")
            print("_______________________________________________________________")
            print()
            f=open("AR_tech.txt",'r')          #import file into this___________read on the program\\\
            print(f.read())
            print()
            print("________________________________________________________________")
            input()      
        else:
            print("PASSWORD INCORRECT!!!!!!!!!!!!!!!!!!!")
            time.sleep(0.3)
            print("\n Aborting....................")
            time.sleep(0.3)
            print("CLOSING PROGRAM ............................")
            time.sleep(0.3)
            print("Press Enter key.....")
            input()
            break
    elif choice1=="2":
        print("This program was made by Arjun G Ravi on 31.07.2019")
        time.sleep(1)
    elif choice1=="3":
        print("So,Hello again",name)
        time.sleep(0.5)
        print("Introducing myself, I'm JARVIS MARK 2.0")
        time.sleep(0.5)
        print("So,",name,"how old are you...?")
        age=input()
        if age.isdigit()==True:
            age=int(age)
            if name.upper()=="SRINIVAS" and age==17:
                print("I GOT A SURPRISE FOR YOU")
                time.sleep(0.5)
                print("!!!!!")
                time.sleep(1)
                f=open("Agent45.txt","r")
                print(f.read())
        else:
            print("Okay....")
            print("You are not taking this one seriously...")
            print("You don't want to reveal your age")
            print("    :( ")
        time.sleep(1)
    elif choice1=="4":
        print("Select the required application")
        time.sleep(1)
        print("1.Calculate BMI")
        time.sleep(0.3)
        print("2.Simple calculator")
        time.sleep(0.3)
        print("3.Multiplication table")
        time.sleep(0.3)
        print("4.Factorial Calculation")
        time.sleep(0.3)
        print("5.Solving a quadratic equation")
        time.sleep(0.3)
        print("6.Calculating Simple interest")
        time.sleep(0.3)
        print("7.Calculating Compound interest")
        time.sleep(0.3)
        print("8.Calculating Fibonacci Series")
        time.sleep(0.3)
        print("9.Power calculation")
        time.sleep(0.3)
        print("10.Pascals triangle")
        time.sleep(0.5)
        choice2=input("Choose (1-10):-")                     #pg no 34 + pyplot to improve
        if choice2=="1":                                                                                                                                   #100
            agmodule.BMI()
            input()
        elif choice2=="2":                                          #Calculator
            print("This is a simple calculator to operate 2 numbers")
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
            print("ERROR")
            input()
    elif choice1=="5":
        print("Select the required game")
        time.sleep(0.3)
        print("1.Guess game")                 #add more games
        time.sleep(0.3)
        print("2.Lottery")
        time.sleep(0.3)
        choice2=input("ENter Enter choice:")
        if choice2=="1":
            game.guessgame()
        elif choice2=="2":                   #Lottery
            x=random.randint(1,6)
            y=int(input("enter a number between 1 and 6[includes 1 and 6 ]:"))
            print("Your selection ....................")
            time.sleep(1)
            print(".....")
            time.sleep(1)
            print("is........")
            time.sleep(2)
            print("...................")
            time.sleep(0.5)
            print("perfectly............")
            time.sleep(3)
            if x==y:
                print("CORRECT!!!")
                print("You won the lot")
                time.sleep(0.3)
                print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            else:
                print("                   INCORRECT!!!")
                print("You lost")
                print("Better luck next time")
                time.sleep(0.3)
                print("The lucky number was",x)
        else:
            print("SORRY")
            input()
    else:
        print("SORRY WRONG CHOICE")
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
time.sleep(0.3)
print()
print("____________________________________________________________________")
print()
print()
time.sleep(0.6)                                                                                                                                           #200
print("The total time spend by you on the program is :",t3,"seconds")
print()
time.sleep(1)
print("Press Enter key to close......")
input()
                #includes
                    #2 modules:-game,agmodule
                    #file AR_tech
                    #files Virus,password,9447430529,9446707053,8547309965
                    #      4545454545,1234567890,incorrect_password
