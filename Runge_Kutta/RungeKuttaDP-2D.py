# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 23:21:34 2020

@author: SOFIA
"""

import matplotlib.pyplot as plt
import numpy
import sys 

def check_int(x):
    while True:
        try:
            x=int(input("\""+x+"\")\t"))
            return x
        except:
            print("Debe ser un número")
            print("Intente de nuevo")
    ##EndWhile
##EndFunction
 
def check_float(x):
    while True:
        try:
            x=float(input("\""+x+"\")\t"))
            return x
        except:
            print("Debe ser un número")
            print("Intente de nuevo")
    ##EndWhile
##EndFunction

def RungeKutta2D(y, t, h):                    #edited; no need for input f
        """ Runge-Kutta 4 method """
        k1 = h*f(t, y)
        k2 = h*f(t+0.5*h, y+0.5*k1)
        k3 = h*f(t+0.5*h, y+0.5*k2)
        k4 = h*f(t+h, y+k3)
        return (k1 + 2*k2 + 2*k3 + k4)/6

def f(t, y):
        alpha = 1.1
        beta = 0.4
        gamma = 0.4
        delta = 0.1
        x1, x2 = y[0], y[1]
        fxd = x1*(alpha - beta*x2)
        fyd = -x2*(gamma - delta*x1)
        return numpy.array([fxd, fyd], float)


    
while True: 
    print("Indique el tiempo inicial (t0) \t")
    t0 = check_int("t0")
    print("Indique el tiempo final (tf) \t")
    tf = check_int("tf")
    print("Indique la condiciones iniciales y(t0) = [y0a y0b] \t")
    a = check_int("y0a")
    b = check_int("y0b")
    y0 = numpy.array([a, b], float)
    print("Indique el número de step (h) \t")
    h = check_float("h")
    
    time = numpy.arange(t0, tf, h)
    ec1, ec2  = [], []
    
    for t in time:
            ec1.append(y0[0])          #edited
            ec2.append(y0[1])          #edited
            y0 += RungeKutta2D(y0, t, h)             #edited; no need for input f
    
    plt.subplot(1, 2, 1)
    plt.plot(time, ec1, "r", label="Presas")
    plt.plot(time, ec2, "b", label="Depredadores")
    plt.grid(True)
    plt.xlabel("t")
    plt.ylabel("y(t)")
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(ec1, ec2)
    plt.grid(True)
    plt.xlabel("Presas")
    plt.ylabel("Depredadores")
    
    plt.show()
    
    while True:
        Resp=input("Desea continuar iterando? (\"S\"/\"N\")\t").upper()
        if Resp=="N":
            print("*** FIN DE PROGRAMA ***\n\n")
            sys.exit()              ## Exit program
        if Resp=="S":
            break                   # Exit option loop
    #endWhile