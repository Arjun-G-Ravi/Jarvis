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
import aggame                  #NameSpace
import math
import agmodule                #NameSpace
import time
import random
import speech                  #NameSpace
# from LLM import *              #NameSpace
from turtle import *
from datetime import datetime




t1=time.time()
print()
print("#################################################################")
print("*****************************************************************")
print("                          JARVIS MARK IV")
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
speech.speech(name)
again="Y"
while again.upper()=="Y":
    print()
    print("1 Top Secret")
    print("2 Help")
    print("3 Interactive mode")
    print("4 Applications")
    print("5 Games")
    print("6 Credits")
    print()
    time.sleep(0.3)
    choice1=input("Type 1-6 :-")
    print("                 -----")


#TOP SECRET                                                                                                                          $$$$$$$$$$$$$$$$$$$$$$$
    if choice1=="1":
        password=input("Enter password:")            #I am inevitable
        Tony_Stark="Ironman_forever"                                 # And................. I am Ironman
        virus=open("9446707052.txt",'r')
        _blastoise=virus
        thanos=_blastoise.read()
        if password==thanos:               #imported password from file to increase security
            speech.speak("Acess granted")
            speech.speeck("Welcome")
            speech.speech(name)
            speech.speak("Info on the Python")
            print("_______________________________________________________________")
            print()
            f=open("Pyth.txt",'r')          #import file into this___________read on the program\\\
            print(f.read())
            print()
            print("________________________________________________________________")
            time.sleep(3)
            print()
        else:
            speech.speak("PASSWORD INCORRECT!!!!!!!!!!!!!!!!!!!")
            time.sleep(0.3)
            speech.speech("\n Aborrrting....................")
            speech.speech("\n Aborrting....................")
            speech.speech("\n Aborting....................")
            time.sleep(0.3)
            speech.speak("CLOSING PROGRAM ............................")
            time.sleep(0.3)
            speech.speak("Press Enter key.....")
            input()
            sys.exit()


