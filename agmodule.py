import math
import time
from speech import *  
from aggame import *  
from agmodule import * 


def QE():                    #quadratic equation

    
    print("Consider the general form of a quadratic equation:  ax**2 + bx + c")
    print("a, b and c should be integers.")
    time.sleep(1)
    speak("Enter the values of a, b and c: ")
    
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    c=int(input("Enter c: "))
    if a==0:
        write("a shouldnot be zero.")
        time.sleep(0.3)
        speak("ERROR"*3)
        time.sleep(0.3)
    else:
        d=b*b-4*a*c
        if d>0:
            r1=(-b+math.sqrt(d))/(2*a)
            r2=(-b-math.sqrt(d))/(2*a)
            speak("Roots are REAL and UNEQUAL")
            word="ROOT1="+ str(r1) +"and  ROOT2="+ str(r2)
            write(word)
        elif d==0:
            r1=(-b+math.sqrt(d))/(2*a)
            write("Roots are REAl and EQUAL")
            word="ROOT="+ str(r1)

        else:
            write("Roots are COMPLEX and IMAGINARY")
 
def BMI():                #BMI
    write("Enter weight in kg:")
    weight4BMI=float(input())
    write("Enter height in metre:")
    height4BMI=float(input())
    bmi=weight4BMI/(height4BMI*height4BMI)
    word="Your body mass index is"+ str(bmi)
    write(word)
    if bmi<15:
        write("You appear to be underweight")
    if bmi<18.5:
        write("You appear to slightly underweight")
    if bmi<24.9:
        write("You appear to be in the healthy BMI range")
    if bmi<29.9:
        write("You appear to be a bit overweight")
    if bmi<=29.9:
        write("You appear to be obese")


def mulTable():                                #multiplication table
    
    n=int(input("Enter the number whose multiplication table you want to print:"))
    m=int(input("Upto which number you want the table to be shown"))
    for a in range(1,m+1):
        print(n,"X",a,"=",n*a)

def factorial():                                #factorial
    num=int(input("Enter a number:-"))
    a=1
    fact=1
    while a<= num:
        fact*=a
        a+=1
    print("The factorial of",num,"is",fact)

def fib():
    n1=0
    n2=1
    count=0
    tup=()
    ntr=int(input("Enter the number upto which fibanoci series is to be displayed:"))
    if ntr<1:
        print("Enter a positive number")
    elif ntr==1:
        print("fibanoci series upto 1:")
        print("0")
    else:
        print("Fibanoci series upto",ntr,"terms is:")
        while count<ntr:
            tup=tup+(n1,)
            nth=n1+n2
            n1=n2
            n2=nth
            count+=1
            print(tup)

def pasTriangle(n):
    trow=[1]
    y=[0]
    for x in range(max(n,0)):
        print(trow)
        trow=[l+r for l,r in zip(trow+y,y+trow)]
    return n>=1

