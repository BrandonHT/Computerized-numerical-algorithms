#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: administrador
"""

# Power Method to Find Largest Eigen Value and Eigen Vector
# Importing NumPy Library
import numpy as np
import sys

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


# Making numpy array n x 1 size and initializing to zero
# for storing initial guess vector
x = np.zeros((Filas))

# Reading initial guess vector
print('Ingresa el vector: ')
for i in range(Filas):
    x[i] = float(input( 'x['+str(i)+']='))

# Reading tolerable error
tolerable_error = float(input('Ingrresa el error tolerable: '))

# Reading maximum number of steps
max_iteration = int(input('Ingresa el máximo número de iteraciones: '))

# Power Method Implementation
lambda_old = 1.0
condition =  True
step = 1
while condition:
    # Multiplying a and x
    x = np.matmul(A,x)
    
    # Finding new Eigen value and Eigen vector
    lambda_new = max(abs(x))
    
    x = x/lambda_new
    
    # Displaying Eigen value and Eigen Vector
    print('\nIteración %d' %(step))
    print('----------')
    print('Eigen Value = %0.4f' %(lambda_new))
    print('Eigen Vector: ')
    for i in range(Filas):
        print('%0.3f\t' % (x[i]))
    
    # Checking maximum iteration
    step = step + 1
    if step > max_iteration:
        print('No convergió en el número máximo de iteraciones!')
        break
    
    # Calculating error
    error = abs(lambda_new - lambda_old)
    print('errror='+ str(error))
    lambda_old = lambda_new
    condition = error > tolerable_error