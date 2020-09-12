#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 23:38:01 2020

@author: brandonhdz
"""
import math
import random
import sys

# F(x) = Any polynomial of grade 10 or less between the range -10,+10

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

def check_format(x):
    while True:
        try:
            x=float(input("\""+x+"\")\t"))
            return int(x)
        except:
            print("May be a number")
            print("Please try again")
    ##EndWhile
##EndFunction
    
def sgn(x):
    if (x>=0):
        return +1
    else:
        return -1
    #endif
    
def SetLimits():
    global less,more
    r1=random.uniform(-10,+10)
    r2=random.uniform(-10,+10)
    if (r1<r2):
        less=r1
        more=r2
    else:
        less=r2
        more=r1
    #endif
    return

def poly(polinomio,x):
    Fx=0
    for i in range(len(polinomio)):
        Fx=Fx+polinomio[i]*(x**(len(polinomio)-1-i))
    return Fx

def Bisect(polinomio,lower,upper):
    a_n=lower
    b_n=upper
    r_n_1=1e+6
    while True:
        r_n=(a_n+b_n)/2
        f_r=poly(polinomio,r_n)
        f_a=poly(polinomio,a_n)
        if (abs(r_n-r_n_1)<1e-10)or(f_r==0):
            return r_n
        #endif
        if (sgn(f_r)==sgn(f_a)):
            a_n=r_n
        else:
            b_n=r_n
        #endif
        r_n_1=r_n
    #enddo
    return

#
#   MAIN
#
# F(x)=F*sen**2(x+DI)+DE    -10,+10
while True:
    print("Please input the grade of the polynomial you want to create")
    while True:
        grado=check_format("Grade")
        if(grado>=1):
            break
        #endif
        print("Error, it may be, at least, a first degree")
    #endwhile
    polinomio=[0]*(grado+1)
    for i in range((grado+1)):
        print("Input the coefficient of the grade ",(grado-i), " of the polynomial")
        texto="Grade "+str((grado-i))
        polinomio[i]=check_format(texto)
    #endfor
    print("Input the number of roots you want to find")
    NZeros=0
    while True:
        NZeros=check_format("NZeros")
        if (((NZeros>=1)and(NZeros<=20))):
            break
        #endif
    #endwhile
    lista=[0]*NZeros
    ZerosFound=0
    for i in range(0,NZeros):
        for j in range(0,100):               # Up to 100 attempts to set the limits
            SetLimits()			              # return <less,more>
            X=Bisect(polinomio,less,more)
            Fx=poly(polinomio,X)
            if (abs(Fx)>=1e-06):
                continue   #Not a Zero; try another configuration
            #endif
#
#               IT IS A ZERO
#
            sameZero=False
            for k in range(0,i):
                delta=abs(X-lista[k])
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
            lista[i]=X                     #New Zero to the list
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
        A[i][1]=lista[i]
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
    #endfor
    ArchOut=input("Give me the name of the file to save the results: \t")
    print(ArchOut)
    try:
        FN = open(ArchOut,"w+")
        print("The file was created sucessfully \""+ArchOut+"\"" )
    except:
        print("The file was not created sucessfully \""+ArchOut+"\"")
        sys.exit("**** End of the program ****")
    #endTry
    for i in range(0,ZerosFound):
        fila_i=("%8.4f \t %8.4f\r" % (A[i][0],(A[i][1]+1)))
        FN.write(fila_i)
    #endfor
    FN.close()
    while True:
        Resp=input("Do you want to continue with a new polynomial? (\"S\"/\"N\")\t").upper()
        if Resp=="N":
            sys.exit("*** End of the program ***\n\n")              ## Exit program
        if Resp=="S":
            break                   # Exit option loop
        #endif
    #endwhile
#endWhile