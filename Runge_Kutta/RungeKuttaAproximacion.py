# -*- coding: utf-8 -*-

import math
import sys
import matplotlib.pyplot as plt
import numpy
#from sympy import * 
from d2lssqI import *

#y = Symbol('y')
#t = Symbol('t')
#f = Symbol("f")

def check_int(x):
    while True:
        try:
            x=int(input("\""+x+"\")\t"))
            return x
        except:
            print("Debe ser un número")
#EndFunction
 
def RungeKutta4(f, t0, y0, tf, n):
    tiempo = [0] * (n + 1)
    Ysol = [0] * (n + 1)
    h = (tf - t0) / float(n)
    tiempo[0] = t = t0
    Ysol[0] = y = y0
    for i in range(1, n + 1):
        k1 = h * f(t, y)
        k2 = h * f(t + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(t + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(t + h, y + k3)
        tiempo[i] = t = t0 + i * h
        Ysol[i] = y = y + (k1 + k2 + k2 + k3 + k3 + k4) / 6
    return tiempo, Ysol

#----------------------------------------------------------------------------#
# CÓDIGO PARA HACER LA INTERPOLACIÓN DE UN SISTEMA DE ECUACIONES



while True:
    
    # Sympify convierte una expresión a una variable que se puede utilizar 
    # con sympy
    #y = sympify(input("Ingrese el lado derecho de la ecuación diferencial ordinaria "))
    #print(type(y))
    #print(f"Y: {y}")
    
    # Definir la Ecuación Diferencial Ordinaria a ser resuelta
    
    def function(t, y):
        return t*math.sqrt(y)
    
    print("Indique la condición inicial y(t0) = y0 \t")
    t0 = check_int("t0")
    y0 = check_int("y0")
    print("Indique el tiempo final (tf) de evaluación \t")
    tf = check_int("tf")
    print("Indique el número de pruebas (n) \t")
    n = check_int("n")
    
    RKt, RKy = RungeKutta4(function, t0, y0, tf, n)
    
    
    plt.plot(RKt, RKy)
    plt.title("Solución Aproximada de la Ecuación Diferencial Ordinaria")
    plt.grid(True)
    plt.xlabel("t")
    plt.ylabel("y(t)")
    plt.show()
    
    #Archivo Texto
    OutDat=("ResultadosRungeKutta.txt")
    try:
        FDO = open(OutDat,"w+")
    except:
        print("No se creó el archivo \""+OutDat+"\"")
        sys.exit("**** Fin de programa ****")
    #endTrydat
    
    resultadosT = numpy.array(RKt).T
    resultadosY = numpy.array(RKy).T
    
    for i in range(len(RKt)):
        fila_i = ("%12.6f \t %12.6f \n" % (resultadosT[i], resultadosY[i]))
        FDO.write(fila_i)
    #endfor 
    FDO.close()
    print("Se guardaron los resultados en ResultadosRungeKutta.txt")
    
    #Archivo Excel
    OutDatExcel=input("Dame el nombre del archivo de resultados en Excel (nombre.xls): \t")
    try:
        EXC = open(OutDatExcel,"w+")
    except:
        print("No se creó el archivo \""+OutDatExcel+"\"")
        sys.exit("**** Fin de programa ****")
    #endTrydat
    
    for i in range(len(RKt)):
        fila_i = ("%12.6f \t %12.6f \n" % (resultadosT[i], resultadosY[i]))
        EXC.write(fila_i)
    #endfor 
    EXC.close()
    print("Se guardaron los resultados en \"" + OutDatExcel + "\"")
    
    
    ArchivoInterpolar = "datosT.txt"
    try:
        ARCH = open(ArchivoInterpolar,"w+")
    except:
        print("No se creó el archivo \""+ArchivoInterpolar+"\"")
        sys.exit("**** Fin de programa ****")
    #endTrydat
        
    for j in range(len(RKt)):
        ARCH.write("%s \n" % resultadosT[j])
    ARCH.close()

    # Exportacion de archivo de Interpolacion d2lssq.I.py
    aproximacion(OutDat, ArchivoInterpolar)
    
    while True:
        Resp=input("Desea continuar iterando? (\"S\"/\"N\")\t").upper()
        if Resp=="N":
            print("*** FIN DE PROGRAMA ***\n\n")
            sys.exit()              ## Exit program
        if Resp=="S":
            break                   # Exit option loop
    #endWhile