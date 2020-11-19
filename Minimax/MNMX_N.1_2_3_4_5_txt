import sys
import random
import math
MaximumNumberOfIndependentVariables=5
DEBUG=False


#
#       INVERT AN MXM MATRIX
#   ON INPUT:
#       "map" ---> MXM MATRIX TO INVERT
#       M=TUPLES/ATRIBS OF "A"
#       "b"   ---> MXM INVERTED MATRIX

def InvertMatrix():
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
            b[i+1][j+1]=ai[i][j]
        #endfor
    #endfor
    return
#endInvertMatrix

#
#       Find the coefficients for (M)X(M+1) system
#           ON INPUT: data is in ab[M][M+1] matrix
#           ON OUTPUT: coefficients are in cf[M]
#
def lassol():
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
#
#	Exchange column with largest element
#
        if (ipiv!=k):
            for i in range(k,M+1):
                temp=ab[k][i]   
                ab[k][i]=ab[ipiv][i]   
                ab[ipiv][i]=temp   
		      #endFor
	     #endIf
#
#	Eliminate all in column except first
#
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
#endLassol

#
#           STABILIZATION
#
def stabilize():
    for i in range(1,n+1):
        for j in range(1,Terms+3):
            if (abs(map[i][j])<10e-6):
                map[i][j]=random.uniform(0,+10e-6)                  #ALMOST 0
            else:
                map[i][j]=map[i][j]*(1+random.uniform(0,+10e-6))    #ALMOST XY[i][1]
            #endif
        #endfor
    #endfor
    return
#endStabilize

def check_integer_ge1(i):
    while True:
        print("Give me the degree of independent variable "+str(i))
        try:
            while True:
                x=float(input())
                x=int(x)
                if (x>=1):
                    return x
                #endif
                print("Degree must be \"1\" or more")
                print("Try again")
            #endwhile
        except:
            print("Must be a number")
            print("Try again")
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
DTA=input("Give me the name of the Data to Analyze: \t")
try:
    FN = open(DTA,"r")
    print("\t***\""+DTA+"\" was opened" )
except:
    print("\t***\""+DTA+"\" was not found" )
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
dummy=input("\"ENTER\" to continue\n")
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
print("ORIGINAL DATA TUPLES")
for i in range(1,n+1):
    Tuple_i=""
    for j in range(1,m+1):
        Tuple_i=Tuple_i+("%6.3f\t" % (xy[i][j]))
    #endfor
    print(Tuple_i)
#endfor
print()
dummy=input("\"ENTER\" to continue\n")
Deg=list(range(0,m))
for i in range(1,m):
    Deg[i]=check_integer_ge1(i)
#endfor
Terms=1
for i in range(1,m):
    Terms=Terms*(Deg[i]+1)
#endFor
#                 X
map=list(range(0,n+1))
for i in range(0,n+1):
    map[i]=list(range(0,Terms+3))       # error+Terms+Dependent variable
#endFor
iv=list(range(m))
for i in range(1,n+1):
    for j in range(1,m):
        iv[j]=xy[i][j]
    #endfor
    k=1
    while k<=Terms:
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
    DEBUG=False
    if (DEBUG):
        print("map["+str(i)+"]["+str(k+1)+"]="+str(map[i][k+1]))
    #endif
#endFor
DEBUG=True
print("There are "+str(Terms+2)+" attributes, "+str(n)+" tuples in MAP") 
dummy=input("\"ENTER\" to continue\n")
stabilize()
if (n<Terms):
    print("Not enough data")
    print("At least "+str(Terms)+" tuples are needed")
    sys.exit()
#endIf 
print("DATA MAPPED INTO THE POWERS OF THE INDEPENDENT VARIABLES")
for i in range(1,n+1):
    tuple_i=""
    for j in range(1,Terms+3):
        tuple_i=tuple_i+"%10.6f\t" % (map[i][j])
    #endfor
    print(tuple_i)
#endfor
dummy=input("\"ENTER\" to continue\n")
ab=list(range(Terms))                 #0,1,...,Terms-1
for i in range(Terms):
    ab[i]=list(range(Terms+1))
#endfor
#
#           MAP DATA TO MATRIX ab FOR lASSOL
#
for i in range(0,Terms):
    for j in range(0,Terms+1):
        ab[i][j]=map[j+1][i+2]
        DEBUG=False
        if (DEBUG):
            print("ab ["+str(i)+"]["+str(j)+"]<--map["+str(j+1)+"]["+str(i+2)+"]")
        #endif
    #endfor
