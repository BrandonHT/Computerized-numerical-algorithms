import sys
import random
import math
#
#       ESTA VERSIÓN INCLUYE DETERMINACIÓN DE LOS PUNTOS DE ORTOGONALIDAD
#       Y ESTABILIZACIÓN DE LOS DATOS
#       Y EL CALCULO POLINOMIAL EN EL INTERVALO ORIGINAL [a,b]
#
#       LEAST SQUARES POLYNOMIAL FIT
#
def GetFG():
    F[1][1]=1
    F[1][2]=0
    F[2][2]=1
    for i in range(1,D+2):
        for j in range(3,D+2):
            F[i][j]=0
        #endfor
    #endfor
    for j in range(3,D+2):
        for i in range(2,j+1):
            F[i][j]=2*F[i-1][j-1]
        #endfor
        for i in range(1,j-1):
            F[i][j]=F[i][j]-F[i][j-2]
        #endfor
    #endfor
#-----------------------------
#	Main diagonal
#-----------------------------
    for i in range(3,D+2):  
        F[i][i]=2*F[i-1][i-1]
    #endfor
#------------------------------
    for i in range(2,D+2):
        for j in range(1,i):
            F[i][j]=0
        #endfor
    #endfor
#    for i in range(1,D+2):
#        fila_i=""
#        for j in range(1,D+2):
#            fila_i=fila_i+("%6.4f " % (F[i][j]))
#        #endfor
#        print(fila_i)
#    #endfor
#    print("------------------------")
#---------------------------------------------
#	Matrix for mapping from P[-1,+1] to P[a,b]
#---------------------------------------------
    for i in range(1,D+2):
        G[i][i]=1
        G[1][i]=1
    #endfor
    for i in range(2,D+2):
        for j in range(i+1,D+2):
            G[i][j]=G[i-1][j-1]+G[i][j-1]
        #endfor
    #endfor
    for i in range(2,D+2):
        for j in range(1,i):
            G[i][j]=0
        #endfor
    #endfor
 #   for i in range(1,D+2):
 #       fila_i=""
 #       for j in range(1,D+2):
 #           fila_i=fila_i+("%6.4f " % (G[i][j]))
 #       #endfor
 #       print(fila_i)
 #   #endfor
    return
#endGetFG

def stabilize(n):
    for i in range(1,n+1):                                # LEAVE OUT EXTREME POINTS
        XY_i1=XY[i][1]
        if (abs(XY_i1)<10e-6):
            XY_i1=random.uniform(0,+10e-6)              #ALMOST 0
        else:
            XY_i1=XY_i1*(1+random.uniform(0,+10e-6))    #ALMOST XY[i][1]
        #endif
        XY[i][1]=XY_i1
    #endfor
    return
#endStabilize

def sort(x,y,n):
#   
#   n is the number of data points
#   x holds the independent data variable´s values
#       Values
#   y holds the dependent data variable´s values
#       Original production sequence
#   ON OUTPUT:
#   array XY is sorted from smallest to largest
#
    for i in range(1,n):                # i=1,...,n-1
        tmin=x[i]
        imin=i
        for j in range(i+1,n+1):        # j=i+1,...,n
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
        XY[i][1]=x[i]
        XY[i][2]=y[i]
    #endFor
    return
#endSort

def DetermineNumberOfOrthogonalityPoints():
    minDif=10e+06
    for i in range(1,N):
        dif=abs(x[i]-x[i+1])
        if (dif<minDif):
            minDif=dif
        #endif
    #endfor
    return math.ceil((x[N]-x[1])/minDif)
#endDetermine
    
