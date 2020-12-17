#
import math
import sys
import random

# F(x)=2*sen**2(x-3)-1    -10,+10

def check_format(x):
    while True:
        try:
            x=float(input("\""+x+"\")\t"))
            return int(x)
        except:
            print("Debe ser un número")
            print("Intente de nuevo")
    ##EndWhile
##EndFunction
    
def sgn(x):
    if (x>=0):
        return +1
    else:
        return -1
    #endif
    
def SetLimits():
    global less,more
    r1=random.uniform(-10,+10)
    r2=random.uniform(-10,+10)
    if (r1<r2):
        less=r1
        more=r2
    else:
        less=r2
        more=r1
    #endif
    return

def Seno(F,DI,DE,x):
    Fx=math.sin(x+DI)
    Fx=Fx*Fx*F+DE
    return Fx

def Bisect(F,DI,DE,lower,upper):
    a_n=lower
    b_n=upper
    r_n_1=1e+6
    while True:
        r_n=(a_n+b_n)/2
        f_r=Seno(F,DI,DE,r_n)
        f_a=Seno(F,DI,DE,a_n)
        if (abs(r_n-r_n_1)<1e-10)or(f_r==0):
            return r_n
        #endif
        if (sgn(f_r)==sgn(f_a)):
            a_n=r_n
        else:
            b_n=r_n
        #endif
        r_n_1=r_n
    #enddo
    return
#
#   MAIN
#
# F(x)=F*sen**2(x+DI)+DE    -10,+10
while True:
    print("Cuántos ceros desea encontrar")
    NZeros=0
    while True:
        NZeros=check_format("NZeros")
        if (((NZeros>=2)and(NZeros<=20))):
            break
        #endif
    #endif
    lista=[]
    for i in range(0,NZeros):
        lista.append(0)
    #endFor
    print("\n\tPROPORCIONA EL FACTOR Y EL DESPLAZAMIENTO INTERNO Y EXTERNO")
    print("Proporciona el Factor")
    F=check_format("F")
    print("Proporciona el desplazamiento interno")
    DI=check_format("DI")
    print("Proporciona el desplazamiento externo")
    DE=check_format("DE")
    ZerosFound=0
    for i in range(0,NZeros):
        for j in range(0,100):              ## Up to 100 attempts to set the limits
            SetLimits()
            X=Bisect(F,DI,DE,less,more)
            Fx=F*math.sin(X+DI)**2+DE
            if (abs(Fx)>=1e-06):
                continue   #Not a Zero; try another configuration
            #endif
#
#               IT IS A ZERO
#
            sameZero=False
            for k in range(0,i):
                delta=abs(X-lista[k])
                if (delta<=1e-6):
                    sameZero=True           #Found the same Zero
                    break                   #Get out of the Zero comparison
                #endif
            #endfor
            if (not(sameZero)):             #Exit the "j" loop
                break                       #Back to the "i" loop
            #endif
        #endfor
        if (j!=99):
            ZerosFound=ZerosFound+1
            lista[i]=X                     #New Zero to the list
        else:
            print("\n\n\t**** Imposible encontrar "+str(NZeros)+" ceros ****\n\n")
            break
        #endif
    #endfor
    while True:
        print("\t"+str(ZerosFound)+" ceros encontrados:\n")
        for i in range(0,ZerosFound):
            print(str(i+1)+") "+str(lista[i]))
        #endfor
        Resp=input("Desea continuar iterando? (\"S\"/\"N\")\t").upper()
        if Resp=="N":
            sys.exit("*** FIN DE PROGRAMA ***\n\n")              ## Exit program
        if Resp=="S":
            break                   # Exit option loop
    #endWhile
##ENDWHILE
