class Underscore:
    def map(self, iterable, callback):
        arry=[]
        for i in iterable:
            arry.append(callback(i))
        return arry

    def find(self, iterable, callback):
        for i in iterable:
            if (callback(i)):
                return i

    def filter(self, iterable, callback):
        arry=[]
        for i in iterable:
            if (callback(i)):
                arry.append(i)
        return arry

    def reject(self, iterable, callback):
        arry=[]
        for i in iterable:
            if (not callback(i)):
                arry.append(i)
        return arry

_ = Underscore() 
doble=_.map([1,2,3], lambda x: x*2) # debería devolver [2,4,6]
mayorACuatro=_.find([1,2,3,4,5,6], lambda x: x>4) # debería devolver el primer valor que sea mayor que 4
evens=_.filter([1,2,3,4,5,6], lambda x: x%2==0) # debería devolver [2,4,6]
odd=_.reject([1,2,3,4,5,6], lambda x: x%2==0) # debería devolver [1,3,5]
print(f"Dobles: {doble}, Mayor a catro: {mayorACuatro}, Pares: {evens}, Impares: {odd}")


