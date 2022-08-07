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
    bmi=round(bmi,2)
    word="Your body mass index is "+ str(bmi)
    write(word)
    if bmi<15:
        write("You appear to be underweight")
    elif bmi<18.5:
        write("You appear to be slightly underweight")
    elif bmi<24.9:
        write("You appear to be in the healthy BMI range")
    elif bmi<29.9:
        write("You appear to be a bit overweight")
    elif bmi<=29.9:
        write("You appear to be obese")


def mulTable():                                #multiplication table
    write("Enter the number whose multiplication table you want to print:")
    n=int(input())
    write("Upto which number you want the table to be shown")
    m=int(input())
    for a in range(1,m+1):
        print(n,"X",a,"=",n*a)

def factorial():                                #factorial
    write("Enter the number whose factorial you want to find: ")
    num=int(input())
    a=1
    fact=1
    while a<= num:
        fact*=a
        a+=1
    word="The factorial of"+str(num)+"is"+str(fact)
    write(word)
def fib():
    n1=1
    n2=1
    count=0
    tup=()
    write("Enter the number of terms which fibanoci series is to be displayed:")
    ntr=int(input())
    if ntr<1:
        write("Enter a positive number")
    elif ntr==1:
        write("fibanoci series upto 1 term:")
        print("1")
    elif ntr==2:
        write("fibanoci series upto 2 terms:")
        print("1")
        print("1")
    else:
        word="Fibanoci series upto"+str(ntr)+"terms is:"
        write(word)
        while count<ntr:
            for i in range(ntr-2):
                n3=n1+n2
                print(n3)
                n1=n2
                n2=n3
            

def pasTriangle(n):
    trow=[1]
    y=[0]
    for x in range(max(n,0)):
        print(trow)
        trow=[l+r for l,r in zip(trow+y,y+trow)]
    return n>=1

