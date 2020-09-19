#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 19:46:57 2020

@author: brandonhdz
"""
import random
import sys
import math

# F(x) = Any polynomial of any grade between the range (a,b)

#   NZeros is the number of desired zeros
#   x holds the independent data variable´s values
#       Values of the zeros
#   y holds the dependent data variable´s values
#       Original production sequence
#   ON OUTPUT:
#   array x is sorted from smallest to largest
#

def sort(n,x,y):
    for i in range(0,n-1):
        tmin=x[i]
        imin=i
        for j in range(i+1,n):
            if (tmin>x[j]):
                tmin=x[j]
                imin=j
            #endIf
        #endFor
        if (imin!=i):
            x[imin]=x[i]
            x[i]=tmin
            tmin=y[imin]
            y[imin]=y[i]
            y[i]=tmin
        #endIf
    #endFor
    for i in range(0,n):
        A[i][0]=x[i]
        A[i][1]=y[i]
    #endFor
    return
#endSort

def check_format_coefficients(x):
    while True:
        try:
            x=float(input("\""+x+"\")\t"))
            return float(x)
        except:
            print("May be a number")
            print("Please try again")
    ##EndWhile
##EndFunction

def check_format_grade(x):
    while True:
        try:
            x=float(input("\""+x+"\")\t"))
            return int(x)
        except:
            print("May be a number")
            print("Please try again")
    ##EndWhile
##EndFunction

def polynomial():
    print("Please input the grade of the polynomial you want to create")
    while True:
        grade=check_format_grade("Grade")
        if(grade>=1):
            break
        #endif
        print("Error, it may be, at least, a first degree")
    #endwhile
    Fx=[0]*(grade+1)
    print("Input the coefficient of the grade ",grade," of the polynomial:\t")
    while True:
        texto="Grade "+str(grade)
        a=check_format_coefficients(texto)
        if a==0:
            print("Error. The coefficient of the grade ",grade," may be different of zero.")
        else:
            Fx[0]=a
            break
        ##EndIf
    ##EndWhile
    for i in range(1,grade+1):
        print("Input the coefficient of the grade ",grade-i," of the polynomial:\t")
        texto="Grade "+str((grade-i))
        Fx[i]=check_format_coefficients(texto)
    ##EndFor
    return Fx
##EndFunction

def derivative_pol(Fx):
    grade=len(Fx)-1
    Fx_prime=[0]*(grade)
    for i in range(grade):
        Fx_prime[i]=Fx[i]*(grade-i)
    return Fx_prime

def start(a,b):
    if a>b:
        x0=random.uniform(b,a)
    else:
        x0=random.uniform(a, b)
    return x0

def evaluate_pol(Fx,x):
    res=0
    grade=len(Fx)-1
    for i in range(grade):
        res+=Fx[i]*x**(grade-i)
    res+=Fx[i+1]
    return res 
    
def newtonRaphson(Fx,x0):
    converge=False
    x_n=x0
    Fx_prime=derivative_pol(Fx)
    while not converge:
        x_n1=x_n-(evaluate_pol(Fx,x_n)/evaluate_pol(Fx_prime,x_n))
        if math.isclose(x_n, x_n1, rel_tol=1e-9):
            converge=True
        x_n=x_n1
    return x_n1

def sine(A,B,C,D,x):
    return A*math.sin(B*x+C)+D

def sine_prime(A,B,C,D,x):
    return A*B*math.cos(B*x+C)

def newtonRaphson_Sine(A,B,C,D,x0):
    converge=False
    x_n=x0
    while not converge:
        x_n1=x_n-(sine(A,B,C,D,x_n)/sine_prime(A,B,C,D,x_n))
        if math.isclose(x_n, x_n1, rel_tol=1e-9):
            converge=True
        x_n=x_n1
    return x_n1

def log10(A,B,C,D,x):
    return A*math.log10(B*x+C)+D

def log10_derivative(A,B,C,D,x):
    return (A*B)/(B*x+C)

def exp(A,B,C,x):
    return A*math.exp(B*x)+C

def exp_derivative(A,B,C,x):
    return A*B*math.exp(B*x)

def newtonRaphson_log10(A,B,C,D,x0):
    converge=False
    x_n=x0
    while not converge:
        x_n1=x_n-(log10(A,B,C,D,x_n)/log10_derivative(A,B,C,D,x_n))
        if math.isclose(x_n, x_n1, rel_tol=1e-9):
            converge=True
        x_n=x_n1
    return x_n1

def newtonRaphson_exp(A,B,C,x0):
    converge=False
    x_n=x0
    while not converge:
        x_n1=x_n-(exp(A,B,C,x_n)/exp_derivative(A,B,C,x_n))
        if math.isclose(x_n, x_n1, rel_tol=1e-9):
            converge=True
        x_n=x_n1
    return x_n1

#
#   MAIN
#FINDING ROOTS OF A POLYNOMIAL OF ANY GRADE BETWEEN THE RANGE (a,b) USING NEWTON RAPHSON ALGORITHM
while True:
    print("Select one of the following functions to find the roots:")
    print("1.- Polynomial")
    print("2.- Sine")
    print("3.- Log10")
    print("4.- Exponential")
    while True:
        option=check_format_grade("Option")
        if(option>=1 and option<=5):
            break
        #EndIf
        print("Error. Select one of the available options.")
    
    print("Input the range (a,b) between you want to find the roots")
    a=check_format_coefficients("a")
    b=check_format_coefficients("b")    
    print("Input the number of roots you want to find")
    NZeros=0
    while True:
        NZeros=check_format_grade("NZeros")
        if (((NZeros>=1)and(NZeros<=20))):
            break
        #endif
    #endwhile
    listZeros=[0]*NZeros
    ZerosFound=0
    
    if option==1:
        Fx=polynomial()
    
        for i in range(NZeros):
            for j in range(100):
                x0=start(a, b)
                x_n=newtonRaphson(Fx, x0)
                sameZero=False
                for k in range(0,i):
                    delta=abs(x_n-listZeros[k])
                    if (delta<=1e-6):
                        sameZero=True           #Found the same Zero
                        break                   #Get out of the Zero comparison
                    #endif
                #endfor
                if (not(sameZero)):             #Exit the "j" loop
                    break                       #Back to the "i" loop
                #endif
            #endfor
            if (j!=99):
                ZerosFound=ZerosFound+1
                listZeros[i]=x_n                  #New Zero to the list
            else:
                print("\n\n\t**** Is is impossible to find "+str(NZeros)+" zeros ****\n\n")
                break
            #endif
        #endfor
    elif option==2:
        print("The sine function has the format A*sin(Bx+C)+D")
        print("Enter the A value:")
        while True:
            A=check_format_coefficients("A")
            if A!=0:
                break
            print("Error. The A value may be different of zero.")
        print("Enter the B value: ")
        B=check_format_coefficients("B")
        print("Enter the BCvalue: ")
        C=check_format_coefficients("C")
        print("Enter the D value: ")
        D=check_format_coefficients("D")
        
        for i in range(NZeros):
            for j in range(100):
                x0=start(a, b)
                x_n=newtonRaphson_Sine(A,B,C,D,x0)
                sameZero=False
                for k in range(0,i):
                    delta=abs(x_n-listZeros[k])
                    if (delta<=1e-6):
                        sameZero=True           #Found the same Zero
                        break                   #Get out of the Zero comparison
                    #endif
                #endfor
                if (not(sameZero)):             #Exit the "j" loop
                    break                       #Back to the "i" loop
                #endif
            #endfor
            if (j!=99):
                ZerosFound=ZerosFound+1
                listZeros[i]=x_n                  #New Zero to the list
            else:
                print("\n\n\t**** Is is impossible to find "+str(NZeros)+" zeros ****\n\n")
                break
            #endif
        #endfor
        
    elif option==3:
        print("The Natural log function has the format A*ln(Bx+C)+D")
        print("Enter the A value:")
        while True:
            A=check_format_coefficients("A")
            if A!=0:
                break
            print("Error. The A value may be different of zero.")
        print("Enter the B value: ")
        B=check_format_coefficients("B")
        print("Enter the BCvalue: ")
        C=check_format_coefficients("C")
        print("Enter the D value: ")
        D=check_format_coefficients("D")
        for i in range(NZeros):
            for j in range(100):
                x0=start(a, b)
                x_n=newtonRaphson_log10(A,B,C,D,x0)
                sameZero=False
                for k in range(0,i):
                    delta=abs(x_n-listZeros[k])
                    if (delta<=1e-6):
                        sameZero=True           #Found the same Zero
                        break                   #Get out of the Zero comparison
                    #endif
                #endfor
                if (not(sameZero)):             #Exit the "j" loop
                    break                       #Back to the "i" loop
                #endif
            #endfor
            if (j!=99):
                ZerosFound=ZerosFound+1
                listZeros[i]=x_n                  #New Zero to the list
            else:
                print("\n\n\t**** Is is impossible to find "+str(NZeros)+" zeros ****\n\n")
                break
            #endif
        #endfor
    
    else:
        print("The exponential function has the format Ae^(Bx)+C")
        print("Enter the A value:")
        while True:
            A=check_format_coefficients("A")
            if A!=0:
                break
            print("Error. The A value may be different of zero.")
        print("Enter the B value: ")
        B=check_format_coefficients("B")
        print("Enter the BCvalue: ")
        C=check_format_coefficients("C")
        for i in range(NZeros):
            for j in range(100):
                x0=start(a, b)
                x_n=newtonRaphson_exp(A,B,C,x0)
                sameZero=False
                for k in range(0,i):
                    delta=abs(x_n-listZeros[k])
                    if (delta<=1e-6):
                        sameZero=True           #Found the same Zero
                        break                   #Get out of the Zero comparison
                    #endif
                #endfor
                if (not(sameZero)):             #Exit the "j" loop
                    break                       #Back to the "i" loop
                #endif
            #endfor
            if (j!=99):
                ZerosFound=ZerosFound+1
                listZeros[i]=x_n                  #New Zero to the list
            else:
                print("\n\n\t**** Is is impossible to find "+str(NZeros)+" zeros ****\n\n")
                break
            #endif
        #endfor
    
    A=list(range(ZerosFound))
    for i in range(0,ZerosFound):
        A[i]=list(range(2))
    for i in range(0,ZerosFound):
        A[i][0]=i
        A[i][1]=listZeros[i]
    x=list(range(ZerosFound))
    y=list(range(ZerosFound))
    for i in range(0,ZerosFound):
        x[i]=A[i][1]                #Valor
        y[i]=A[i][0]                #Orden
    sort(ZerosFound,x,y)
    print("\tZeros Sorted:")
    for i in range(0,ZerosFound):
        fila_i=("%12.6f \t %4.0f\r" % (A[i][0],(A[i][1]+1)))
        print(fila_i)
        
    while True:
        Resp=input("Do you want to continue with a new polynomial? (\"S\"/\"N\")\t").upper()
        if Resp=="N":
            sys.exit("*** End of the program ***\n\n")              
            ## Exit program
        if Resp=="S":
            break
            # Exit option loop
        #endif
    #endwhile
##EndWhile