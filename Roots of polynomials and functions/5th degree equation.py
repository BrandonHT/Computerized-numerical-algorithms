#   THIS IS AN EXAMPLE OF HOW FLOATING POINT IMPRECISION
#       WHEN COEFFICIENTS ARE ALL =0 A NEGATIVE "NEAR ZERO"
#       CAUSES THE PROGARM TO CRASH!!!
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
        return math.pow(x,1/3)
    else:
        return -math.pow(-x,1/3)
#EndFunction

def solve4(aa,bb,cc,dd,ee):  
    global X1,X2,X3,X4
    a=bb/aa
    b=cc/aa
    c=dd/aa
    d=ee/aa
    #
    a3=-1
    b3=b
    c3=4*d-a*c
    d3=(a**2)*d-4*b*d+c**2
    #
    m=(3*a3*c3-b3**2)/(3*(a3**2))
    n=(2*(b3**3)-9*a3*b3*c3+27*(a3**2)*d3)/(27*(a3**3))
    disc3=(n**2)/4+(m**3)/27
    if (disc3>=0):
        u=cubic_root(-n/2+math.sqrt(disc3))
        v=cubic_root(-n/2-math.sqrt(disc3))
        y=u+v
    else:
        u=math.acos((-n/2)*math.sqrt(-27/m**3))
        y=2*math.sqrt(-m/3)*math.cos(u/3)
    #endif
    r=y-(b3/(3*a3))
#
    t1=math.sqrt((a*a)/4-b+r)
    t2=math.sqrt((r*r)/4-d)
    bb12=a/2-t1
    cc12=r/2-t2
    delta12=bb12**2-4*cc12
    X1=(-bb12+(delta12)**0.5)/2
    X2=(-bb12-(delta12)**0.5)/2
    #
    bb34=a/2+t1
    cc34=r/2+t2
    delta34=bb34**2-4*cc34
    X3=(-bb34+(delta34)**0.5)/2
    X4=(-bb34-(delta34)**0.5)/2
    return

def Poly5(a,b,c,d,e,f,X):
    Fx=f+X*(e+X*(d+X*(c+X*(b+X*(a)))))
    return Fx

def Bisect(a,b,c,d,e,f,upper,lower):
    a_n=lower
    b_n=upper
    r_n_1=1e+6
    while True:
        r_n=(a_n+b_n)/2
        if (abs(r_n-r_n_1)<1e-10):
            return r_n
#   	endif
        f_r=Poly5(a,b,c,d,e,f,r_n)
        f_a=Poly5(a,b,c,d,e,f,a_n)*f_r
        if (f_a>=0):
            a_n=r_n
#       endif
        f_b=Poly5(a,b,c,d,e,f,b_n)*f_r
        if (f_b>=0):
            b_n=r_n
#       endif
        r_n_1=r_n
    #enddo
    return

while True:
    print("\n\tPROPORCIONA LOS 6 COEFICIENTES DE LA ECUACIÓN DE GRADO 5:")
    aa=check_format("a")
    if (aa==0):
        sys.exit("\n\tESTA NO ES UNA ECUACIÓN DE 5o GRADO!!!!!") ## Exit program
#   endif        
    bb=check_format("b")
    cc=check_format("c")
    dd=check_format("d")
    ee=check_format("e")
    ff=check_format("f")
    X5=Bisect(aa,bb,cc,dd,ee,ff,+128,-128)
    r=X5
    a=aa
    b=aa*r+bb
    c=aa*r**2+bb*r+cc
    d=aa*r**3+bb*r**2+cc*r+dd
    e=aa*r**4+bb*r**3+cc*r**2+dd*r+ee
    solve4(a,b,c,d,e)  
    print("X1 = %12.6f %12.6f" % (X1.real,X1.imag))
    print("X2 = %12.6f %12.6f" % (X2.real,X2.imag))
    print("X3 = %12.6f %12.6f" % (X3.real,X3.imag))
    print("X4 = %12.6f %12.6f" % (X4.real,X4.imag)) 
    print("X5 = %12.6f %12.6f" % (X5.real,X5.imag))
    while True:
        Resp=input("Verifica resultados? (\"S\"/\"N\")\n").upper()
        if Resp=="N":
            break
        if Resp!="S":
            continue
        F1=aa*X1**5+bb*X1**4+cc*X1**3+dd*X1**2+ee*X1+ff
        print("F(X1) = %12.6f %12.6f" % (F1.real,F1.imag))
        F2=aa*X2**5+bb*X2**4+cc*X2**3+dd*X2**2+ee*X2+ff
        print("F(X2) = %12.6f %12.6f" % (F2.real,F2.imag))
        F3=aa*X3**5+bb*X3**4+cc*X3**3+dd*X3**2+ee*X3+ff
        print("F(X3) = %12.6f %12.6f" % (F3.real,F3.imag))
        F4=aa*X4**5+bb*X4**4+cc*X4**3+dd*X4**2+ee*X4+ff
        print("F(X4) = %12.6f %12.6f" % (F4.real,F4.imag))
        F5=aa*X5**5+bb*X5**4+cc*X5**3+dd*X5**2+ee*X5+ff
        print("F(X5) = %12.6f %12.6f" % (F5.real,F5.imag))
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
