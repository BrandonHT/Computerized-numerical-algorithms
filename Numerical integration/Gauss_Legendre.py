import sys
import math
from sympy import Symbol, diff, solve, integrate, sympify

x = Symbol('x')
y = Symbol('y')

# Verifica que los valores ingresados sean tipo float
def check_format(x):
    while True:
        try:
            x = float(input("\""+x+"\")\t"))
            return x
        except:
            print("Must been a number")
            print("Try again")
            

# FORMULA DE RODRIGUES
# Fórmula para los polinomios de Legendre
# 
# n es el grado del polinomio de Legendre
def rodrigues(n):   
    x = Symbol("x")
    y = (x**2 - 1)**n
    polinomio = diff(y, x, n) / (2**n * math.factorial(n))
    return polinomio

def cuadra_Gauss(a, b, n):
    #Calcula raíces del polinomio de Legendre
    var = rodrigues(n)
    #--print(f"Rodrigues: {var}")
    x_roots = solve(var, x) 
    
    # Calcula derivadas del polinomio de Legendre 
    x_diff= diff(rodrigues(n)) 
    #--print(f"Valor de diferencial: {x_diff}")
    
    # Guarda los valores 
    Suma = [] 
    Aux = [[] , []] 
    
    for i in range(n):
        Suma.append(2/((1-x_roots[i]**2)*(x_diff.evalf(subs={x:x_roots[i]}))**2))
        Aux[0].append(y.evalf(subs={x:(b-a)*(x_roots[i]/2)+(a+b)/2}))
        Aux[1].append(Suma[i]*Aux[0][i])
        
    print(str(Suma))
    
    cuad = ((b-a)/2)*sum(Aux[1])
    exac = (integrate(y,x).evalf(subs={x:b}))-(integrate(y,x).evalf(subs={x:a}))    
    error = ((exac-cuad))    
    ER = abs((exac - cuad)/exac) * 100   
    print ("\nResultado de cuadratura: ", cuad)    
    print ("Resultado exacto : ", exac)    
    print ("Porcentaje de error absoluto: ", error)
    print ("Error relativo: ", ER)
    
    return error


#----------------------------------------------------------------------------#
# CÓDIGO PARA HACER LA INTERPOLACIÓN DE UN SISTEMA DE ECUACIONES

def lassol(M, XY, CF):
    for i in range(0,M):
       rowmax = abs(XY[i][0])
       for j in range(1,M+1):   
           rowmax = max(rowmax, abs(XY[i][j]))
       #endFor
       if (rowmax == 0):
         return False
       #endIf
       scale=1 / rowmax   
       for j in range(0,M+1):
           XY[i][j] = XY[i][j]*scale   
       #endFor
    #endFor
    for k in range(0, M):
        big = 0
        for i in range(k, M):
            temp = abs(XY[i][k])   
            if (big < temp):
                big = temp
                ipiv = i
            #endIf
        #endFor
        if (big == 0):
            return False
        #endIf
        
#
#	Exchange column with largest element
#
        if (ipiv != k):
            for i in range(k, M+1):
                temp = XY[k][i]   
                XY[k][i] = XY[ipiv][i]   
                XY[ipiv][i] = temp   
		      #endFor
	     #endIf
         
         
#
#	Eliminate all in column except first
#
        for i in range(k+1, M):
            quot = XY[i][k]/XY[k][k]   
            for j in range(k+1,M+1):
                XY[i][j] = XY[i][j] - quot * XY[k][j]   
		      #endfor
        #endFor
    #endFor
    
    if (XY[M - 1][M - 1] == 0):
        return False 
    #endIf
    CF[M - 1] = XY[M - 1][M] / XY[M - 1][M - 1]
    for i in range(M-2, -1, -1):
        sum = 0
        for j in range(i+1, M):
            sum = sum + XY[i][j] * CF[j]
        #endFor
        CF[i] = (XY[i][M] - sum) / XY[i][i]
    #endFor
    return True