def SpCoef(n):
# This subroutine calculates the values of the 2nd derivatives of the spline.
#     ON INPUT:
# n is the number of data points
# x holds the independent variable’spoints to be interpolated
# y holds the dependent variable’s points to be interpolated
#     ON OUTPUT:
#- s is the vector where the 2nd derivatives are stored
#- sig(ma) and tau are auxiliary stores of size n
#
    sig[2]=0.  
    tau[2]=0.  
    for i in range(2,n):                    # 2,3,...,n-1
        Him1=x[i]-x[i-1]
        Hi=x[i+1]-x[i]  
        temp=(Him1/Hi)*(sig[i]+2)+2. 
        sig[i+1]=-1/temp                    # sig[3],sig[4],...,sig[n]
        d=6*((y[i+1]-y[i])/Hi-(y[i]-y[i-1])/Him1)/Hi  
        tau[i+1]=(d-Him1*tau[i]/Hi)/temp    # tau[3],tau[4],...,tau[n] 
    #endfor  
    s[1]=0  
    s[n]=0  
    for i in range(1,n-1):  
       ib=n-i
       s[ib]=sig[ib+1]*s[ib+1]+tau[ib+1]    # s[n-1],s[n-2],...,s[2]
    #endfor
    return  
#endSPcoef
    
def Spline(x_i,n):
    for i in range(2,n+1):
        if (x_i<=x[i]):
            break                           # Determine the i-th segment of the spline
        #endif
    #endfor
    i=i-1
    a=x[i+1]-x_i
    b=x_i-x[i]
    hi=x[i+1]-x[i]
    y_i=a*s[i]*(a*a/hi-hi)/6+b*s[i+1]*(b*b/hi-hi)/6+(a*y[i]+b*y[i+1])/hi
    return y_i
#endSpline

def check_integer_ge1():
    while True:
        try:
            while True:
                x=float(input())
                x=int(x)
                if (x>=2):
                    return x
                #endif
                print("El grado debe ser \"2\" o más")
                print("Intente de nuevo")
            #endwhile
        except:
            print("Debe ser un número")
            print("Intente de nuevo")
    ##EndWhile
##EndFunction  

def check_integer_in():
    while True:
        try:
            while True:
                x=float(input())
                x=int(x)
                if (x==0 or x==1):
                    return x
                #endif
                print("Debe ser \"0\" (NO) o \"1\" (SI)")
                print("Intente de nuevo")
            #endWhile
        except:
            print("Debe ser un número")
            print("Intente de nuevo")
    ##EndWhile
##EndFunction  
    
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

#
#       The value of the r-th Chebushev polynomial at x
#
def T(r,x):
    return math.cos(r*math.acos(x))
#
#       MAIN
#

print("Deme el GRADO DEL POLINOMIO DE APROXIMACIÓN:")
D=check_integer_ge1()      ## MAXIMUM INTERPOLATING DEGREE
F=list(range(D+2))
for i in range(D+2):
    F[i]=list(range(D+2))
G=list(range(D+2))
for i in range(D+2):
    G[i]=list(range(D+2))
GetFG()
#    
C     =list(range(D+2))
AB    =list(range(D+2))
Arch=input("Deme el nombre del ARCHIVO DE DATOS A ANALIZAR: \t")
try:
    FN = open(Arch,"r")
    print("\t*** Se abrió el archivo \""+Arch+"\"" )
except:
    print("\t*** No se encontró el archivo \""+Arch+"\"")
    sys.exit("**** Fin de programa ****")
#endTrydat
Lineas=FN.readlines()
N=len(Lineas)
print("Filas: "+str(N))
LineLen=len(Lineas[0])
Columnas=NumCols(Lineas[0],LineLen)
print("Columnas: "+str(Columnas))
if (Columnas!=2):
    print("¡¡¡Debe haber solamente dos columnas!!!")
    print("**** \tFin de Programa ****\n\n\n")
    sys.exit()
#endIf
FN = open(Arch,"r")             # REWIND
XY=list(range(0,N+1))
for i in range(0,N+1):
    XY[i]=list(range(0,3))