#endfor
DEBUG=True
M=Terms
cf = list(range(M))
if (not lassol()):
    print("Unstable system")
    sys.exit()
else:
    print("\n\tMinimax Signs\n")
    for i in range(0,M):
        if (cf[i])<0:
            s_i=-1.
        else:
            s_i=+1.
        #endif
        print("\ts[ %2.0f ] = %10.6f " % (i,s_i))
        map[i+1][1]=s_i
    #endFor
    print("\ts[ %2.0f ] = %10.6f " % (M,-1))
    map[M+1][1]=-1.
#endIf
dummy=input("\"ENTER\" to continue\n")
print("\nDATA FOR MINIMAX APPROXIMATION")
for i in range(1,M+2):
    tuple_i=""
    for j in range(1,M+3):
        tuple_i=tuple_i+"%10.6f\t" % (map[i][j])
    #endfor
    print(tuple_i)
#endfor
dummy=input("\"ENTER\" to continue\n")
#
#           MAP DATA TO MATRIX ab FOR lASSOL
#
for i in range(0,M):
    for j in range(0,M+1):
        ab[i][j]=map[i+1][j+1]
        DEBUG=False
        if (DEBUG):
            print("ab ["+str(i)+"]["+str(j)+"]<--map["+str(j+1)+"]["+str(i+2)+"]")
        #endif
    #endfor
#endfor
DEBUG=True
cf = list(range(M))
if (not lassol()):
    print("Unstable system")
    sys.exit()
#
b=list(range(M+2))
for i in range(M+2):
    b[i]=list(range(M+2))
#endfor
InvertMatrix()          # b = map^(-1)
if (DEBUG):
    print("MATRIX TO INVERT:")
    for i in range(1,M+2):
        map_i=""
        for j in range(1,M+2):
            map_i=map_i+"%10.6f\t" % (map[i][j])
        #endfor
        print(map_i)
    #endfor
    print("INVERTED MATRIX:")
    for i in range(1,M+2):
        b_i=""
        for j in range(1,M+2):
            b_i=b_i+"%10.6f\t" % (b[i][j])
        #endfor
        print(b_i)
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
                p[i][j]=p[i][j]+map[i][k]*b[k][j] 
            #endfor
        #endfor
    #endfor
    print("PRODUCT OF MATRIX BY ITS INVERTED")
    for i in range(1,M+2):
        P_i=""
        for j in range(1,M+2):
            P_i=P_i+"%10.6f\t" % (p[i][j])
        #endfor
        print(P_i)
    #endfor
#endif
#
#   OBTAIN ERROR AND COEFFICIENTS
#
c=list(range(M+2))
f=list(range(M+2))
for i in range(1,M+2):
    f[i]=map[i][M+2]
#endfor
for i in range(1,M+2):
    c[i]=f[1]*b[i][1]
    for j in range(2,M+2):
        c[i]=c[i]+f[j]*b[i][j]
    #endfor
#endfor
print("\nepsi="+str(c[1]))
l=2
for p1 in range(0,Deg[1]+1):
    if (IV==1):
        print("c["+str(p1)+"]="+str(c[l]))
        l=l+1
        continue
    #endif
    for p2 in range(0,Deg[2]+1):
        if (IV==2):
            print("c["+str(p1)+str(p2)+"]="+str(c[l]))
            l=l+1
            continue
        #endif
        for p3 in range(0,Deg[3]+1):
            if (IV==3):
                print("c["+str(p1)+str(p2)+str(p3)+"]="+str(c[l]))
                l=l+1
                continue
            #endif
            for p4 in range(0,Deg[4]+1):
                if (IV==4):
                    print("c["+str(p1)+str(p2)+str(p3)+str(p4)+"]="+str(c[l]))
                    l=l+1
                    continue
                #endif
                for p5 in range(0,Deg[5]+1):
                    print("c["+str(p1)+str(p2)+str(p3)+str(p4)+str(p5)+"]="+str(c[l]))
                    l=l+1
                #endfor
            #endfor
        #endfor
    #endfor
#endfor
#endfor
#def getCoefs():
#    for i in range(1,Mp1):
#        C(i)=Ix(i,1)*f(1) 
#        for j in range(2,Mp1):
#            C(i)=C(i)+Ix(i,j)*Y(j)
#        #endfor
#    #endfor
#    return
#endgetCoefs
