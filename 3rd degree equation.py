#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 22:41:36 2020

@author: brandonhdz
"""

#   THIS PROGRAM SOLVES FOR THE THREE ROOTS OF A 3RD
#   DEGREE EQUATION
#       aX^3+BX^2+CX+D
#
import math
import sys
a=input("Deme el valor de \"a\"\t")
a=float(a)
print("El valor de \"a\" es "+str(a))
b=input("Deme el valor de \"b\"\t")
b=float(b)
print("El valor de \"b\" es "+str(b))
c=input("Deme el valor de \"c\"\t")
c=float(c)
print("El valor de \"c\" es "+str(c))
d=input("Deme el valor de \"d\"\t")
d=float(d)
print("El valor de \"d\" es "+str(d))

m=(3*a*c-(b**2))/(3*(a**2))
n=(2*(b**3)-(9*a*b*c)+(27*(a**2)*d))/(27*(a**3))

n2=(n**2)/4
m3=(m**3)/27

disc=n2+m3

print("\nEl valor del discriminante es "+str(disc))

if (disc>=0):
    aux1=(-(n/2)+(disc**0.5))
    aux2=(-(n/2)-(disc**0.5))
    sigAux1=+1
    sigAux2=+1
    if(aux1<0):
    	sigAux1=-1
    if(aux2<0):
    	sigAux2=-1
    aux1=abs(aux1)**0.33
    aux2=abs(aux2)**0.33
    aux1*=sigAux1
    aux2*=sigAux2
    y1=aux1+aux2
else:
    aux1=(-(n/2)*((-27/(m**3))**0.5))
    aux2=(1/3)*(math.acos(aux1))
    aux3=math.cos(aux2)
    y1=2*((-m/3)**0.5)*aux3

x1=y1-(b/(3*a))

aux=((((a*x1)+b)**2)-(4*a*(a*(x1**2)+b*x1+c)))**0.5
x2=-((a*x1+b)+aux)/(2*a)
x3=-((a*x1+b)-aux)/(2*a)

print("\n***\t\"X1\"= %8.4f  %8.4f" % (x1.real,x1.imag))
print("\n***\t\"X2\"= %8.4f  %8.4f" % (x2.real,x2.imag))
print("\n***\t\"X3\"= %8.4f  %8.4f" % (x3.real,x3.imag))

Comprueba1=a*x1**3+b*x1**2+c*x1+d
Comprueba2=a*x2**3+b*x2**2+c*x2+d
Comprueba3=a*x3**3+b*x3**2+c*x3+d

print(" Comprobación:\n\t#1:\t"+str(Comprueba1)+"\n\t#2:\t"+str(Comprueba2)+"\n\t#3:\t"+str(Comprueba3))


CompruebaTotal=Comprueba1+Comprueba2+Comprueba3
if CompruebaTotal.real>0.000001:
    print(" Comprobación global:\n\t"+str(CompruebaTotal.real))
