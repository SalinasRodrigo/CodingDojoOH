def countdown(num):
    arry=[]
    for i in range(num,-1,-1):
        arry.append(i)
    return arry

def imprimirYdevolver(arry):
    print(arry[0])
    return arry[1]

def primeroYlongitud(arry):
    return arry[0]+ len(arry)

def mayoresSegundos(arry):
    if(len(arry)<=2):
        return False

    newArry=[]
    for i in arry:
        if (i>arry[1]):
            newArry.append(i)
    print(len(newArry))
    return newArry

def longituValor(l,v):
    arry=[]
    for i in range(l):
        arry.append(v)
    
    return arry

arry=countdown(5)
print(arry)
arry=[1,2]
x=imprimirYdevolver(arry)
print(x)
arry=[1,2,3,4,5]
print(primeroYlongitud(arry))
arry=[5,2,3,2,1,4]
print(mayoresSegundos(arry))
arry=[5]
print(mayoresSegundos(arry))
print(longituValor(4,7))
print(longituValor(6,2))
