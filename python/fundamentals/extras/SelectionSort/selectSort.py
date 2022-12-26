import math
def selectSort(arry):
    
    for j in range(len(arry)):
        minimo= math.inf
        pos=0
        print("iteracion",j)
        for i in range(j,len(arry)):
            if(arry[i]<minimo):
                minimo=arry[i]
                pos=i
        aux=arry[j]
        arry[j]=arry[pos]
        arry[pos]=aux
        print(arry)

arry=[9,6,2,5,7,4,8,1,3]
selectSort(arry)