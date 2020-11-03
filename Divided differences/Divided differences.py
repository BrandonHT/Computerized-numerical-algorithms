# -*- coding: utf-8 -*-
"""

@author: cuauh
"""

# Diferencias divididas
#
import sys

## FUNCIONES:
    

# Función que encuentra el término del producto
def proterm(i, value, x): 
	pro = 1; 
	for j in range(i): 
		pro = pro * (value - x[j]); 
	return pro; 

# Calcular la tabla de diferencias dividas
def dividedDiffTable(x, y, n): 

	for i in range(1, n): 
		for j in range(n - i): 
			y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
									(x[j] - x[i + j])); 
	return y; 

# Función para aplicar la fórmula de DD
def applyFormula(value, x, y, n): 

	sum = y[0][0]; 

	for i in range(1, n): 
		sum = sum + (proterm(i, value, x) * y[0][i]); 
	
	return sum; 

# Imprimir la tabla
def printDiffTable(y, n): 

	for i in range(n): 
		for j in range(n - i): 
			print(round(y[i][j], 4), "\t", 
							end = " "); 

		print(""); 
    #endFor
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


##  MAIN

Arch=input("Dame el nombre del archivo con los datos originales: \t")
print(Arch)
try:
        FN = open(Arch,"r")
        print("Se abrió el archivo \""+Arch+"\"" )
except:
        print("No se encontró el archivo \""+Arch+"\"")
        sys.exit("**** Fin de programa ****")
    #endTrydat
Datos=FN.readlines()
NumDatos=len(Datos)
n=NumDatos
FN = open(Arch,"r") 
A=list(range(NumDatos+1))
for i in range(NumDatos+1):
    A[i]=list(range(3))
for i in range(NumDatos):
    Datos[i]=FN.readline()
    for j in range(1,3):
            L=Datos[i]
            Num=getNum(L,j-1)     
            A[i+1][j]=Num
    #endFor
#endFor
x=list(range(NumDatos))
y = [[0 for i in range(10)] 
		for j in range(10)]; 
for i in range(0,NumDatos):
        x[i]=A[i+1][1]
        y[i][0]=A[i+1][2]
    #endFor


# Calcular tabla e imprimirla
ddt=dividedDiffTable(x, y, n); 
print("\n La tabla de diferencias dividas es la siguiente: \n")
printDiffTable(ddt, n); 

# value to be interpolated 
value = input("Dame el valor a interpolar: "); 
value=float(value)
# printing the value 
print("\nEl valor en el punto", value, "es", 
		round(applyFormula(value, x, y, n), 2)) 


