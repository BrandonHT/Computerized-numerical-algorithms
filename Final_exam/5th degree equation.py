﻿import math
import sys
import cmath

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
    print("Dame el grado del polinomio que deseas crear:")
    while True:
        grado=check_format("Grade")
        if(grado>=2 and grado<=5):
            break
        #endif
        print("Error, it may be, at least, a second degree and less or equals than 5 degree")
    #endwhile
    if grado==2:
        a=input("Deme el valor de \"a\"\t")
        a=float(a)
        print("El valor de \"a\" es "+str(a))
        b=input("Deme el valor de \"b\"\t")
        b=float(b)
        print("El valor de \"b\" es "+str(b))
        c=input("Deme el valor de \"c\"\t")
        c=float(c)
        print("El valor de \"c\" es "+str(c))
        Disc=b**2-4*a*c
        #sys.exit()
        print("\nEl valor del discriminante es "+str(Disc))
        sqDisc=Disc**0.5
        #
        #   NOTAR QUE sq2=math.sqrt(Disc) NO ACEPTA ARGUMENTOS NEGATIVOS
        #   PERO Disc**0.5 SÍ
        #
        X1=(-b+sqDisc)/(2*a)
        print("\n***\t\"X1\"= %8.4f  %8.4f" % (X1.real,X1.imag))
        X2=(-b-sqDisc)/(2*a)
        print("\n***\t\"X2\"= %8.4f  %8.4f" % (X2.real,X2.imag))
        Comprueba1=a*X1**2+b*X1+c
        Comprueba2=a*X2**2+b*X2+c
        print(" Comprobación:\n\t#1:\t"+str(Comprueba1)+"\n\t#2:\t"+str(Comprueba2))
        CompruebaTotal=Comprueba1+Comprueba2
        if CompruebaTotal.real>0.000001:
            print(" Comprobación global:\n\t"+str(CompruebaTotal.real))
    if grado==3:
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
    if grado==4:
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
    if grado==5:
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
