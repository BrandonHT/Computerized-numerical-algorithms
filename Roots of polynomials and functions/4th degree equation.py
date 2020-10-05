#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 18:50:48 2020

@author: brandonhdz
"""
#   THIS PROGRAM SOLVES FOR THE FOUR ROOTS OF A FOURTH
#   DEGREE EQUATION
#       aX^4+bX^3+cX^2+dX+e
#
#   WITH LOOP USING "WHILE"
#   USE EXCEPTION HANDLING
#
#   USE A FUNCTION
#
#   FORMAT THE OUTPUT
#
#   math.pow(X,1/3.) VARIATION
#
#   RESULTS VERIFICATION
#
#   SALIDA DEL SISTEMA
#
import math
import cmath
import sys

def check_format(x):
    while True:
        try:
            x=float(input("\""+x+"\")\t"))
            return x
        except:
            print("Debe ser un número")
            print("Intente de nuevo")
    ##EndWhile
##EndFunction
    
def cubic_root(x):
    if (x>=0):
        return x**0.33
    else:
        return (-1)*(abs(x)**0.33)
#EndFunction
    
while True:
    print("\n\tPROPORCIONA LOS 5 COEFICIENTES DE LA ECUACIÓN DE GRADO 4:")
    aa=check_format("a")
    if (aa==0):
        sys.exit("\n\tESTA NO ES UNA ECUACIÓN DE 4o GRADO!!!!!") ## Exit program
#   endif        
    bb=check_format("b")
    cc=check_format("c")
    dd=check_format("d")
    ee=check_format("e")
    #
    a=float(bb/aa)
    b=float(cc/aa)
    c=float(dd/aa)
    d=float(ee/aa)
    #
    a3=-1.0
    b3=b
    c3=float(4*d-a*c)
    d3=float((a**2)*d-4*b*d+c**2)
    #

    m=(3*a3*c3-(b3**2))/(3*(a3**2))
    n=(2*(b3**3)-(9*a3*b3*c3)+(27*(a3**2)*d3))/(27*(a3**3))
    #
    
    n2=(n**2)/4
    m3=(m**3)/27
    
    disc3=n2+m3
    print("\tD3 %8.4f" % (disc3))
    if (disc3>=0):
        u=cubic_root((-n/2)+(disc3**0.5))
        v=cubic_root((-n/2)-(disc3**0.5))
        y=u+v
    else:
        u=(1/3)*(math.acos((-n/2)*((-(27/(m**3)))**0.5)))
        y=2*((-m/3)**0.5)*math.cos(u)
    #endif
    r=y-(b3/(3*a3))
    
    #
    t1=(((a**2)/4)-b+r)**0.5
    t2=(((r**2)/4)-d)**0.5
    bb12=a/2-t1
    cc12=r/2-t2
    delta12=(bb12**2)-(4*cc12)
    
    if(delta12<0):
        X1=complex(-bb12,(delta12**0.5).imag)/2
        print("X1 = %8.4f %8.4f" % (X1.real,X1.imag))
        X2=complex(-bb12,(-1.0)*((delta12)**0.5).imag)/2
        print("X2 = %8.4f %8.4f" % (X2.real,X2.imag))
    else:
        X1=(-bb12+(delta12)**0.5)/2
        print("X1 = %8.4f %8.4f" % (X1.real,X1.imag))
        X2=(-bb12-(delta12)**0.5)/2
        print("X2 = %8.4f %8.4f" % (X2.real,X2.imag))
    #
    bb34=a/2+t1
    cc34=r/2+t2
    delta34=bb34**2-4*cc34
    if(delta34<0):
        X3=(-bb34+cmath.sqrt(delta34))/2
        print("X3 = %8.4f %8.4f" % (X3.real,X3.imag))
        X4=(-bb34-cmath.sqrt(delta34))/2
        print("X4 = %8.4f %8.4f" % (X4.real,X4.imag))
    else:  
        X3=(-bb34+(delta34)**0.5)/2
        print("X3 = %8.4f %8.4f" % (X3.real,X3.imag))
        X4=(-bb34-(delta34)**0.5)/2
        print("X4 = %12.6f %12.6f" % (X4.real,X4.imag))
#    sys.exit()
    while True:
        Resp=input("Verifica resultados? (\"S\"/\"N\")\n").upper()
        if Resp=="N":
            break
        if Resp!="S":
            continue
        F1=aa*X1*X1*X1*X1+bb*X1*X1*X1+cc*X1*X1+dd*X1+ee
        print("F(X1) = %12.6f %12.6f" % (F1.real,F1.imag))
        F2=aa*X2*X2*X2*X2+bb*X2*X2*X2+cc*X2*X2+dd*X2+ee
        print("F(X2) = %12.6f %12.6f" % (F2.real,F2.imag))
        F3=aa*X3*X3*X3*X3+bb*X3*X3*X3+cc*X3*X3+dd*X3+ee
        print("F(X3) = %12.6f %12.6f" % (F3.real,F3.imag))
        F4=aa*X4*X4*X4*X4+bb*X4*X4*X4+cc*X4*X4+dd*X4+ee
        print("F(X4) = %12.6f %12.6f" % (F4.real,F4.imag))
        break
    #endWhile
    while True:
        Resp=input("Desea continuar iterando? (\"S\"/\"N\")\t").upper()
        if Resp=="N":
            sys.exit("*** FIN DE PROGRAMA ***\n\n")              ## Exit program
        if Resp=="S":
            break                   # Exit option loop
    #endWhile
##ENDWHILE
