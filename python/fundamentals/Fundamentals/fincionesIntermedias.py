def iterateDictionary(dic):
    flag=0
    for i in dic:
        for j in i:
            if(flag==0):
                print(j+" - "+i[j]+", ",end="")
                flag=1
            else:
                print(j+" - "+i[j])
                flag=0
                
def iterateDictionary2(kry_name, dic):
    for i in dic:
        print(i[kry_name])
            
def printInfo(dic):
    keyList=list(dic.keys())
    for i in keyList:
        print('\n')
        print(len(dic[i]),i)
        for j in dic[i]:
            print(j)



x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
print(x)
estudiantes[0]['last_name']='Bryant'
print('\n')
print(estudiantes)
directorio_deportes['fútbol'][0]='Andrés'
print('\n')
print(directorio_deportes)
z[0]['y']=30
print('\n')
print(z)

estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary(estudiantes)
print('\n')
iterateDictionary2('first_name', estudiantes)
print('\n')
iterateDictionary2('last_name', estudiantes)
dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)