#
#       PON LOS DATOS EN XY[i][j] EN PUNTO FLOTANTE
#
for i in range(0,N):            # N tuples  (i=0,1,...,N-1)
    for j in range(0,2):        # 2 columns (j=0,1)
        L=Lineas[i]
        Num=getNum(L,j)         #"Num" is Floating point
        XY[i+1][j+1]=Num        # XY[1][1];XY[1][2];...;XY[N][1];XY[N][2])
    #endFor
#endFor
FN.close()
#
#       STEP 1:
#           SORT THE DATA IN ASCENDING ORDER
#
x=list(range(N+1))
y=list(range(N+1))
for i in range(1,N+1):
    x[i]=XY[i][1]
    y[i]=XY[i][2]
#endfor
sort(x,y,N)
#
#       STEP 2:
#           STABILIZE THE ABSCISSAS
#
stabilize(N)
#
#       STEP 3:
#           MAP INTO DE [-1,+1] INTERVAL
#
Xsum=x[N]+x[1]
Xdif=x[N]-x[1]
for i in range(1,N+1):
    x[i]=(2*x[i]-Xsum)/Xdif
#endfor
#
#       STEP 4:
#           CALCULATE THE NATURAL SPLINE
#
sig=list(range(N+1))
tau=list(range(N+1))
s  =list(range(N+1))
SpCoef(N)                           #CALCULATE THE SPLINE'S COEFFICIENTS
#
#       STEP 5:
#           DETERMINE THE NUMBER OF ORTHOGONALITY POINTS 
#           FOR THE INPUT DATA
#
N=DetermineNumberOfOrthogonalityPoints()
#
#       STEP 5:
#           CALCULATE THE ARGUMENTS FOR THE ORTHOGONALITY POINTS
#
Pi_2N=math.pi/(2*N)
A=list(range(N+1))
for i in range(1,N+1):
    iB=N-i+1
    A[i]=(2*iB-1)*Pi_2N
#endfor
#
#       STEP 6:
#           OBTAIN THE VALUES OF "X" AT THE ORTHOGONALITY POINTS
#
Xbar=list(range(N+1))               # 0,1,...,N
for i in range(1,N+1):              # 1,...,N
    Xbar[i]=math.cos(A[i])          # The i-th Chebayshev abscissa
#endfor
#
#       STEP 7:
#           OBTAIN THE VALUES OF "Y" AT THE ORTHOGONALITY POINTS
#
Ybar=list(range(N+1))             # 0,1,...,N
for i in range(1,N+1):
    Ybar[i]=Spline(Xbar[i],N)
#endfor
#
#       STEP 8:
#           CALCULATE THE COEFFICIENTS FOR THE CHEBYSHEV POLYNOMIALS
#               (FOR A SPECIFIED DEGREE)
#
for j in range(1,D+2):
    C[j]=0
    j_1=j-1
    for i in range(1,N+1):
        C[j]=C[j]+Ybar[i]*math.cos(j_1*A[i])
    #endfor
    if (j==1):
        C[j]=C[j]/float(N)
    else:
        C[j]=C[j]*2/float(N)
    #endif
#endfor
print("Coeficientes del Producto de Polinomios de Chebyshev en [-1,+1]:")
for i in range(1,D+2):
    fila_i=("C(%2.0f)=\t%12.10f" % ((i-1),C[i]))
    print(fila_i)
#endfor
#
#               STEP 9:
#                   CALCULATE THE COEFFICIENTS FOR THE POLYNOMIAL
#                   EXPANSION IN THE [-1,+1] INTERVAL
#
A=list(range(D+2))
for U in range(2,D+2):
    for j in range(1,U+1):
        A[j]=0
        for i in range(j,U+1):
            A[j]=A[j]+C[i]*F[j][i]
        #endfor
    #endfor
#endfor
print("Coeficientes del Producto de Potencias de Monomios en [-1,+1]:")
for i in range(1,D+2):
    fila_i=("A(%2.0f)=\t%12.10f" % ((i-1),A[i]))
    print(fila_i)
