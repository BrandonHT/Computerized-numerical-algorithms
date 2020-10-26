import sys
import random
import math
#
#
#       INTEGRAL DE UNA FUNCIÓN MUESTREADA
#
def GetFG():
#---------------------------------------------
#	Matrix for mapping from T[-1,+1] to P[-1,+1]
#---------------------------------------------
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
        if (abs(x[i])<10e-6):
            x[i]=random.uniform(0,+10e-6)              #ALMOST 0
        else:
            x[i]=x[i]*(1+random.uniform(0,+10e-6))    #ALMOST XY[i][1]
        #endif
        xB[i]=x[i]
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
    for i in range(1,N):                # 1,2,...,N-1
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

print("Deme el GRADO MÁXIMO A CONSIDERAR PARA EL POLINOMIO A INTEGRAR:")
D=check_integer_ge1()      ## MAXIMUM INTERPOLATING DEGREE
Arch=input("Deme el nombre del archivo con los datos de la FUNCIÓN A INTEGRAR: \t")
try:
    FN = open(Arch,"r")
    print("\t*** Se abrió el archivo \""+Arch+"\"" )
except:
    print("\t*** No se encontró el archivo \""+Arch+"\"")
    sys.exit("**** Fin de programa ****")
#endTrydat
#    
C     =list(range(D+2))             # Coeficientes de los Tn(x)
Tuplas=FN.readlines()
N=len(Tuplas)
print("Tuplas: "+str(N))
LineLen=len(Tuplas[0])
Atribs=NumCols(Tuplas[0],LineLen)
print("Columnas: "+str(Atribs))
if (Atribs!=2):
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
        L=Tuplas[i]
        Num=getNum(L,j)         #"Num" is Floating point
        XY[i+1][j+1]=Num        # XY[1][1];XY[1][2];...;XY[N][1];XY[N][2])
    #endFor
#endFor
FN.close()
#
#       STEP 1:
#           STABILIZE THE ABSCISSAS
#
x=list(range(N+1))
xB=list(range(N+1))
y=list(range(N+1))
for i in range(1,N+1):
    x[i]=XY[i][1]
    xB[i]=x[i]
    y[i]=XY[i][2]
#endfor
stabilize(N)
#
#
#       STEP 2:
#           SORT THE DATA IN ASCENDING ORDER
#
sort(x,y,N)
Inf=x[1]                    # Smallest value for the integral
Sup=x[N]                    # Largest value for the integral
print("El límite inferior de la integral es %8.6f" % (Inf))
print("El límite superiorr de la integral es %8.6f" % (Sup))
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
#N=DetermineNumberOfOrthogonalityPoints()
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
#
#               STEP 9:
#                   EXPLORE DEGREES TO DETERMINE BEST APPROXIMATION
#
MinErr=+10e+06
for i in range(3,D+1):
    RMS_i=0
    for j in range(1,N+1):
        x_j=(2*xB[j]-Xsum)/Xdif                    # Mapea a [-1,+1]
        fx_j=0
        for k in range(1,i+1):
            fx_j=fx_j+C[k]*T(k-1,x_j)
        #endfor
        err_j=y[j]-fx_j
        RMS_i=RMS_i+err_j*err_j
    #endfor
    RMS_i=math.sqrt(RMS_i/float(N))
    if (RMS_i<MinErr):
        MinErr=RMS_i
        MinNdx=i
    #endif
#endfor
D=MinNdx        # This is the degree for the best error
print("El grado del polinomio con el menor error es "+str(D))
F=list(range(D+2))
for i in range(D+2):
    F[i]=list(range(D+2))
G=list(range(D+2))
for i in range(D+2):
    G[i]=list(range(D+2))
GetFG()                             # Calcula las matrices F y G
#
#               STEP 10:
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
#
#               STEP 11:
#                   CALCULATE THE COEFFICIENTS FOR THE MONOMIAL´S
#                   EXPANSION IN THE [A,B] INTERVAL
#
P    =list(range(D+2))             # Coeficientes de los monomios de x^i
U=-(Xsum/Xdif)
V=2/Xdif
for ix in range(2,D+2):
    i=1
    for k in range(1,ix+1):
        P[k]=0
        for j in range(k,ix+1):
            P[k]=P[k]+G[i][j]*A[j]*math.pow(U,j-k)
        #endfor
        P[k]=P[k]*math.pow(V,k-1)
        i=i+1
    #endfor
#endfor
print("\nEl polinomio encontrado es: \n")
for i in range(1,D+2):
    print("C%2.0f) %14.12f X**%2f" % (i-1,P[i],i-1))
#endfor
print()
Q    =list(range(D+2))             # Coeficientes de la integral
for i in range(1,D+2):
    Q[i]=P[i]/float(i)
#endfor
print("Integral definida entre %6.4f y %6.4f" % (Inf,Sup))
for i in range(1,D+2):
    print("C%2.0f) %14.12f X**%2f" % (i,Q[i],i))
#endfor
print()
Upper=0
Lower=0
for i in range(1,D+2):
    j=D+1-i
    Lower=Lower+Q[j]*math.pow(Inf,j)
    Upper=Upper+Q[j]*math.pow(Sup,j)
#endfor
print("Upper: "+str(Upper))
print("Lower: "+str(Lower))
Integral=Upper-Lower
print("El valor de la integral definida entre %12.6f y %12.6f es %12.6f"  % (Inf,Sup,Integral))
#
OutDat="Test.xls"
try:
    FDO = open(OutDat,"w+")
except:
    print("No se creó el archivo \""+OutDat+"\"")
    sys.exit("**** Fin de programa ****")
#endTrydat
for i in range(1,N+1):
    x_i=xB[i]
    ys=0
    for i in range(1,D+2):
        ys=ys+Q[i]*math.pow(x_i,i-1)
    #endfor
    fila_i=("%12.6f \t %12.6f\n" % (x_i,ys))
    FDO.write(fila_i)
#endfor    
FDO.close()
print("\n**** Los datos de la integral interpolada se escribieron en "+OutDat)
