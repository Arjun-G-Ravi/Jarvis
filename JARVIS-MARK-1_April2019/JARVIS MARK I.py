import time
print("Hello")
time.sleep(1)
print("I'm JARVIS,Your personal AI companion")
name=input("What can I call you:-")
print("I'm happy to see you",name)
print("")
print("What do you want me to do",name)
print("1.Research info")
print("2.Computer info")
print("3.Free Talk mode")
print("4.Games")
print("5.applications")
choice1=input("Choose 1 or 2 or 3 or 4 or 5:-")
if choice1=="1":
    password=input("Enter password:")
    if password=='4545':
        print("Acess granted.Welcome sir")
        print("This is made on 23.04.2019.")  #add more
elif choice1=="5":
    print("Select the required application")
    print("1.Calculate BMI")
    print("2.Simple calculator")
    choice2=input("Choose 1 or 2 :-")
    if choice2=="1":
        weight4BMI=float(input("Enter weight in kg:"))
        height4BMI=float(input("Enter height in metere:"))
        BMI=weight4BMI/(height4BMI*height4BMI)
        print("Your BMI is",BMI)
    elif choice2=="2":
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
            print("ERROR")
    else:
        print("Under construction")
else:
    print("sorry",name,"program under construction")
print("Thank you",name)
input("Press enter key to close the prgoram.....")