#INTERACTIVE MODE
                    
    elif choice1=="3":
        print("**")
        print("The full access to the program requires an active internet connection")
        print("**")
        time.sleep(1)
        speech.speak("Are we online?")
        speech.speech(name)
        online=input("Type{Y/N}:")

  #ONLINE MODE
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

                     elif 'open amazon' in query:
                         speech.speak('With pleasure')
                         webbrowser.open("www.amazon.in")

                     elif 'what is your name' in query:
                        speech.speak("Oh, Sorry that I didn't introduce myself")
                        speech.speak("I'm JARVIS")
                        speech.speech(name)
                        speech.speech("I'm a private digital assistant, at your service")
                        speech.speech("I'm a kind of tribute to the genius ,billionare ,playboy, philanthropist")
                        speech.speech("TONY STARK")
             
             
                     elif 'open gmail' in query: 
                         speech.speak('okay') 
                         webbrowser.open('www.gmail.com') 
             
             
                     elif "what\'s up" in query or 'how are you' in query: 
                         stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy'] 
                         speech.speak(random.choice(stMsgs)) 
             
             
                     elif 'nothing' in query or 'abort' in query or 'stop' in query: 
                         speech.speak('okay') 
                         speech.speak('Bye Sir, have a good day.') 
                         break

                     elif 'kill power' in query:
                         speech.speek("sure sir")
                         sys.exit()
                         
                     elif 'hello' in query or 'hi' in query: 
                         speech.speak('Hello Sir') 
             
             
                     elif 'bye' in query: 
                         speech.speak('Bye Sir, have a good day.') 
                         break

                     elif 'Shantiniketan School' in query:
                        speech.speak("With pleasure")
                        webbrowser.open('www.shanthiniketanschool.com') 
                        
                                                  
                     '''elif 'play music' in query: 
                         music_folder =Music
                         music = [music1, music2, music3, music4, music5] 
                         random_music = music_folder + random.choice(music) + '.mp3' 
                         os.system(random_music) 
                         speech.speak('Okay, here is your music! Enjoy!')
                         
                     elif 'I wanna type' in query:
                         c3=input("What do you want to search:")
                         res = client.query(c3) 
                         results = next(res.results).text  
                         speech.speak('Got it.') 
                         speech.speak(results) '''
                         
                         
                     '''else: 
                         query = query 
                         speech.speak('Searching...') 
                         try: 
                             try: 
                                 res = client.query(query) 
                                 results = next(res.results).text  
                                 speech.speak('Got it.') 
                                 speech.speak(results) 
                               
                             except: 
                                 results = wikipedia.summary(query, sentences=5) 
                                 speech.speak('Got it.')  
                                 speech.speak(results)
                      
                         except: 
                             webbrowser.open('www.google.com') 
                    '''  
                     speech.speak('Next Command! Sir!')



  #OFFLINE MODE                     
        elif online.upper()=="N":
            speech.speak("Type your command")
            speech.speech(name)
            while True:
                
                c1=input("COMMAND:")
                c1=c1.upper()
                
                if c1=="HOW ARE YOU":
                 stMsgs = ['I am fine!', 'Nice!', 'I am nice and full of energy'] 
                 speech.speak(random.choice(stMsgs)) 


                elif 'nothing' in c1 or 'abort' in c1 or 'stop' in c1 or 'bye' in c1: 
                 speech.speak('okay') 
                 speech.speak('Bye, have a good day.')
                 speech.speech(name)
                 break 
                 
                elif 'hello' in c1 or 'hi' in c1: 
                 speech.speak('Hello')
                 speech.speech(name)
                 speech.speak("Hope you are having a fine time")

                elif 'play music' in c1: 
                #  music_folder =Music
                #  music = [music1, music2, music3, music4, music5] 
                #  random_music = music_folder + random.choice(music) + '.mp3' 
                #  os.system(random_music) 
                 speech.speak('Music not available at the moment')

                else:
                 speech.speak("Sorry sir, activate the internet connection for the pefect functioning of the program")
                 print("You may type 'bye' to quit")

                speech.speak('Next Command!')
                speech.speech(name)
        else:
            speech.speak("ERROR")
            print("Wrong command")


#Application

    elif choice1=="4":
        print("Select the required application")
        print("1 Calculate BMI")
        print("2 Simple calculator")
        print("3 Multiplication table")
        print("4 Factorial Calculation")
        print("5 Solving a quadratic equation")
        print("6 Calculating Simple interest")
        print("7 Calculating Compound interest")
        print("8 Calculating Fibonacci Series")
        print("9 Power calculation")
        print("10 Pascals triangle")

        print("11 Exit")
        choice2=input("Choose (1-10):-")                          #pg no 34 + pyplot to improve

        x=True
        while x==True:
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
                    speech.speak("Incorrect operator")
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


            elif choice2=="11":
                x=False
                
            else:
                speech.speak("ERROR")
                input()


