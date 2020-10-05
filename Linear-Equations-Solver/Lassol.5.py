"""
   Lee el archivo "Datos.txt"
   Determina el número de líneas
   Determina el número de columnas

   Convierte los datos (ASCII) en flotantes
   Declara una matriz y la llena
   Pasa la matriz como parámetro
"""
import sys

def lassol(M, XY, CF):
    for i in range(0,M):
       rowmax=abs(XY[i][0])
       for j in range(1,M+1):   
           rowmax=max(rowmax,abs(XY[i][j]))
       #endFor
       if (rowmax==0):
         return False
       #endIf
       scale=1/rowmax   
       for j in range(0,M+1):
           XY[i][j]=XY[i][j]*scale   
       #endFor
    #endFor
    for k in range(0,M):
        big=0
        for i in range(k,M):
            temp=abs(XY[i][k])   
            if (big<temp):
                big=temp
                ipiv=i
            #endIf
        #endFor
        if (big==0):
            return False
        #endIf
#
#	Exchange column with largest element
#
        if (ipiv!=k):
            for i in range(k,M+1):
                temp=XY[k][i]   
                XY[k][i]=XY[ipiv][i]   
                XY[ipiv][i]=temp   
		      #endFor
	     #endIf
#
#	Eliminate all in column except first
#
        for i in range(k+1,M):
            quot=XY[i][k]/XY[k][k]   
            for j in range(k+1,M+1):
                XY[i][j]=XY[i][j]-quot*XY[k][j]   
		      #endfor
        #endFor
    #endFor
    if (XY[M-1][M-1]==0):
        return False
    #endIf
    CF[M-1]=XY[M-1][M]/XY[M-1][M-1]
    for i in range(M-2,-1,-1):
        sum=0
        for j in range(i+1,M):
            sum=sum+XY[i][j]*CF[j]
        #endFor
        CF[i]=(XY[i][M]-sum)/XY[i][i]
    #endFor
    return True
#endLassol

def PassMat(M,rows,cols):
    print("La matriz en memoria: ")
    for i in range(0,rows):
        for j in range(0,cols):
            print("XY["+str(i)+"]["+str(j)+"]\t"+str(M[i][j]))
        #endFor
    #endFor
    return
#endFunction
    
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
#       MIN
#
print("****")
print("    **** Empieza el programa ****")
print("****")
try:
    FN = open("1.Datos.txt","r")
    print("Se abrió el archivo \"Datos.txt\"" )
except:
    print("No se encontró el archivo \"Datos.txt\"")
    sys.exit("**** Fin de programa ****")
#endTry
lista = list(range(100))
lista=FN.readlines()
Filas=len(lista)
print("Filas: "+str(Filas))
FN = open("1.Datos.txt","r") 
Lineas=list(range(100))
Lineas[0]=FN.readline()
LineLen=len(Lineas[0])
Columnas=NumCols(Lineas[0],LineLen)
print("Columnas: "+str(Columnas))
if (Filas!=Columnas-1):
    print("¡¡¡<Número de filas> debe ser = <Número de columnas-1>!!!")
    print("**** \tFin de Programa ****\n\n\n")
    sys.exit()
#endIf
FN = open("1.Datos.txt","r")
XY=list(range(Filas))
for i in range(0,Filas):
    XY[i]=list(range(Columnas))
for i in range(0,Filas):
    Lineas[i]=FN.readline()
    for j in range(0,Columnas):
        L=Lineas[i]
        Num=getNum(L,j)     #j-th variablesin i-th line
        XY[i][j]=Num
    #endFor
#endFor
FN.close()
print("\tMatriz de datos:")
for i in range(0,Filas):
    fila_i=""
    for j in range(0,Columnas):
        fila_i=fila_i+str(XY[i][j])+"\t"
    #endfor
    print(fila_i)
#endfor
"""    
       LA MATRIZ "XY" SE MODIFICA EN LASSOL
       POR ELLO ES INDISPENSABLE ALMACENAR "XY" EN OTRO ARREGLO
       EN ESTE CASO EL ARRGELO SE DENOMINA "AB"
       PARA TENER UNA COPIA DE XY ES IMPOSIBLE HACER
       SIMPLEMENTE AB=XY
       EL OBJETO "AB" ES IDÉNTICO AL OBJETO "XY"
"""      
AB=list(range(Filas))
for i in range(0,Filas):
    AB[i]=list(range(Columnas))
for i in range(0,Filas):
    for j in range(0,Columnas):
        AB[i][j]=XY[i][j]
    #endFor
#endFor
Vars=Filas
CF = list(range(Vars))
if (not lassol(Vars, XY, CF)):
    print("Unstable system")
else:
    print("\n\tVALORES DE LA SOLUCIÓN\n")
    for i in range(0,Vars):
        print("\tC[ %2.0f ] = %10.6f " % (i,CF[i]))
    #endFor
#endIf
print("\n\t**** COMPROBACIÓN DE RESULTADOS ****\n")
print("         FUNCIÓN           ORIGINAL")
print("         -------           --------")
for i in range(0,Filas):
    F_Vars=0
    for j in range(0,Columnas-1):
        F_Vars=F_Vars+AB[i][j]*CF[j]
    #endFor
    print(" %2.0f ) %10.6f\t %10.6f " % (i, F_Vars, AB[i][Columnas-1]))
#endFor
#endLassol.5
