#   THIS PROGRAM SOLVES FOR THE TWO ROOTS OF A 2ND
#   DEGREE EQUATION
#       aX^2+bX+c
#
import math
import sys
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


     