#endLassol

def PassMat(M, rows, cols):
    print("La matriz en memoria: ")
    for i in range(0, rows):
        for j in range(0, cols):
            print("XY["+ str(i) +"]["+ str(j) +"]\t"+ str(M[i][j]))
        #endFor
    #endFor
    return
#endFunction
    
def NumCols(Linea, Linelen):
    cols = 1
    for i in range(0, LineLen):
        if (Linea[i] == "\t"):
            cols = cols + 1
        #endIf
    #endFor
    return cols
#endFunction

def getNum(Linea, numVar):
    countVar = -1
    first = 0
    for i in range(0, numVar+1):
        x = ""
        for j in range(first, len(Linea)):
            if (Linea[j] == "\t" or Linea[j] == "\n"):
                first = j + 1
                countVar = countVar + 1
                break
            else:
                x = x + Linea[j]
            #endif
        #endFor
        if (countVar == numVar):
            return float(x)
        #endIf
    #endFor
#endFunction

def polynomial(lista):
    while True:
        degree = len(lista)
        if(degree >= 1):
            break
        #endif
        print("Error, it may be, at least, a first degree")
    #endwhile
    Fx = [0]*(degree)
    
    for i in range(degree):
        Fx[i] = lista[i]
    ##EndFor
    print(f"{Fx}")
    return Fx
##EndFunction

## Evalua el polinomio
def evaluate_pol(Fx, x):
    res = 0
    degree = len(Fx) 
    for i in range(degree ):
       # print(f"COEFICIENTE: {Fx[i]}")
       #print(f"VALOR i: {i}")
       #print(f"GRADO: {degree}")
       res += Fx[i]*x**(i)
    #print(f"\nEL RESULTADO PRUEBA ES: {res}")
    return res 

#----------------------------------------------------------------------------#
   
#           INICIA PROGRAMA

# Symbol se utiliza para definir variables
# sin otorgarles algún valor en específico
# Se vuelven para usar Sympy
y = Symbol('y')
x = Symbol('x')
f = Symbol("f")

print("Seleccione como quiere ingresar la función ")
print("1) Ingresar la función manualmente ")
print("2) A partir de un documento externo (Sistema de ecuaciones)")

try:
    resp = int(input("Seleccione 1 o 2: "))
except:
    sys.exit("*** FIN DEL PROGRAMA ***")
    
if resp == 1:
    
    # Sympify convierte una expresión a una variable que se puede utilizar 
    # con sympy
    y = sympify(input("Ingrese manualmente la función (escriba en términos de x  y sin y= ) "))
    print(type(y))
    print(f"Y: {y}")
        
    # Intervalos de integración
    print("Da el valor de los intervalos de integración: ")
    try:
        a = check_format("a")
        b = check_format("b")
    except:
        sys.exit("*** VERIFIQUE QUE LOS VALORES INGRESADOS HAYAN SIDO NÚMEROS ***")
    
    # Grado polinomio Legendre
    try:
        n = int(input("Grado polinomio de Legendre: \n"))#check_format("Grado: ")    
    except:
        sys.exit("*** ERROR ***")
    
   
    cuadra_Gauss(a, b, n)
    
    
    
