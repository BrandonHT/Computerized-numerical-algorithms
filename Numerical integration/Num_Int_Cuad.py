# -*- coding: utf-8 -*-

import sys 
import math

def check_format(x):
    while True:
        try:
            x=float(input("\""+x+"\")\t"))
            return x
        except:
            sys.exit("\n\tDEBE SER UN NÚMERO, INTENTE DE NUEVO") ## Exit program
    ##EndWhile
    
def transform(a,b,pol):
    global t1,t2,t3,t4,t5,dt
    dt=(b-a)/2
    if pol == 1:
        t1=(b+a)/2
    
    if pol == 2:
        t1=((b+a)+(b-a)*math.sqrt(1/3))/2
        t2=((b+a)+(b-a)*(-math.sqrt(1/3)))/2
        
    if pol == 3:
        t1=((b+a)+(b-a)*math.sqrt(3/5))/2
        t2=(b+a)/2
        t3=((b+a)+(b-a)*(-math.sqrt(3/5)))/2
        
    if pol == 4:
        t1=((b+a)+(b-a)*-0.861136312)/2
        t2=((b+a)+(b-a)*-0.339981044)/2
        t3=((b+a)+(b-a)*0.339981044)/2
        t4=((b+a)+(b-a)*0.861136312)/2
       
    
    if pol == 5:
        t1=((b+a)+(b-a)*-0.906179846)/2
        t2=((b+a)+(b-a)*-0.538469310)/2
        t3=(b+a)/2
        t4=((b+a)+(b-a)*0.538469310)/2
        t5=((b+a)+(b-a)*0.906179846)/2
        
        
    return
  

def resolve(pol):   
    if pol == 1:
        q1=2
        res=q1*(C2*t1+C1)*dt
    
    if pol == 2:
        q1=1
        res=q1*((C3*t1**2+C2*t1+C1)*dt)+q1*((C3*t2**2+C2*t2+C1)*dt)
         
    if pol == 3:
        q1=5/9
        q2=8/9
        q3=5/9
        res=q1*((C4*t1**3+C3*t1**2+C2*t1+C1)*dt)+q2*((C4*t2**3+C3*t2**2+C2*t2+C1)*dt)+q3*((C4*t3**3+C3*t3**2+C2*t3+C1)*dt)
    
    if pol == 4:
        q1=0.3478548
        q2=0.6521452
        q3=0.6521452
        q4=0.3478548
 
        res=q1*((C5*t1**4+C4*t1**3+C3*t1**2+C2*t1+C1)*dt)+q2*((C5*t2**4+C4*t2**3+C3*t2**2+C2*t2+C1)*dt)+q3*((C5*t3**4+C4*t3**3+C3*t3**2+C2*t3+C1)*dt)+q4*((C5*t4**4+C4*t4**3+C3*t4**2+C2*t4+C1)*dt)
        
    if pol == 5:
        q1=0.2369269
        q2=0.4786287
        q3=0.5688889
        q4=0.4786287
        q5=0.2369269
 
        res=q1*((C6*t1**5+C5*t1**4+C4*t1**3+C3*t1**2+C2*t1+C1)*dt)+q2*((C6*t2**5+C5*t2**4+C4*t2**3+C3*t2**2+C2*t2+C1)*dt)+q3*((C6*t3**5+C5*t3**4+C4*t3**3+C3*t3**2+C2*t3+C1)*dt)+q4*((C6*t4**5+C5*t4**4+C4*t4**3+C3*t4**2+C2*t4+C1)*dt)+q5*((C6*t5**5+C5*t5**4+C4*t5**3+C3*t5**2+C2*t5+C1)*dt)
    return res

global C1,C2,C3,C4,C5,C6

print("\n\tPROPORCIONA EL NÚMERO DE COEFICIENTES DE LA ECUACIÓN DE GRADO:")
pol=check_format("Grado")
if (pol>6):
    sys.exit("\n\tESTA ECUACIÓN SUPERA EL GRADO 6") ## Exit program
#   endif        
if pol == 1:
    print("\n\tPROPORCIONA LOS COEFICIENTES:")
    C1=check_format("c1")
    C2=check_format("c2")
    print("\n\tDA EL VALOR DE LOS INTERVALOS DE INTEGRACIÓN DE a HASTA b:")
    A=check_format("a")
    B=check_format("b")
  
if pol == 2:
    print("\n\tPROPORCIONA LOS COEFICIENTES:")
    C1=check_format("c1")
    C2=check_format("c2")
    C3=check_format("c3")
    print("\n\tDA EL VALOR DE LOS INTERVALOS DE INTEGRACIÓN DE a HASTA b:")
    A=check_format("a")
    B=check_format("b")
    
if pol == 3:
    print("\n\tPROPORCIONA LOS COEFICIENTES:")
    C1=check_format("c1")
    C2=check_format("c2")
    C3=check_format("c3")
    C4=check_format("c4")
    print("\n\tDA EL VALOR DE LOS INTERVALOS DE INTEGRACIÓN DE a HASTA b:")
    A=check_format("a")
    B=check_format("b")
    
if pol == 4:
    print("\n\tPROPORCIONA LOS COEFICIENTES:")
    C1=check_format("c1")
    C2=check_format("c2")
    C3=check_format("c3")
    C4=check_format("c4")
    C5=check_format("c5")
    print("\n\tDA EL VALOR DE LOS INTERVALOS DE INTEGRACIÓN DE a HASTA b:")
    A=check_format("a")
    B=check_format("b")
    
if pol == 5:
    print("\n\tPROPORCIONA LOS COEFICIENTES:")
    C1=check_format("c1")
    C2=check_format("c2")
    C3=check_format("c3")
    C4=check_format("c4")
    C5=check_format("c5")
    C6=check_format("c6")
    print("\n\tDA EL VALOR DE LOS INTERVALOS DE INTEGRACIÓN DE a HASTA b:")
    A=check_format("a")
    B=check_format("b")

transform(A,B,pol)
x=resolve(pol)
print ("\nEL ÁREA BAJO LA CURVA DE LA INTEGRAL ES: ", x)    
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
