def one2hundredfifty():
    for i in range(0,151):
        print(i)

def multiplo5():
    for i in range(5,1001):
        if(i%5==0):
            print(i)

def contarCDJ():
    str=""
    for i in range(0,101):
        if(i%10==0):
            print("Coding Dojo")
        elif(i%5==0):
            print("Coding")
        else:
            print(i)
    pass

def impares():
    sum=0
    for i in range(0,500000):
        if(i%2!=0):
            sum+=i
    print(sum)

def cuentaRegresiva():
    for x in range(2018, 0,-4):
        print(x) 

def contadorFlexible(lowNum,highNum,mult):
    for i in range(lowNum,highNum+1):
        if(i%mult==0):
            print(i)
    pass

one2hundredfifty()
multiplo5()
contarCDJ()
impares()
cuentaRegresiva()
contadorFlexible(2,9,3)