if resp == 2:
    # Intervalos de integración
    print("Da el valor de los intervalos de integración: ")
    try:
        a = float(input("El valor de a es: "))
        b = float(input("El valor de b es: "))
    except:
        sys.exit("**** Los valores que dio no son números ****")
        
    # Grado del polinomio de Legendre
    try:
        n = int(input("Grado polinomio de Legendre: \n"))    
    except:
        sys.exit("*** ERROR ***")

    # Código utilizado en el programa Interp.1.py
    Arch = input("Dame el nombre del archivo a leer: \t")
    Interp = Arch
    
    try:
        FN = open(Arch, "r")
        print("Se abrió el archivo \""+ Arch +"\"" )
    except:
        print("No se encontró el archivo \""+ Arch +"\"")
        sys.exit("**** Fin de programa ****")
        
    
    lista = list(range(0))
    lista = FN.readlines()
    Filas = len(lista)
    print("Filas: " + str(Filas))
    
    FN = open(Arch, "r") 
    Lineas = list(range(Filas))
    Lineas[0] = FN.readline()
    LineLen = len(Lineas[0])
    Columnas = NumCols(Lineas[0], LineLen)
    print("Columnas: " + str(Columnas))
    
    if (Filas != Columnas - 1):
        print("¡¡¡<Número de filas> debe ser = <Número de columnas-1>!!!")
        print("**** \tFin de Programa ****\n\n\n")
        sys.exit()
    
    FN = open(Arch,"r") 
    XY = list(range(Filas))
    
    for i in range(0, Filas):
        XY[i]=list(range(Columnas))
        
    for i in range(0, Filas):
        Lineas[i] = FN.readline()
        for j in range(0, Columnas):
            L = Lineas[i]
            Num = getNum(L, j)     #j-th variablesin i-th line
            XY[i][j] = Num
    
    FN.close()
    
    print("\tMatriz de datos:")
    for i in range(0, Filas):
        fila_i = ""
        for j in range(0, Columnas):
            XYij = XY[i][j]
            fila_i = fila_i + ("%10.4f" % (XY[i][j]))
        
        print(fila_i)
    
    
    """    
           LA MATRIZ "XY" SE MODIFICA EN LASSOL
           POR ELLO ES INDISPENSABLE ALMACENAR "XY" EN OTRO ARREGLO
           EN ESTE CASO EL ARREGLO SE DENOMINA "AB"
           PARA TENER UNA COPIA DE XY ES IMPOSIBLE HACER
           SIMPLEMENTE AB=XY
           EL OBJETO "AB" ES IDÉNTICO AL OBJETO "XY"
    """      
    
    AB = list(range(Filas))
    
    for i in range(0, Filas):
        AB[i] = list(range(Columnas))
        
    for i in range(0, Filas):
        for j in range(0, Columnas):
            AB[i][j] = XY[i][j]
    
    
    Vars = Filas
    CF = list(range(Vars))
    var = list()    # Almacena los valores de los coeficientes
    
    if (not lassol(Vars, XY, CF)):
        print("****\n****\n\t\tUNSTABLE SYSTEM\n****\n****")
    else:
        print("\n\tVALORES DE LA SOLUCIÓN\n")
        for i in range(0, Vars):
            var.append(CF[i])
            print("\tC[ %2.0f ] = %10.6f " % (i,CF[i]))
    
    
    for i in range(0,Filas):
        F_Vars=0
        for j in range(0,Columnas-1):
            F_Vars=F_Vars+AB[i][j]*CF[j]
        #endFor
        print(" %2.0f ) %10.6f\t %10.6f " % (i, F_Vars, AB[i][Columnas-1]))
    
    #
    #   Obtenemos los valores de los coeficientes de la función interpolada
    #
    print("\n\n**** VALORES DE LOS COEFICIENTES DE LA FUNCIÓN INTERPOLADA ****")
    for i in range (0, Columnas-1):
        print(f"  {i}) {var[i]}")
        
    
    #
    # Escribimos el polinomio con los coeficientes
    # obtenidos de la interpolación
    #
    PolIn = " "
    count = len(var)
    
    for i in range(len(var)):
        if i < len(var)-1:
            PolIn = PolIn +(str(var[i]*x**(count-1))) + "+"
        else:
            PolIn = PolIn +(str(var[i]*x**(count-1))) 
        count = count -1
    
    print(f"{PolIn}")
    
    # Convertimos la variable "y" en una variable
    # tipo sympy para poder realizar la cuadratura
    y = sympify(PolIn)
    
    cuadra_Gauss(a, b, n)

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    