#endfor
#
#               STEP 10:
#                   CALCULATE THE COEFFICIENTS FOR THE MONOMIAL´S
#                   EXPANSION IN THE [A,B] INTERVAL
#
U=-(Xsum/Xdif)
V=2/Xdif
for ix in range(2,D+2):
    i=1
    for k in range(1,ix+1):
        AB[k]=0
        for j in range(k,ix+1):
            AB[k]=AB[k]+G[i][j]*A[j]*math.pow(U,j-k)
        #endfor
        AB[k]=AB[k]*math.pow(V,k-1)
        i=i+1
    #endfor
#endfor
print("Coeficientes del Producto de Potencias de Monomios en [A,B]:")
for i in range(1,D+2):
    fila_i=("AB(%2.0f)=\t%12.10f" % ((i-1),AB[i]))
    print(fila_i)
#endfor
#
#               INTERPOLACIÓN
#
print("-----------------")
print("DATOS A INTERPOLAR: ")
InpDat=input("Dame el nombre del archivo de DATOS A INTERPOLAR: \t")
try:
    FDI = open(InpDat,"r")
except:
    print("No se encontró el archivo \""+InpDat+"\"")
    sys.exit("**** Fin de programa ****")
#endTrydat
print("-----------------")
print("En el ARCHIVO DE RESULTADOS se pondrán los valores interpolados del Polinomio de Chebyshev" )
OutDat1=input("Dame el nombre de regresión para Polinomio de Chebyshev: \t")
try:
    FDO1 = open(OutDat1,"w+")
except:
    print("No se creó el archivo \""+OutDat1+"\"")
    sys.exit("**** Fin de programa ****")
#endTrydat
for i in range(1,D+2):
    fila_i=("T(%2.0f)=\t%12.10f\n" % ((i-1),C[i]))
    FDO1.write(fila_i)
#endfor
FDO1.write("*****\n")
print("-----------------")
print("En el ARCHIVO DE RESULTADOS se pondrán los valores interpolados del Polinomio en [A,B]" )
OutDat2=input("Dame el nombre de regresión para Suma de Monomios: \t")
try:
    FDO2 = open(OutDat2,"w+")
except:
    print("No se creó el archivo \""+OutDat2+"\"")
    sys.exit("**** Fin de programa ****")
#endTrydat
for i in range(1,D+2):
    fila_i=("AB(%2.0f)=\t%12.10f\n" % ((i-1),AB[i]))
    FDO2.write(fila_i)
#endfor
FDO2.write("*****\n")
#
#       Existencia de archivos ha sido validada
#
lista=FDI.readlines()
inFilas=len(lista)
print("Número de puntos a interpolar: "+str(inFilas))
FDI = open(InpDat,"r")               # REWIND Input File
inDato=list(range(inFilas))
for i in range(inFilas):
    inDato[i]=FDI.readline()
    x_i=float(inDato[i])
    xs=(2*x_i-Xsum)/Xdif                    # Mapea a [-1,+1]
    if (xs<x[1] or xs>x[N]):
        print("¡¡¡VALOR DE INTERPOLACIÓN FUERA DE RANGO!!!")
        print("Punto No. "+str(i))
        print("*** PUNTO NO SE PROCESA ***")
        continue
    #endif
    ys=0
    for i in range(1,D+2):
        ys=ys+C[i]*T((i-1),xs)
    #endfor
    fila_i=("%12.6f \t %12.6f\n" % (x_i,ys))
    FDO1.write(fila_i)
    ys=0
    for i in range(1,D+2):
        ys=ys+AB[i]*math.pow(x_i,i-1)
    #endfor
    fila_i=("%12.6f \t %12.6f\n" % (x_i,ys))
    FDO2.write(fila_i)
#endfor    
FDI.close()
FDO1.close()
FDO2.close()
print("\n**** Los datos interpolados para Chebyshev se escribieron en "+OutDat1)
print("\n**** Los datos interpolados para Polinomio se escribieron en "+OutDat2)
