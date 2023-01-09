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
    speech.speak("2 Help")
    speech.speak("3 Free talk")
    speech.speak("4 Applications")
    speech.speak("5 Games")
    print()
    time.sleep(0.3)
    choice1=input("Type 1 or 2 or 3 or 4 or 5:-")
    print("                 -----")
    if choice1=="1":
        password=input("Enter password:")            #I am inevitable
        thanos = "1"
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

        try:
            from LLM import *
        except ImportError:
            print("Module Not imported")

        # MAIN
        con=True
        while con:
            print("################################################################################")
            print(" ")
            print("                                 PYTHON TUTORIAL                                ")
            print(" ")
            print("################################################################################")
            print(" ")
            print(" Welcome to python tutorial!!!!!!!!")
            print(" ")
            print("  1. GET STARTED with PYTHON")
            print("  2. ABOUT PYTHON AND PROJECT")
            print("  3. EXIT")
            try:
                i1=int(input("Enter your choice(1-3):"))
            except IOError:
                print(" No Input!")
                print(" ")
                print("PROGRAM WILL RESTART")
                cls(2)

            if i1==1:
                con2=True
                while con2:
                    cls(2)
                    print(" Lets start with python")
                    print("Choose anyone of the module to start")
                    cls(2)
                    print(" 1. Working with Srings")
                    print(" 2. Simple Input and Output Statements")
                    print(" 3. Python Functions and Modules")
                    print(" 4. Loops in Python")
                    print(" 5. Data Types and Usage")
                    print(" 6. Linear list Manipulation")
                    print(" 7. Stacks and Queues")
                    print(" 8. Data File Handiling")
                    print(" 9. Exception handiling and Generators in python")
                    print("10. Get back to main menu")

                    try:
                        i2=int(input("Enter your choice(1-10):"))
                    except IOError:
                        print(" No input given")

                    if i2==1: # String OPerations
                        con3=True
                        while con3:
                            cls(2)
                            s()
                            print("Strings :-A data type are any number of valid characters into a set of quotion marks.")
                            print("Operations that can be performed with string are::")
                            print("1.Traversing of string")
                            print("2.String opeartors  on string")
                            print("3.String Functions")
                            print("4.Slicing a string")
                            print("5.Get Back to previous menu")

                            try:
                                i3=int(input("Enter your choice(1-5):"))
                            except IOError:
                                print("No input given")

                            if i3==1:
                                print("Traversing can be performed in a following way")
                                a="Python"
                                print(">>>a='Python'")
                                print(">>>for i in a:")
                                print("      print i,'-'")
                                print("_______________")
                                for i in a :
                                    print(i,"-",)
                                print(" *** ")


                                input("Press Enter to Continue")

                            elif i3==2:
                                print("String operators are")
                                print("1.String Concatenation operator (+):")
                                print("  eg.")
                                print("     'ram' + 'shayam'")
                                print("  will result into")
                                print("     'ramshayam' ")
                                print("2. String replication operator  (*):")
                                print("  eg.")
                                print("     'DSS'*3")
                                print("  will result into ")
                                print("     'DSSDSSDSS'")
                                print("3. Mermbership operator:")
                                print("in : Returns True if sub string  exist in given string, otherwise False")
                                print("not in: Returns True if sub string   not exist in given string, oterwise False")
                                print(" eg.")
                                print("   >>> 'a' in 'ram'")
                                print("       True")
                                print("   >>> 'a' not in 'ram'")
                                print("4.Comparison operator(<,>,>=,<=,==,!=):")
                                print(" eg.")
                                print("   'a'=='a' will give True")
                                print("   'a'=='b' will give False")


                                input("Press Enter to Continue")

                            elif i3==3:
                                q=open("S_FUN.txt")
                                w=q.read()
                                print(w)
                                del q,w


                                input("Press Enter to Continue")

                            elif i3==4:
                                cls(2)
                                print("Slicing a string can be performed  as follow,")
                                print("")
                                print(">>a=ramayan")
                                a='ramayan'
                                print(">>>print a[0:3]")
                                print("  ",a[0:3])


                                input("Press Enter to Continue")

                            elif i3==5:
                                con3=False

                            else:
                                print("INvalid input !!!!!!!!!!!")

                    elif i2==2:   #Simple I/O Statement
                        print("Smple input and output statement can be given bu using")
                        print("1. For input :")
                        print("  1.input() and")
                        print("  2.raw_input()")
                        print("  Following are sample programs to illustrate")
                        print("    eg.")
                        print("       >>> a=raw_input('Enter your  number:' )")
                        print("           Enter your number: 25")
                        cls(2)
                        print("2.For output Python use 'print' key word")
                        print("")
                        print(">>>For i in 'Python':")
                        print("      print i    ")        # print is output keyword
                        print("   Output will be as")
                        print("   P \n   y\n   t\n   h\n   o\n  n\n")


                        input("Press Enter to continue...")

                    elif i2==3: # FUNctions and modules
                         con4=True
                         while con4:
                             cls(2)
                             print("Python offers 3 type of Functions")
                             print("1.In-built functions")
                             print("2.Function defined in Modules")
                             print("3.User  defined functions")
                             print("4.Get back to previous menu")

                             try:
                                 i4=int(input(" Enter your choice(1-4):"))
                             except IOError:
                                 print("No input provided")

                             if i4==1:
                                print("Python offers some builtin functions which are always availabel to use")
                                print(" eg. len(),type(),int()")
                                cls(2)
                                print(">>> a=Python")
                                print(">>>len(a)")
                                print("   6")


                                input("Press Enter to continue...")

                             elif i4==2:
                                 q=open("M_FUN.txt")
                                 w=q.read()
                                 print(w)
                                 q.close()
                                 del q,w


                                 input("Press Enter to continue...")

                             elif i4==3:
                                 print("These are the functions defined by programmer.And can be defined using 'def' keyword. ")
                                 print("How to create a function is illustrated in following eample")
                                 print()
                                 print("def sum(x,y):")
                                 print("    r= x+y")
                                 print("    return r")
                                 print("a=input('Enter number1:')")
                                 print("b=input('Enter number 2:)")
                                 print("c=sum(a,b)")
                                 print("print c")


                                 input("Press Enter to continue...")

                             elif i4==4:
                                 con4=False

                             else:
                                print("Invalid input")

                    elif i2==4:
                        con5=True
                        while con5:
                            cls(2)
                            print("Python offers  2  type of loop statement")
                            print("1. The for loop")
                            print("2. The while loop")
                            print("3. Get back to previous menu")

                            try:
                                i4=int(input("Enter your choice(1-3):"))
                            except IOError:
                                print("No input provided ")

                            if i4==1:
                                print("The general form of 'for loop' is as given below:")
                                print(" for <variable> in <sequence> :")
                                print("     statements_to_repeat")
                                cls(2)
                                print("eg.")
                                print("    for element in [10,15,20,25]:")
                                print("        print (element +2),")
                                print("Or for loop can be also used wiht range()function")
                                print("eg.")
                                print("   for val in range(3,10):")
                                print("      print val")

                            elif i4==2:
                                print("The general form of while loop is given below")
                                print(" while <logicalExpression>:")
                                print("    loop-body")

                            elif i4==3:
                                con5=False

                            else:
                                print("Invalid Input")

                    elif i2==5:
                        try:
                            e=open("D_T.txt",'r')
                            w=e.read()
                            print(w)
                        except EOFError:
                            print("Error in file opening")
                        del e,w


                        input("Press Enter to continue...")

                    elif i2==6:
                        con6=True
                        while con6:
                            cls(2)
                            print(" Basic operations on Linear list")
                            print("1.Searching")
                            print("2.Insertion")
                            print("3.Deletion")
                            print("4.Traversal")
                            print("5.Sorting")
                            print("6.Return to previous menu")

                            try:
                                i6=int(input("Enter your choice(1-6):"))
                            except:
                                print(" InputError!!!!")

                            if i6==1:
                                con7=True
                                while con7:
                                    cls(2)
                                    print("Python offers 2 type of common searching technique")
                                    print("1.Linear search")
                                    print("2.Binary search")
                                    print("3.Return to previous menu")
                                    try:
                                        i7=int(input("Enter your choice(1-3):"))
                                    except IOError:
                                        print("Input error")

                                    if i7==1:
                                        print("__________________Linear search_______________")
                                        print("In linear search each element of array with the given Item to be searched for, one by one")
                                        print("Following program illustrate searching by linear search")
                                        L=eval(input("Enter the elements: "))
                                        n=len(L)
                                        item=eval(input("Enter the element that you want to search : "))
                                        for i in range(n):
                                            if L[i]==item:
                                                print("Element found at the position :", i+1)
                                                break
                                        else:
                                            print("Element not Found")



                                        input("Press Enter to continue...")

                                    elif i7==2:
                                        print("___________________Binary search_______________")
                                        print(" Binary search can work for any sorted array while linear search can work for both sorted as well as unsorted array")
                                        def Binary_Search(sequence, item, LB, UB):
                                            if LB>UB:
                                                return -5 # return any negative value
                                            mid=int((LB+UB)/2)
                                            if item==sequence[mid]:
                                                return mid
                                            elif item<sequence[mid]:
                                                UB=mid-1
                                                return Binary_Search(sequence, item, LB, UB)
                                            else:
                                                LB=mid+1
                                                return Binary_Search(sequence, item, LB, UB)

                                        L=eval(input("Enter the elements in sorted order: "))
                                        n=len(L)
                                        element=int(input("Enter the element that you want to search :"))
                                        found=Binary_Search(L,element,0,n-1)
                                        if found>=0:
                                            print(element, "Found at the index : ",found+1)
                                        else:
                                            print("Element not present in the list")

                                        input("Press Enter to continue...")

                                    elif i7==3:
                                        con7=False
                                        

                                    else:
                                        print(" Invalid input")
                                      

                            elif i6==2:
                                print("_________________Insertion in a list______________")
                                n=eval(input("Enter the elements in list"))
                                ar=[0]*n
                                for i in range(n):
                                    ar[i]=input("Element"+str(i+1)+":")
                                s_sort(ar)
                                print("List in sorted order is",ar)
                                item=int(input("Enetr new element to be inserted:"))
                                position=Findpos(ar,item)
                                shift(ar,position)
                                ar[position]=item
                                print("The list after insertng",item,"is")
                                print(ar)


                                input("Press Enter to continue...")

                            elif i6==3:
                                print("______________Deletion in a list____________________")
                                n=int(input("Enter desired linear-list size(max. 50).."))
                                ar=[0]*n
                                for i in range(n):
                                    ar[i]=input("Element"+str(i+1)+":")
                                s_sort(ar)
                                print("List in sorted order is",ar)
                                item=input("Enter new element to be deleted:")
                                position=b_s(ar,item)
                                if position:
                                    del ar[position]
                                    print("The list after deletion",item,"is")
                                    print(ar)
                                else:
                                    print("SORRY! No such element in the list")


                                input("Press Enter to continue...")

                            elif i6==4:
                                print("____________ Traversal of list_____________________")
                                n=int(input("Enter desired linear-list size(max. 50).."))
                                ar=[0]*n
                                print("Enter element for the  linear list")
                                for i in range(n):
                                    ar[i]=input("Element"+str(i+1)+":")
                                print("Traversing the list:")
                                traverse(ar)


                                input("Press Enter to continue...")

                            elif i6==5:
                                cls(2)
                                print("Python offers 3 type of common sorting technique")
                                print("1.Selection sort")
                                print("2.Bubble sort")
                                print("3.Insertion sort")
                                try:
                                    i7=int(input("Enter your choice(1-3):"))
                                except IOError:
                                    print("Input error")

                                if i7==1:
                                    print("_______________________Selection sort____________________________")
                                    print()
                                    print(" The basic idea of selection sort is to repeadily select the smallest key in remaining us sorted array")
                                    print(" The following program ilustrate the sorting by selection sort")
                                    n=input("Enter desired linear-list size(max. 50)..")
                                    ar=[0]*n
                                    print("Enter element for the  linear list")
                                    for i in range(n):
                                        ar[i]=input("Element"+str(i+1)+":")
                                    print("Original list is:",ar)
                                    s_sort(ar)
                                    print("List after sorting:",ar)


                                    input("Press Enter to Continue")

                                elif i7==2:
                                    print("______________________Bubble sort__________________________________")
                                    print()
                                    print("The basic idea of bubble sort is  to compare two adjoining values and exchange them if they are not in proper order.")
                                    print(" The following program ilustrate the sorting by Bubble sort")
                                    n=int(input("Enter desired linear-list size(max. 50).."))
                                    ar=[0]*n
                                    print("Enter element for the  linear list")
                                    for i in range(n):
                                        ar[i]=input("Element"+str(i+1)+":")
                                    print("Original list is:",ar)
                                    b_sort(ar)
                                    print("List after sorting:",ar)


                                    input("Press Enter to Continue")

                                elif i7==3:
                                    print("______________________Insertion sort__________________________________")
                                    print()
                                    print("Suppose an array A wuth n elements a[1],A[2],...,A[N} is in memory.The insertion sort algorithm scans A from A[1]to A[N],insertion each element A[K]into is proper position in the previousy sorted sub array A[1],A[2]...,A[K-1].")
                                    print(" The following program ilustrate the sorting by Insertion sort")
                                    n=input("Enter desired linear-list size(max. 50)..")
                                    ar=[0]*n
                                    print("Enter element for the  linear list")
                                    for i in range(n):
                                         ar[i]=input("Element"+str(i+1)+":")
                                    print("Original list is:",ar)
                                    i_sort(ar)
                                    print("List after sorting:",ar)

                                else :
                                    print("Invalid input!!!!")
                                del i7

                            elif i6==6:
                                con6=False

                            else:
                                print("Invalid Input")

                    elif i2==7:
                        con8=True
                        while con8:
                            cls(2)
                            print("1.Stacks")
                            print("2.Queues")
                            print("3.Return to previous menu")
                            try:
                                i7=int(input("Enter your choice(1-3):"))
                            except IOError:
                                print("Input error")

                            if i7==1:
                                print("Python program to illustrate Stack operation")
                                ###############STACK IMPLEMENTAION ###################
                                """
                                   Stack:implemented as a list
                                   top:Integer having topmost elemenet in a stack
                                """
                                stack=[]
                                top=None
                                con=1
                                while con==1:
                                    cls(2)
                                    print("STACK OPERATIONS")
                                    print("1.Push")
                                    print("2.Pop")
                                    print("3.Peek")
                                    print("4.Display stack")
                                    print("5.Exit")
                                    try:
                                        ch=int(input("Enter your choice(1-5):"))
                                    except IOError:
                                        print("Input error")

                                    if ch==1:
                                        try:
                                            item=input("Enter item:")
                                        except IOError:
                                            print("Input error")
                                        push(stack,item)
                                        input("Press Enter to continue....")

                                    elif ch==2:
                                        item=pop(stack)
                                        if item=="Underflow":
                                            print("Underflow! Stack is empty!")
                                        else:
                                            print("Popped item is",item)
                                            input("Press Enter to continue....")

                                    elif ch==3:
                                        item=peek(stack)
                                        if item=="Underflow":
                                            print("Underflow! Stack is empty!")
                                        else:
                                            print("Topmost item is",item)
                                        input("Press Enter to continue....")    

                                    elif ch==4:
                                        display(stack)
                                        input("Press Enter to continue....")

                                    elif ch==5:
                                        con=0

                                    else:
                                        print("INvalid INPUT")


                                

                            elif i7==2:
                                print("Python program to illustrate queue operation")
                                ############### queue IMPLEMENTAION ###################
                                """
                                   queue:implemented as a list
                                   front:Integer having position if first (front most) element in a queue
                                   rear: integer having position of last element in queue
                                """
                                queue=[]
                                front=None
                                b=True
                                while b:
                                    cls(2)
                                    print("QUEUE OPERATIONS")
                                    print("1.Enqueue")
                                    print("2.Dequeue")
                                    print("3.Peek")
                                    print("4.Display queue")
                                    print("5.Exit")
                                    try:
                                        ch=int(input("Enter your choice(1-5):"))
                                    except IOError:
                                        print("Input error")

                                    if ch==1:
                                        try:
                                            item=input("Enter item:")
                                        except IOError:
                                            print("Input error")
                                        qu_enqueue(queue,item)


                                        input("Press Enter to continue....")

                                    elif ch==2:
                                        item=qu_dequeue(queue)
                                        if item=="Underflow":
                                            print("Underflow! Queue is empty!")
                                        else:
                                            print("Deueue-ed item is",item)


                                        input("Press Enter to Continue.....")

                                    elif ch==3:
                                        item=qu_peek(queue)
                                        if item=="Underflow":
                                            print("Underflow! Queue is empty!")
                                        else:
                                            print("Frontmost item is",item)


                                        input("Press Enter to continue...")

                                    elif ch==4:
                                        display(queue)


                                        input("Press Enter to continue...")

                                    elif ch==5:
                                         b=False

                                    else:
                                        print("Invalid choice!")


                                        input("Press Enter to continue...")

                            elif i7==3:
                                con8=False

                            else:
                                print("Invalid Input")
                                

                    elif i2==8:
                        con9=True
                        while con9:
                            cls(2)
                            print("___________________ DATA FILE HANDLING__________________")
                            print("1. Opening and closing a file")
                            print("2. Reading and Writting onto files")
                            print("3. Return to previous menu")
                            try:
                                i7=int(input("Enter your choice(1-3):"))
                            except IOError:
                                print("Input error")

                            if i7==1:
                                a=open("R_W.txt")
                                b=a.read(837)
                                print(b)
                                
                                a.close()
                                input("Press Enter to continue...")

                            elif i7==2:
                                a=open("R_W.txt")
                                b=a.read(837)
                                c=a.read(1900)
                                print(c)
                                a.close()
                                
                                print(" ")


                                input("Press Enter to continue...")
                            elif i7==3:
                                con9=False
                            else:
                                print("Invalid input")
                            

                    elif i2==9:
                        con10=True
                        while con10:
                            cls(2)
                            print("1.Exception Handiling")
                            print("2.Generators")
                            print("3.Return to previous menu")
                            try:
                                i7=int(input("Enter your choice(1-3):"))
                            except IOError:
                                print("Input error")

                            if i7==1:
                                a=open("ERROR.TXT")
                                b=a.read(2140)
                                print(b)
                                a.close()
                                del a,b
                                input("Press Enter to continue.......")

                            elif i7==2:
                                a=open("ERROR.TXT")
                                b=a.read(2140)
                                c=a.read(9999)
                                print(c)
                                a.close()
                                del a,b,c
                                input("Press Enter to continue.......")

                            elif i7==3:
                                con10=False

                            else:
                                print("Invalid Input")

                    elif i2==10:
                        con2=False

                    else:
                        print(" Invalid input!")

            elif i1==2:
                cls(2)
                a=open("ABOUT.txt")
                b=a.read()
                a.close()
                print(b)
                del a,b
                print("*****************************************************************")
                cls(2)

            elif i1==3:
                con=False
                print("Thank u for using program")
                print("Exiting from the program.............")

            else:
                print(" ")
                print(" INVALID INPUT !!!!")
                print(" ")
                print("PROGRAM WILL RESTART")
                for i in range (10000):
                    a=i
                del a



        
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