#GAMES
    elif choice1=="5":
        x=True
        while x==True:
            speech.speak("Select the required game")
            speech.speak("1 Guess game")                 #add more games
            speech.speak("2 Lottery")
            speech.speak("3 Paint") 
            speech.speak("4 Clock")
            speech.speak("5 Nim {against the computer} ")
            choice2=input(" Enter your choice:")
            print()

            
            if choice2=="1":
                aggame.guessgame()

                
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

                    
            """elif choice2=="3":
                
                def switchupdown(x=0, y=0):
                    if pen()["pendown"]:
                        end_fill()
                        up()
                    else:
                        down()
                        begin_fill()

                def changecolor(x=0, y=0):
                    global colors
                    colors = colors[1:]+colors[:1]
                    color(colors[0])

                def main():
                    global colors
                    shape("circle")
                    resizemode("user")
                    shapesize(.5)
                    width(3)
                    colors=["red", "green", "blue", "yellow"]
                    color(colors[0])
                    switchupdown()
                    onscreenclick(goto,1)
                    onscreenclick(changecolor,2)
                    onscreenclick(switchupdown,3)
                    return "ENJOY PAINTING"

                if __name__ == "__main__":
                    msg = main()
                    print(msg)
                    mainloop()


            elif choice2=="4":
                def jump(distanz, winkel=0):
                    penup()
                    right(winkel)
                    forward(distanz)
                    left(winkel)
                    pendown()

                def hand(laenge, spitze):
                    fd(laenge*1.15)
                    rt(90)
                    fd(spitze/2.0)
                    lt(120)
                    fd(spitze)
                    lt(120)
                    fd(spitze)
                    lt(120)
                    fd(spitze/2.0)

                def make_hand_shape(name, laenge, spitze):
                    reset()
                    jump(-laenge*0.15)
                    begin_poly()
                    hand(laenge, spitze)
                    end_poly()
                    hand_form = get_poly()
                    register_shape(name, hand_form)

                def clockface(radius):
                    reset()
                    pensize(7)
                    for i in range(60):
                        jump(radius)
                        if i % 5 == 0:
                            fd(25)
                            jump(-radius-25)
                        else:
                            dot(3)
                            jump(-radius)
                        rt(6)

                def setup():
                    global second_hand, minute_hand, hour_hand, writer
                    mode("logo")
                    make_hand_shape("second_hand", 125, 25)
                    make_hand_shape("minute_hand",  130, 25)
                    make_hand_shape("hour_hand", 90, 25)
                    clockface(160)
                    second_hand = Turtle()
                    second_hand.shape("second_hand")
                    second_hand.color("gray20", "gray80")
                    minute_hand = Turtle()
                    minute_hand.shape("minute_hand")
                    minute_hand.color("blue1", "red1")
                    hour_hand = Turtle()
                    hour_hand.shape("hour_hand")
                    hour_hand.color("blue3", "red3")
                    for hand in second_hand, minute_hand, hour_hand:
                        hand.resizemode("user")
                        hand.shapesize(1, 1, 3)
                        hand.speed(0)
                    ht()
                    writer = Turtle()
                    #writer.mode("logo")
                    writer.ht()
                    writer.pu()
                    writer.bk(85)

                def wochentag(t):
                    wochentag = ["Monday", "Tuesday", "Wednesday",
                        "Thursday", "Friday", "Saturday", "Sunday"]
                    return wochentag[t.weekday()]

                def datum(z):
                    monat = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
                             "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
                    j = z.year
                    m = monat[z.month - 1]
                    t = z.day
                    return "%s %d %d" % (m, t, j)

                def tick():
                    t = datetime.today()
                    sekunde = t.second + t.microsecond*0.000001
                    minute = t.minute + sekunde/60.0
                    stunde = t.hour + minute/60.0
                    try:
                        tracer(False)  # Terminator can occur here
                        writer.clear()
                        writer.home()
                        writer.forward(65)
                        writer.write(wochentag(t),
                                     align="center", font=("Courier", 14, "bold"))
                        writer.back(150)
                        writer.write(datum(t),
                                     align="center", font=("Courier", 14, "bold"))
                        writer.forward(85)
                        tracer(True)
                        second_hand.setheading(6*sekunde)  # or here
                        minute_hand.setheading(6*minute)
                        hour_hand.setheading(30*stunde)
                        tracer(True)
                        ontimer(tick, 100)
                    except Terminator:
                        pass  # turtledemo user pressed STOP

                def main():
                    tracer(False)
                    setup()
                    tracer(True)
                    tick()
                    return "WALL CLOCK"

                if __name__ == "__main__":
                    mode("logo")
                    msg = main()
                    print(msg)
                    mainloop()

            elif choice2==5:
                SCREENWIDTH = 640
                SCREENHEIGHT = 480

                MINSTICKS = 7
                MAXSTICKS = 31

                HUNIT = SCREENHEIGHT // 12
                WUNIT = SCREENWIDTH // ((MAXSTICKS // 5) * 11 + (MAXSTICKS % 5) * 2)

                SCOLOR = (63, 63, 31)
                HCOLOR = (255, 204, 204)
                COLOR = (204, 204, 255)

                def randomrow():
                    return random.randint(MINSTICKS, MAXSTICKS)

                def computerzug(state):
                    xored = state[0] ^ state[1] ^ state[2]
                    if xored == 0:
                        return randommove(state)
                    for z in range(3):
                        s = state[z] ^ xored
                        if s <= state[z]:
                            move = (z, s)
                            return move

                def randommove(state):
                    m = max(state)
                    while True:
                        z = random.randint(0,2)
                        if state[z] > (m > 1):
                            break
                    rand = random.randint(m > 1, state[z]-1)
                    return z, rand


                class NimModel(object):
                    def __init__(self, game):
                        self.game = game

                    def setup(self):
                        if self.game.state not in [Nim.CREATED, Nim.OVER]:
                            return
                        self.sticks = [randomrow(), randomrow(), randomrow()]
                        self.player = 0
                        self.winner = None
                        self.game.view.setup()
                        self.game.state = Nim.RUNNING

                    def move(self, row, col):
                        maxspalte = self.sticks[row]
                        self.sticks[row] = col
                        self.game.view.notify_move(row, col, maxspalte, self.player)
                        if self.game_over():
                            self.game.state = Nim.OVER
                            self.winner = self.player
                            self.game.view.notify_over()
                        elif self.player == 0:
                            self.player = 1
                            row, col = computerzug(self.sticks)
                            self.move(row, col)
                            self.player = 0

                    def game_over(self):
                        return self.sticks == [0, 0, 0]

                    def notify_move(self, row, col):
                        if self.sticks[row] <= col:
                            return
                        self.move(row, col)


'''    class Stick(turtle.Turtle):
                    def __init__(self, row, col, game):
                        turtle.Turtle.__init__(self, visible=False)
                        self.row = row
                        self.col = col
                        self.game = game
                        x, y = self.coords(row, col)
                        self.shape("square")
                        self.shapesize(HUNIT/10.0, WUNIT/20.0)
                        self.speed(0)
                        self.pu()
                        self.goto(x,y)
                        self.color("white")
                        self.showturtle()

                    def coords(self, row, col):
                        packet, remainder = divmod(col, 5)
                        x = (3 + 11 * packet + 2 * remainder) * WUNIT
                        y = (2 + 3 * row) * HUNIT
                        return x - SCREENWIDTH // 2 + WUNIT // 2, SCREENHEIGHT // 2 - y - HUNIT // 2

                    def makemove(self, x, y):
                        if self.game.state != Nim.RUNNING:
                            return
                        self.game.controller.notify_move(self.row, self.col)


                class NimView(object):
                    def __init__(self, game):
                        self.game = game
                        self.screen = game.screen
                        self.model = game.model
                        self.screen.colormode(255)
                        self.screen.tracer(False)
                        self.screen.bgcolor((240, 240, 255))
                        self.writer = turtle.Turtle(visible=False)
                        self.writer.pu()
                        self.writer.speed(0)
                        self.sticks = {}
                        for row in range(3):
                            for col in range(MAXSTICKS):
                                self.sticks[(row, col)] = Stick(row, col, game)
                        self.display("... a moment please ...")
                        self.screen.tracer(True)

                    def display(self, msg1, msg2=None):
                        self.screen.tracer(False)
                        self.writer.clear()
                        if msg2 is not None:
                            self.writer.goto(0, - SCREENHEIGHT // 2 + 48)
                            self.writer.pencolor("red")
                            self.writer.write(msg2, align="center", font=("Courier",18,"bold"))
                        self.writer.goto(0, - SCREENHEIGHT // 2 + 20)
                        self.writer.pencolor("black")
                        self.writer.write(msg1, align="center", font=("Courier",14,"bold"))
                        self.screen.tracer(True)

                    def setup(self):
                        self.screen.tracer(False)
                        for row in range(3):
                            for col in range(self.model.sticks[row]):
                                self.sticks[(row, col)].color(SCOLOR)
                        for row in range(3):
                            for col in range(self.model.sticks[row], MAXSTICKS):
                                self.sticks[(row, col)].color("white")
                        self.display("Your turn! Click leftmost stick to remove.")
                        self.screen.tracer(True)

                    def notify_move(self, row, col, maxspalte, player):
                        if player == 0:
                            farbe = HCOLOR
                            for s in range(col, maxspalte):
                                self.sticks[(row, s)].color(farbe)
                        else:
                            self.display(" ... thinking ...         ")
                            time.sleep(0.5)
                            self.display(" ... thinking ... aaah ...")
                            farbe = COLOR
                            for s in range(maxspalte-1, col-1, -1):
                                time.sleep(0.2)
                                self.sticks[(row, s)].color(farbe)
                            self.display("Your turn! Click leftmost stick to remove.")

                    def notify_over(self):
                        if self.game.model.winner == 0:
                            msg2 = "Congrats. You're the winner!!!"
                        else:
                            msg2 = "Sorry, the computer is the winner."
                            speech.speek("The computer loses only in 1 out of every 14 million 405 possibilities")
                            speech.speek("YOu are so very wise")
                            speech.speek(name)
                        self.display("To play again press space bar. To leave press ESC.", msg2)

                    def clear(self):
                        if self.game.state == Nim.OVER:
                            self.screen.clear()


                class NimController(object):

                    def __init__(self, game):
                        self.game = game
                        self.sticks = game.view.sticks
                        self.BUSY = False
                        for stick in self.sticks.values():
                            stick.onclick(stick.makemove)
                        self.game.screen.onkey(self.game.model.setup, "space")
                        self.game.screen.onkey(self.game.view.clear, "Escape")
                        self.game.view.display("Press space bar to start game")
                        self.game.screen.listen()

                    def notify_move(self, row, col):
                        if self.BUSY:
                            return
                        self.BUSY = True
                        self.game.model.notify_move(row, col)
                        self.BUSY = False


                class Nim(object):
                    CREATED = 0
                    RUNNING = 1
                    OVER = 2
                    def __init__(self, screen):
                        self.state = Nim.CREATED
                        self.screen = screen
                        self.model = NimModel(self)
                        self.view = NimView(self)
                        self.controller = NimController(self)


                def main():
                    mainscreen = turtle.Screen()
                    mainscreen.mode("standard")
                    mainscreen.setup(SCREENWIDTH, SCREENHEIGHT)
                    nim = Nim(mainscreen)
                    return "ALL THE BEST"

                if __name__ == "__main__":
                    main()
                    turtle.mainloop()


                

            else:
                speech.speak("SORRY")
                input()'''"""


#CREDITS
    elif choice1=="6":
                
                a=open("ABOUT.txt")
                b=a.read()
                a.close()
                speech.speak(b)
                del a,b
                speech.speech("This is also a kind of tribute to the genius ,billionare ,playboy, philanthropist")
                speech.speech("TONY STARK")
                speech.speech("The idea and inspiration is one hundred percent from his innovation")
                print("*****************************************************************")
                


#IF WRONG CHOICE
                
    else:
        speech.speak("SORRY WRONG CHOICE")
        input("Press Enter key")
    print()
    print("DO YOU WANT TO CONTINUE",name,"?{y/n}")
    again=input()
    print("                 ----------------------------")

#
print()
t2=time.time()
t3=round(t2-t1,2)
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
time.sleep(0.6)                                                                                                                                         
speech.speech("The total time spend by you on the program is :")
speech.speech(t3)
speech.speech("seconds")
print()
time.sleep(1)
print("Press Enter key to close......")
input()

#THE END                                                                                                                                 
    
        



                        


                




