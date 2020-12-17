#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: administrador
"""

import numpy as np
import sys
from numpy import linalg as LA


def NumCols(Linea,Linelen):
    cols=1
    for i in range(0,LineLen):
        if (Linea[i]=="\t"):
            cols=cols+1
        #endIf
    #endFor
    return cols
#endFunction

def getNum(Linea,numVar):
    countVar=-1
    first=0
    for i in range(0,numVar+1):
        x=""
        for j in range(first,len(Linea)):
            if (Linea[j]=="\t" or Linea[j]=="\n"):
                first=j+1
                countVar=countVar+1
                break
            else:
                x=x+Linea[j]
            #endif
        #endFor
        if (countVar==numVar):
            return float(x)
        #endIf
    #endFor
#endFunction

Arch=input("Deme el nombre del ARCHIVO DE DATOS A ANALIZAR: \t")
try:
    FN = open(Arch,"r")
    print("\t*** Se abrió el archivo \""+Arch+"\"" )
except:
    print("\t*** No se encontró el archivo \""+Arch+"\"")
    sys.exit("**** Fin de programa ****")
    
lista = list(range(0))
lista=FN.readlines()
Filas=len(lista)
print("Filas: "+str(Filas))
FN = open(Arch,"r") 
Lineas=list(range(Filas))
Lineas[0]=FN.readline()
LineLen=len(Lineas[0])
Columnas=NumCols(Lineas[0],LineLen)
print("Columnas: "+str(Columnas))
if (Columnas!=Filas):
    print("El número de filas de ser igual al número de columnas")
    print("**** \tFin de Programa ****\n\n\n")
    sys.exit()

FN = open(Arch,"r") 
A=np.zeros((Filas,Filas))
for i in range(0,Filas):
    A[i]=list(range(Columnas))
for i in range(0,Filas):
    Lineas[i]=FN.readline()
    for j in range(0,Columnas):
        L=Lineas[i]
        Num=getNum(L,j)     #j-th variablesin i-th line
        A[i][j]=Num
    #endFor
#endFor    

print("\tMatriz de datos:")
print(A)
w,v=LA.eig(A)
print("\nEigenvalores = n")
print(w)
print("\nEigenvectores = u")
print(v)
print("\n")

print("comprobamos que si se cumpla la ecuación An = nu")
for i in range(0,Filas):
    u=v[:,i]
    lam=w[i]
    print("\nEigenvalor en la casilla "+str(i+1)+":  "+str(lam)+"\n")
    print(" Matriz por el Eigenvector (An):")
    print(np.dot(A,u))
    print(" Eigenvalor por el Eigenvector (nu)")
    print(lam*u)
    print("-------------------------")



               









