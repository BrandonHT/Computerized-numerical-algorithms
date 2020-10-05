#
#   EJEMPLO DE COEFICIENTES:
#   F=2, DI=-3, DI=-0.5
#
import sys
import random
import math

#   n is the number of data points
#   x holds the independent data variable´s values
#       Values of the zeros
#   y holds the dependent data variable´s values
#       Original production sequence
#   ON OUTPUT:
#   array x is sorted from smallest to largest
#
def sort(n,x,y):
    for i in range(0,n-1):
        tmin=x[i]
        imin=i
        for j in range(i+1,n):
            if (tmin>x[j]):
                tmin=x[j]
                imin=j
            #endIf
        #endFor
        if (imin!=i):
            x[imin]=x[i]
            x[i]=tmin
            tmin=y[imin]
            y[imin]=y[i]
            y[i]=tmin
        #endIf
    #endFor
    for i in range(0,n):
        A[i][0]=x[i]
        A[i][1]=y[i]
    #endFor
    return
#endSort

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
    
def sgn(x):
    if (x>=0):
        return +1
    else:
        return -1
    #endif
    
def SetLimits():
    global less,more
    r1=random.uniform(-20,+20)
    r2=random.uniform(-20,+20)
    if (r1<r2):
        less=r1
        more=r2
    else:
        less=r2
        more=r1
    #endif
    return

def SenCos(F,DI,DE,x):
    Fx=F*math.sin(x+DI)*math.cos(x+DI)+DE
    return Fx

def Bisect(F,DI,DE,lower,upper):
    a_n=lower
    b_n=upper
    r_n_1=1e+6
    while True:
        r_n=(a_n+b_n)/2
        f_r=SenCos(F,DI,DE,r_n)
        f_a=SenCos(F,DI,DE,a_n)
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
while True:
    print("Cuántos ceros desea encontrar")
    NZeros=0
    while True:
        NZeros=check_format("NZeros")
        NZeros=int(NZeros)
        if (((NZeros>=2)and(NZeros<=40))):
            break
        #endif
    #endif
    lista=[]
    for i in range(0,NZeros):
        lista.append(0)
    #endFor
    print("\n\tPROPORCIONA LOS PARÁMETROS DE F*SIN(X+DI)*COS(X+DI)+DE")
    print("F")
    F=check_format("F")
    print("DI")
    DI=check_format("DI")
    print("DE")
    DE=check_format("DE")
    ZerosFound=0
    for i in range(0,NZeros):
        for j in range(0,100):               # Up to 100 attempts to set the limits
            SetLimits()			              # return <less,more>
            X=Bisect(F,DI,DE,less,more)
            Fx=SenCos(F,DI,DE,X)
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
    print("\n\t**** Se econtraron "+str(ZerosFound)+" ceros **** \n\n")
    print(" <ENTER> para continuar...")
    cont=input("\n")
    print("\n\t**** VERIFICACIÓN ****\n")
#   print(123456789ABC\t1234
    print("      Cero          F(Cero)   ")
    print("      ----         ---------")
    for i in range(0,ZerosFound):
       Fx=SenCos(F,DI,DE,lista[i])
       fila_i=("%12.6f \t %12.8f\r" % (lista[i],Fx))
       print(fila_i)
    #endfor
    A=list(range(ZerosFound))
    for i in range(0,ZerosFound):
        A[i]=list(range(2))
    for i in range(0,ZerosFound):
        A[i][0]=i
        A[i][1]=lista[i]
    x=list(range(ZerosFound))
    y=list(range(ZerosFound))
    for i in range(0,ZerosFound):
        x[i]=A[i][1]                #Valor
        y[i]=A[i][0]                #Orden
    sort(ZerosFound,x,y)
    print("\n\t**** CEROS ORDENADOS ****\n")
    for i in range(0,ZerosFound):
        fila_i=("%12.6f \t %4.0f\r" % (A[i][0],(A[i][1]+1)))
        print(fila_i)
    #endfor
    ArchOut=input("Dame el nombre del archivo a escribir: \t")
    print(ArchOut)
    try:
        FN = open(ArchOut,"w+")
        print("Se creó el archivo \""+ArchOut+"\"" )
    except:
        print("No se creó el archivo \""+ArchOut+"\"")
        sys.exit("**** Fin de programa ****")
    #endTry
    for i in range(0,ZerosFound):
        fila_i=("%8.4f \t %8.4f\r" % (A[i][0],(A[i][1]+1)))
        FN.write(fila_i)
    #endfor
    FN.close()
    while True:
        Resp=input("Desea continuar iterando? (\"S\"/\"N\")\t").upper()
        if Resp=="N":
            sys.exit("*** FIN DE PROGRAMA ***\n\n")              ## Exit program
        if Resp=="S":
            break                   # Exit option loop
        #endif
    #endwhile
#endWhile
