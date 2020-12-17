"""
        SPLINES.Sort.7
        
   Lee el nombre del archivo
       Determina el número de líneas
       Determina el número de columnas
   Convierte los datos (ASCII) en flotantes
   Declara una matriz y la llena
   Hace un sort
   Escribe el archivo con los datos ordenados
   Encuentra las segundas derivadas
   Lee un archivo de datos
   Lo interpola
   Escribe los resultados en un pseudo-xls

"""
import sys
import random

#   n is the number of data points
#   x holds the independent data variable´s values
#   y holds the dependent data variable´s values
#   ON OUTPUT:
#   array x is sorted from smallest to largest
#
def sort(n,x,y):
    for i in range(1,n):
        tmin=x[i]
        imin=i
        for j in range(i+1,n+1):
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
    for i in range(1,n+1):
        A[i][1]=x[i]
        A[i][2]=y[i]
    #endFor
    return
#endSort

def SpCoef(n):
# This subroutine calculates the values of the coefficients for the spline.
#     on input:
# n is the number of data points
# x holds the independent variable’spoints to be interpolated
# y holds the dependent variable’s points to be interpolated
#     on output:
#- s is the vector where the coefficients are stored
#- sig and tau are auxiliary stores of size n
    sig[2]=0.  
    tau[2]=0.  
    for i in range(2,n):
        Him1=x[i]-x[i-1]
        Hi=x[i+1]-x[i]  
        if (Hi==0):
            print("Dos valores de \"x\" son iguales!!!")
            while True:
                Resp=input("Desea estabilizar (S/N)").upper()
                if Resp!="S" and Resp!="N":
                    continue
                #endIf
                if Resp=="N":
                    sys.exit()
                #endIf
                for j in range(i,n):
                    if x[j]==0:
                        x[j]=x[j]*random.random()*0.00001
                    else:
                        x[j]=x[j]*(1+random.random()*0.00001)
                    #endIf
                #endFor
                break
            #endWhile
            return
        #endIf
        temp=(Him1/Hi)*(sig[i]+2)+2. 
        sig[i+1]=-1/temp
        d=6*((y[i+1]-y[i])/Hi-(y[i]-y[i-1])/Him1)/Hi  
        tau[i+1]=(d-Him1*tau[i]/Hi)/temp  
    #endfor  
    s[1]=0  
    s[n]=0  
    for i in range(1,n-1):  
       ib=n-i
       s[ib]=sig[ib+1]*s[ib+1]+tau[ib+1]  
    #endfor
    print("\nValores de las segundas derivadas:")
    for i in range(1,n+1):
        print("\ts(%3.0f)\t%10.6f))" % (float(i),s[i]))
    #endfor
    return  
#endSPcoef
    
def Spline(n,alfa):
    for i in range(2,n+1):
        if (alfa<=x[i]):
            break
        #endif
    #endfor
    i=i-1
    a=x[i+1]-alfa
    b=alfa-x[i]
    hi=x[i+1]-x[i]
    beta=a*s[i]*(a*a/hi-hi)/6+b*s[i+1]*(b*b/hi-hi)/6+(a*y[i]+b*y[i+1])/hi
    return beta
#endSpline
    
def NumCols(Linea,Linelen):
    cols=1
    for i in range(0,DatoLen):
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

print("****")
print("    **** Empieza el programa ****")
print("****")
while True:
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
    print("Filas: "+str(NumDatos))
    FN = open(Arch,"r")  # REWIND
    DatoLen=len(Datos[0])
    Columnas=NumCols(Datos[0],DatoLen)
    print("Columnas: "+str(Columnas))
    if (Columnas!=2):
        print("El número de columnas debe ser = 2!!!")
        print("\n**** FIN DE PROGRAMA ****\n")
        sys.exit()
    #endif
    FN = open(Arch,"r")             # REWIND
    A=list(range(NumDatos+1))
    for i in range(NumDatos+1):
        A[i]=list(range(3))
    for i in range(NumDatos):
        Datos[i]=FN.readline()
        for j in range(1,3):
            L=Datos[i]
            Num=getNum(L,j-1)     #j-th variablesin i-th line
            A[i+1][j]=Num
        #endFor
    #endFor
    B=list(range(NumDatos+1))
    for i in range(NumDatos+1):
        B[i]=list(range(3))
    for i in range(NumDatos):          #B <-- A
        for j in range(1,3):
            B[i+1][j]=A[i+1][j]
        #endFor
    #endFor
    FN.close()
    print("\t\tMatriz de datos:")
    for i in range(1,NumDatos+1):
        fila_i=""
        for j in range(1,3):
            fila_i=fila_i+("\t %10.6f" % (A[i][j]))
        #endfor
        print(fila_i)
    #endfor
    x=list(range(NumDatos+1))
    y=list(range(NumDatos+1))
    for i in range(1,NumDatos+1):
        x[i]=A[i][1]
        y[i]=A[i][2]
    #endFor
    sort(NumDatos,x,y)
    print("\n\t\tMatriz Ordenada:")
    for i in range(1,NumDatos+1):
        fila_i=""
        for j in range(1,3):
            fila_i=fila_i+("\t %10.6f" % (A[i][j]))
        #endfor
        print(fila_i)
    #endfor
    sig=list(range(NumDatos+1))
    tau=list(range(NumDatos+1))
    s  =list(range(NumDatos+1))
    SpCoef(NumDatos)
    print("-----------------")
    print("Los DATOS A INTERPOLAR deben estar en el dominio de <"+Arch+">")
    Interp=input("Dame el nombre del archivo de DATOS A INTERPOLAR: \t")
    print(Interp)
    try:
        FN = open(Interp,"r")
        print("Se abrió el archivo de DATOS A INTERPOLAR \""+Interp+"\"" )
    except:
        print("No se encontró el archivo \""+Interp+"\"")
        sys.exit("**** Fin de programa ****")
    #endTrydat
    print("En el ARCHIVO DE RESULTADOS se pondrán los valores \"splineados\"" )
    IntArch=input("Dame el nombre del ARCHIVO DE RESULTADOS: \t")
    print(IntArch)
    try:
        FI = open(IntArch,"w+")
        print("Se creó el archivo \""+IntArch+"\"" )
    except:
        print("No se creó el archivo \""+IntArch+"\"")
        sys.exit("**** Fin de programa ****")
    #endTrydat
    lista=FN.readlines()
    inFilas=len(lista)
    print("Datos a interpolar: "+str(inFilas))
    FN = open(Interp,"r")               # REWIND
    inDato=list(range(inFilas))
    for i in range(inFilas):
        inDato[i]=FN.readline()
        z=Spline(inFilas,float(inDato[i]))
        fila_i=("%12.6f \t %12.6f\r" % (float(inDato[i]),z))
        FI.write(fila_i)
    FN.close()
    FI.close()
    print("\n**** Los datos interpolados se escribieron en "+IntArch)
    #z=Spline(Filas,4.0)
    while True:
        Resp=input("\n\t\tDESEA SEGUIR ITERANDO (S/N)").upper()
        if Resp!="S" and Resp!="N":
            continue
        #endIf
        if Resp=="N":
            sys.exit("\t\t*** FIN DE PROGRAMA ***")
        #endIf
        break
    #endWhile
#endSplines.Sort.6
