# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 17:51:49 2020

@author: brand
"""


import random
import sys
from sklearn.metrics import mean_squared_error

MaximumNumberOfIndependentVariables=5
DEBUG=False
DDEBUG=False
while True:
    #DEBUG=input("Want to debug this run? (Y/N) ").upper()
    DEBUG='N'
    if (DEBUG=="Y"):
        DEBUG=True
        break
    #endif
    if (DEBUG=="N"):
        DEBUG=False
        break
    #endif
#endwhile
if (DEBUG):
    while True:
        DDEBUG=input("\tDouble Debug? (Y/N) ").upper()
        if (DDEBUG=="Y"):
            DDEBUG=True
            break
        #endif
        if (DDEBUG=="N"):
            DDEBUG=False
            break
        #endif
    #endwhile
#endif
    
infinity=100000000
EpsiTh=-infinity
bxe=+infinity
Th_Ndx=0
EpsiPh=0
PrevTh=0
Ph_Ndx=0
Mu=+1

def sort(n,x,y):
    for i in range(0,n):
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
    return x,y
def data2map():
    iv=list(range(m))
    for i in range(1,n+1):
        for j in range(1,m):
            iv[j]=xy[i][j]
        #endfor
        k=1
        while k<=M:
            for p1 in range(0,Deg[1]+1):
                if (IV==1):
                    map[i][k+1]=pow(iv[1],p1)
                    k=k+1
                    continue
                #endif
                for p2 in range(0,Deg[2]+1):
                    if (IV==2):
                        map[i][k+1]=pow(iv[1],p1)*pow(iv[2],p2)
                        k=k+1
                        continue
                    #endif
                    for p3 in range(0,Deg[3]+1):
                        if (IV==3):
                            map[i][k+1]=pow(iv[1],p1)*pow(iv[2],p2)*pow(iv[3],p3)
                            k=k+1
                            continue
                        #endif
                        for p4 in range(0,Deg[4]+1):
                            if (IV==4):
                                map[i][k+1]=pow(iv[1],p1)*pow(iv[2],p2)*pow(iv[3],p3)*pow(iv[4],p4)
                                k=k+1
                                continue
                            #endfor
                            for p5 in range(0,Deg[5]+1):
                                map[i][k+1]=pow(iv[1],p1)*pow(iv[2],p2)*pow(iv[3],p3)*pow(iv[4],p4)*pow(iv[5],p5)
                                k=k+1
                            #endfor
                        #endfor
                    #endfor
                #endfor
            #endfor
        #endfor
        map[i][k+1]=xy[i][m]
    #endfor
    return
#endData2Map

#
#           STABILIZATION
#
def stabilize():
    for i in range(1,n+1):
        for j in range(1,M+3):
            if (abs(map[i][j])<10e-6):
                map[i][j]=random.uniform(0,+10e-6)                  #ALMOST 0
            else:
                map[i][j]=map[i][j]*(1+random.uniform(0,+10e-6))    #ALMOST XY[i][1]
            #endif
        #endfor
    #endfor
    return
#endStabilize

#
#       Find the signs from the coefficients of an (M)X(M+1) system
#           ON INPUT: data is in ab[M][M+1] matrix
#           ON OUTPUT: coefficients are in cf[M]
#
def FirstSigns():
    for i in range(0,M):
        rowmax=abs(ab[i][0])
        for j in range(1,M+1):   
            rowmax=max(rowmax,abs(ab[i][j]))
        #endFor
        if (rowmax==0):
          return False
        #endIf
        scale=1/rowmax   
        for j in range(0,M+1):
            ab[i][j]=ab[i][j]*scale   
        #endFor
    #endFor
    for k in range(0,M):
        big=0
        for i in range(k,M):
            temp=abs(ab[i][k])   
            if (big<temp):
                big=temp
                ipiv=i
            #endIf
        #endFor
        if (big==0):
            return False
        #endIf
        if (ipiv!=k):
            for i in range(k,M+1):
                temp=ab[k][i]   
                ab[k][i]=ab[ipiv][i]   
                ab[ipiv][i]=temp   
		      #endFor
	     #endIf
        for i in range(k+1,M):
            quot=ab[i][k]/ab[k][k]   
            for j in range(k+1,M+1):
                ab[i][j]=ab[i][j]-quot*ab[k][j]   
		      #endfor
        #endFor
    #endFor
    if (ab[M-1][M-1]==0):
        return False
    #endIf
    cf[M-1]=ab[M-1][M]/ab[M-1][M-1]
    for i in range(M-2,-1,-1):
        sum=0
        for j in range(i+1,M):
            sum=sum+ab[i][j]*cf[j]
        #endFor
        cf[i]=(ab[i][M]-sum)/ab[i][i]
    #endFor
    return True
#endFirstSigns

#
#       INVERT AN MXM MATRIX
#   ON INPUT:
#       "map" ---> MXM MATRIX TO INVERT
#       M=TUPLES/ATRIBS OF "A"
#       "Ix"   ---> MXM INVERTED MATRIX

def FirstInverse():
    import numpy as np
    from numpy import empty
    a = empty([M+1,M+1])
    for i in range(0,M+1):
        for j in range(0,M+1):
            a[i][j]=map[i+1][j+1]
        #endfor
    #endfor
    ai=np.linalg.inv(a) 
    for i in range(0,M+1):
        for j in range(0,M+1):
            Ix[i+1][j+1]=ai[i][j]
        #endfor
    #endfor
    return
#endInvertMatrix

def testInverse():
    #print("MATRIX TO INVERT:")
    for i in range(1,M+2):
        map_i=""
        for j in range(1,M+2):
            map_i=map_i+"%10.6f\t" % (map[i][j])
        #endfor
        #print(map_i)
    #endfor
    #print("INVERSE MATRIX:")
    for i in range(1,M+2):
        Ix_i=""
        for j in range(1,M+2):
            Ix_i=Ix_i+"%10.6f\t" % (Ix[i][j])
        #endfor
        #print(Ix_i)
    #endfor
    p=list(range(M+2))
    for i in range(M+2):
        p[i]=list(range(M+2))
    #endfor
    for i in range(1,M+2):
        for j in range(1,M+2):
            p[i][j]=0
        #endfor
    #endfor
    for i in range(1,M+2): 
        for j in range(1,M+2): 
            for k in range(1,M+2): 
                p[i][j]=p[i][j]+map[i][k]*Ix[k][j] 
            #endfor
        #endfor
    #endfor
    #print("PRODUCT OF MATRIX BY ITS INVERSE")
    for i in range(1,M+2):
        P_i=""
        for j in range(1,M+2):
            P_i=P_i+"%10.6f\t" % (p[i][j])
        #endfor
        #print(P_i)
    #endfor
    return
#endtestInverse

def getCoefs():
    global EpsiPh,EpsiTh,PrevTh
    for i in range(1,M+2):
        C[i]=f[1]*Ix[i][1]
        for j in range(2,M+2):
            C[i]=C[i]+f[j]*Ix[i][j]
        #endfor
    #endfor
    PrevTh=EpsiTh
    EpsiTh=abs(C[1])
    return

def printCoefs():
    print("\nepsi="+str(C[1]))
    l=2
    for p1 in range(0,Deg[1]+1):
        if (IV==1):
            print("c["+str(p1)+"]="+str(C[l]))
            l=l+1
            continue
        #endif
        for p2 in range(0,Deg[2]+1):
            if (IV==2):
                print("c["+str(p1)+str(p2)+"]="+str(C[l]))
                l=l+1
                continue
            #endif
            for p3 in range(0,Deg[3]+1):
                if (IV==3):
                    print("c["+str(p1)+str(p2)+str(p3)+"]="+str(C[l]))
                    l=l+1
                    continue
                #endif
                for p4 in range(0,Deg[4]+1):
                    if (IV==4):
                        print("c["+str(p1)+str(p2)+str(p3)+str(p4)+"]="+str(C[l]))
                        l=l+1
                        continue
                    #endif
                    for p5 in range(0,Deg[5]+1):
                        print("c["+str(p1)+str(p2)+str(p3)+str(p4)+str(p5)+"]="+str(C[l]))
                        l=l+1
                    #endfor
                #endfor
            #endfor
        #endfor
    #endfor
    return

def generateCoefs():
    listaCoefAux=[]
    print("\nepsi="+str(C[1]))
    l=2
    for p1 in range(0,Deg[1]+1):
        if (IV==1):
            print("c["+str(p1)+"]="+str(C[l]))
            l=l+1
            continue
        #endif
        for p2 in range(0,Deg[2]+1):
            if (IV==2):
                print("c["+str(p1)+str(p2)+"]="+str(C[l]))
                l=l+1
                continue
            #endif
            for p3 in range(0,Deg[3]+1):
                if (IV==3):
                    print("c["+str(p1)+str(p2)+str(p3)+"]="+str(C[l]))
                    l=l+1
                    continue
                #endif
                for p4 in range(0,Deg[4]+1):
                    if (IV==4):
                        print("c["+str(p1)+str(p2)+str(p3)+str(p4)+"]="+str(C[l]))
                        l=l+1
                        continue
                    #endif
                    for p5 in range(0,Deg[5]+1):
                        cadenaCoef="c["+str(p1)+str(p2)+str(p3)+str(p4)+str(p5)+"]="+str(C[l])
                        listaCoefAux.append(cadenaCoef)
                        l=l+1
                    #endfor
                #endfor
            #endfor
        #endfor
    #endfor
    return listaCoefAux

def getExternal():
    global Ph_Ndx,Th_Ndx,Mu,bxe,EpsiPh
    EpsiPh=-infinity					    # Initialize external error
    for i in range(M+2,n+1):        # Check for determined elements
        p_x=0
        for j in range(2,M+2):
            prod_j=C[j]*map[i][j]
            p_x=p_x+prod_j              # Calculate "F"
        #endfor
        extErr=map[i][M+2]-p_x	      # External error
        absErr=abs(extErr)         #  Absolute external error
        if (absErr>EpsiPh):        # Check for largest error
            EpsiPh=absErr          # Present external error
            Ph_Ndx=i               # Index of element
            if (extErr<0):
                Mu=-1
            else:
                Mu=+1
            #endif
        #endif
    #endfor
    #print("External: "+str(Ph_Ndx))
    #print("Ep_phi:   "+str(EpsiPh))
#    print("extError: "+str(EpsiPh))
    if (bxe>EpsiPh):
        bxe=EpsiPh
        T[1]=bxe
        for j in range(2,M+2):
            T[j]=C[j]
        #endfor
    #endif
    return

def Converge(errorMin,coeficientes,listaErrores):
    if (EpsiPh<=EpsiTh):
        listaErrores.append(EpsiTh)
        coeficientes.append(generateCoefs())
        listaErrores=sort(len(listaErrores),listaErrores,coeficientes)
        #print("ABSOLUTE")
        return True
    #endif
    diffErr=abs(EpsiTh-PrevTh)
    if (diffErr<10e-8):
        #print("ERROR DIFFERENCE<.00000001 \n\t["+str(diffErr)+"]")
        listaErrores.append(EpsiTh)
        coeficientes.append(generateCoefs())
        listaErrores=sort(len(listaErrores),listaErrores,coeficientes)
        #print("ABSOLUTE")
        return True
    #endif
    if ((EpsiTh<=PrevTh) and (itera>20)):
        for i in range(1,M+1):   #Retain best previous coefficients
            C[i]=T[i]
        #endfor
        listaErrores.append(EpsiTh)
        coeficientes.append(generateCoefs())
        listaErrores=sort(len(listaErrores),listaErrores,coeficientes)
        #print("UNSTABLE")
        return True
    #endif
    return False
#endConverge

def getInternal():
    global Th_Ndx,Ph_Ndx
    # Put external vector as a function of internal vectors
    #Ph_ndx is the number of the vector with largest external error
    for i in range(1,M+2):
        Sum=Mu*Ix[1][i]
        for j in range(2,M+2):
            Sum=Sum+map[Ph_Ndx][j]*Ix[j][i]
        #endfor
        Lambda[i]=Sum
    #endfor
#   Determine which internal vector to swap
    betaMax=-infinity
    for i in range(1,M+2):
        quot=Mu*Lambda[i]/Ix[1][i]
        if (quot>betaMax):
            betaMax=quot
            Th_Ndx=i
        #endif
    #endfor
    #print("Internal: "+str(Th_Ndx))
    #print("Ep_theta: "+str(EpsiTh))
    return

def Swap():
    #print("Swap "+str(Th_Ndx)+" --> "+str(Ph_Ndx))
    T4S=list(range(M+3))
    for i in range(1,M+3):
        T4S[i]=map[Th_Ndx][i]           # From Epsi_Theta
    #endfor
    for i in range(1,M+3):
        map[Th_Ndx][i]=map[Ph_Ndx][i]   # From Epsi_Phi
    #endfor
    for i in range(1,M+3):
        map[Ph_Ndx][i]=T4S[i]           # From Epsi_Theta
    #endfor
    return
#
def NxtInverse():
    for i in range(1,M+2):
        Ix[i][Th_Ndx]=Ix[i][Th_Ndx]/Lambda[Th_Ndx]
    #endfor
    for i in range(1,M+2):
        for j in range(1,M+2):
            if (i!=Th_Ndx):
                Ix[j][i]=Ix[j][i]-Lambda[i]*Ix[j][Th_Ndx]
            #endif
        #endfor
    #endfor
    return

def check_integer_ge1(i):
    while True:
        #print("Give me the degree of independent variable "+str(i))
        try:
            while True:
                x=float(input())
                x=int(x)
                if (x>=1):
                    return x
                #endif
                #print("Degree must be \"1\" or more")
                #print("Try again")
            #endwhile
        except:
            #print("Must be a number")
            #print("Try again")
            nada=True
    ##endWhile
##endFunction  

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
#               MAIN
#
# Y(Mp1),C(Mp1),X(Mp1,Mp1),Sgn(Mp1),Ix(Mp1,Mp1)
# Lamda(Mp1), T(Mp1)
gradMax=int(input("¿Hasta qué grado vas a querer calcular?"))
global errorMin
errorMin=999999999
coeficientes=[]
listaErrores=[]
for vara in range(1,gradMax+1):
    for varb in range(1,gradMax+1):
        for varc in range(1,gradMax+1):
            for vard in range(1,gradMax+1):
                for vare in range(1,gradMax+1):
                    varsAux=[vara,varb,varc,vard,vare]
                    #print("Give me the name of the Data to Analyze: \t")
                    DTA="customTrain.txt"
                    #print(DTA)
                    print("****************************************")
                    print(vara,varb,varc,vard,vare)
                    try:
                        FN = open(DTA,"r")
                        #print("\t***\""+DTA+"\" was opened" )
                    except:
                        #print("\t***\""+DTA+"\" was not found" )
                        sys.exit("**** End of Program ****")
                    #endTrydat
                    Tuples=FN.readlines()
                    n=len(Tuples)
                    print("Tuples:     "+str(n))
                    LineLen=len(Tuples[0])
                    Atribs=NumCols(Tuples[0],LineLen)
                    m=Atribs
                    print("Attributes: "+str(m))
                    print("INDEPENDENT VARIABLES: "+str(m-1))
                    IV=m-1
                    if (IV>MaximumNumberOfIndependentVariables):
                        print("Exceeded number of maximum allowed independent variables")
                        sys.out("***\t\tPROGRAM WILL NOW END\t\t***")
                    #endif
                    print("\tDEPENDENT VARIABLE IS IN COLUMN "+str(m))
                    print()
                    FN = open(DTA,"r")             # REWIND
                    xy=list(range(0,n+1))
                    for i in range(0,n+1):
                        xy[i]=list(range(0,m+1))
                    #
                    #       PON LOS DATOS EN xy[i][j] EN PUNTO FLOTANTE
                    #
                    for i in range(0,n):            # n tuples  (i=0,1,...,n-1)
                        for j in range(0,m):        # m columns (j=0,1,...,m-1)
                            L=Tuples[i]
                            Num=getNum(L,j)         #"Num" is Floating point
                            xy[i+1][j+1]=Num 
                        #endFor
                    #endFor
                    FN.close()
                    if (DEBUG):
                        print("ORIGINAL DATA TUPLES")
                        for i in range(1,n+1):
                            Tuple_i=""
                            for j in range(1,m+1):
                                Tuple_i=Tuple_i+("%6.3f\t" % (xy[i][j]))
                            #endfor
                            print(Tuple_i)
                        #endfor
                        print()
                    #endif
                    Deg=list(range(0,m))
                    for i in range(1,m):
                        Deg[i]=varsAux[i-1]
                    #endfor
                    M=1
                    for i in range(1,m):
                        M=M*(Deg[i]+1)
                    #endFor
                    ################################################
                    Lambda=list(range(M+2))             # Include signs
                    T     =list(range(M+2))             # Include signs
                    ################################################
                    #                 X
                    map=list(range(0,n+1))              # 1,...,n   ; all data
                    for i in range(0,n+1):
                        map[i]=list(range(0,M+3))       # 1,...,M+2 ;Include signs and Function
                    #endFor
                    data2map()
                    #print("There are "+str(M+2)+" attributes, "+str(n)+" tuples in MAP") 
                    #dummy=input("\"ENTER\" to continue\n")
                    if (n<M+1):
                        print("Not enough data")
                        print("At least "+str(M+1)+" tuples are needed")
                        break
                    #endIf 
                    while True:
                        #Resp=input("Do you wish to stabilize the data? (Y/N)").upper()
                        Resp='Y'
                        if (Resp=="Y"):
                            stabilize()
                            break
                        #endif
                        if (Resp=="N"):
                            break
                        #endif
                    #endwhile
                    if (DEBUG):
                        print("DATA MAPPED INTO THE POWERS OF THE INDEPENDENT VARIABLES")
                        for i in range(1,n+1):
                            tuple_i=""
                            for j in range(1,M+3):
                                tuple_i=tuple_i+"%10.6f\t" % (map[i][j])
                            #endfor
                            print(tuple_i)
                        #endfor
                        dummy=input("\"ENTER\" to continue\n")
                    #endif
                    ab=list(range(M))                 #0,1,...,M-1
                    for i in range(M):
                        ab[i]=list(range(M+1))
                    #endfor
                    #
                    #           COPY MATRIX map TO MATRIX ab FOR FirsSigns
                    #
                    for i in range(0,M):
                        for j in range(0,M+1):
                            ab[i][j]=map[j+1][i+2]
                        #endfor
                    #endfor
                    FN = open("Data4Cofactors.xls","w+")
                    for i in range(0,M):
                        ab_j=""
                        for j in range(0,M+1):
                            ab_j=ab_j+str(ab[i][j])+"\t"
                        #endfor
                        ab_j=ab_j+"\n"
                        FN.write(ab_j)
                    #endfor
                    FN.close()
                    cf = list(range(M))
                    if (not FirstSigns()):
                        print("Unstable system")
                        sys.exit()
                    else:
                        if (DEBUG):
                            print("\tMinimax Signs\n")
                        #endif
                        for i in range(0,M):
                            if (cf[i])<0:
                                s_i=-1.
                            else:
                                s_i=+1.
                            #endif
                            if (DEBUG):
                                print("\ts[ %2.0f ] = %10.6f " % (i,s_i))
                            #endif
                            map[i+1][1]=s_i             # Llena la 1a columna de map
                        #endFor
                        if (DEBUG):
                            print("\ts[ %2.0f ] = %10.6f " % (M,-1))
                        #endif
                        map[M+1][1]=-1.
                    #endIf
                    if (DEBUG):
                        dummy=input("\"ENTER\" to continue\n")
                        print("\nDATA FOR MINIMAX APPROXIMATION (INCLUDING SIGNS)")
                        for i in range(1,M+2):
                            tuple_i=""
                            for j in range(1,M+3):
                                tuple_i=tuple_i+"%10.6f\t" % (map[i][j])
                            #endfor
                            print(tuple_i)
                        #endfor
                        dummy=input("\"ENTER\" to continue\n")
                    #endif
                    ii=1                                # Counter of files (Map_i.xls)
                    Ix=list(range(M+2))
                    for i in range(M+2):
                        Ix[i]=list(range(M+2))
                    #endfor
                    FirstInverse()                      # Find inverse matrix (map^-1)
                    C=list(range(M+2))                  # C[M+1]
                    f=list(range(M+2))
                    for i in range(1,M+2):              # f[M+1][M+1]
                        f[i]=map[i][M+2]
                    #endfor
                    for itera in range(1,infinity):
                        if (DEBUG):
                            testInverse()
                            dummy=input("INVERSE HAS BEEN CHECKED; \"ENTER\" to continue\n")
                        #endif
                        getCoefs() 			            # Get Ci's from inner product
                        getExternal()                   # Largest error vector
                        resConverge=Converge(errorMin,coeficientes,listaErrores)
                        if (resConverge):
                            #printCoefs()
                            print("\n**********\n\tALGORITHM HAS CONVERGED\n\tEND OF PROGRAM\n**********")
                            break
                        #endif
                        getInternal()                   # Best Internal vector
                        Swap()                          # Swap internal vs. external
                        FirstInverse()
                    #    NxtInverse()                    # Fast inverse
                    #endfor
                    
                    print("-----------------------------SÍ LLEGUÉ :D----------------------")


test=open("newCustomTest.txt","r")
testTuples=test.readlines()
numTestData=len(testTuples)
listaResultadosCombinaciones=[]
for combinacion in coeficientes:
    listaResultadosTuplas=[]
    for tuplaTest in testTuples:
        datosTest=tuplaTest.split("\t")
        datosTest[4]=datosTest[4][:-1]
        res=0
        for i in range(len(combinacion)):
            auxres=1
            potSplit, coefSplit=combinacion[i].split('=')
            potencias=[int(potSplit[2]),int(potSplit[3]),int(potSplit[4]),int(potSplit[5]),int(potSplit[6])]
            coef=float(coefSplit)
            for j in range(5):
                auxres=auxres*(float(datosTest[j])**potencias[j])
            res=res+(auxres*coef)
        listaResultadosTuplas.append(res)
    listaResultadosCombinaciones.append(listaResultadosTuplas)
test.close()

testResultados=open("customTest.txt","r")
testResultadosTuples=testResultados.readlines()
ultimaColumnaTest=[]
for tupla in testResultadosTuples:
    resAux=tupla.split('\t')
    ultimaColumnaTest.append(float(resAux[5][:-1]))
            
testResultados.close()


listaRMSE=[]

for comb in listaResultadosCombinaciones:
    listaRMSE.append(mean_squared_error(ultimaColumnaTest, comb, squared=False))

indice=listaRMSE.index(min(listaRMSE))

print("********************************")
print("Esta es la \"mejor combinación\" de coeficientes")
print("********************************")
for cof in coeficientes[indice]:
    print(cof)

coefResultados=open("coefResultados.xls", "w+")
coefResultados.write("\n".join(coeficientes[indice]))
coefResultados.close()



