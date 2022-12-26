class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result+=num
        for i in nums:
            self.result+=i
        return self

    def subtract(self, num, *nums):
        self.result-=num
        for i in nums:
            self.result-=i
        return self
# crear una instancia:
md = MathDojo()
# para probar:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# debería imprimir 5
x = md.add(1,3,2,1).add(1).result
print(x)
x= md.subtract(2,3,1,5,1).subtract(10).result
print(x)


# ejecuta cada uno de los métodos unas cuantas veces más y verifica el resultado

