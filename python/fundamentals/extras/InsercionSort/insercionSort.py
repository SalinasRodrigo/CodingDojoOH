def insercionSort(arry):
    for i in range(len(arry)):
        print("iteracion",i)
        for j in range (i,0,-1):
            if(arry[j]<arry[j-1]):
                arry[j], arry[j-1]=arry[j-1], arry[j]
        print(arry)

arry=[9,6,2,5,7,4,8,1,3]
insercionSort(arry)