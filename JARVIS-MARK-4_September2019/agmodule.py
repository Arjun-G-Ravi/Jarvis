import math
import time

def quadeqn():                    #quadratic equation
    print("For a quadratic equation__ ax**2 + bx + c __,enter coefficients a,b,c below:")
    print("Make sure that a,b,c are INTEGERS") 
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    c=int(input("Enter c: "))
    if a==0:
        print("a shouldnot be zero")
        time.sleep(0.3)
        print("\n Aborting!!!.............................")
        time.sleep(0.3)
    else:
        d=b*b-4*a*c
        if d>0:
            r1=(-b+math.sqrt(d))/(2*a)
            r2=(-b-math.sqrt(d))/(2*a)
            print("Roots are REAL and UNEQUAL")
            print("ROOT1=",r1," , ROOT2=",r2)
        elif d==0:
            r1=(-b+math.sqrt(d))/(2*a)
            print("Roots are REAl and EQUAL")
            print("ROOT=",r1)
        else:
            print("Roots are COMPLEX and IMAGINARY")
 
def BMI():                #BMI
    weight4BMI=float(input("Enter weight in kg:"))
    height4BMI=float(input("Enter height in metere:"))
    BMI=weight4BMI/(height4BMI*height4BMI)
    print("Your BMI is",BMI)

def multable():                                #multiplication table
    n=int(input("Enter the number whose multiplication table you want to print:"))
    m=int(input("Upto which number you want the table to be shown"))
    for a in range(1,m+1):
        print(n,"X",a,"=",n*a)

def fact():                                #factorial
    num=int(input("Enter a number:-"))
    a=1
    fact=1
    while a<= num:
        fact*=a
        a+=1
    print("The factorial of",num,"is",fact)

def Simint():
    p=int(input("Enter the principal value:"))
    r=int(input("Enter annual rate of interest:"))
    t=int(input("Total time for the interest calculation:"))
    Sint=p*r*t/100
    amt=p+Sint
    print("Total amount to be paid=",amt)

def Fibonacci():
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

def pastrl(n):
    trow=[1]
    y=[0]
    for x in range(max(n,0)):
        print(trow)
        trow=[l+r for l,r in zip(trow+y,y+trow)]
    return n>=1
        

    