import animals

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    def agregar_leon(self, name):
        self.animals.append( animals.Leon(name) )
    def agregar_tigre(self, name):
        self.animals.append( animals.Tigre(name) )
    def agregar_oso(self, name):
       self.animals.append( animals.Oso(name) )
    def imprimir_toda_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.mostrarInfo()
    def alimentarZoo(self):
        for i in self.animals:
            i.alimentar()

zoo1 = Zoo("El zoo de John")
zoo1.agregar_leon("Nala")
zoo1.agregar_leon("Simba")
zoo1.agregar_tigre("Rajah")
zoo1.agregar_tigre("Shere Khan")
zoo1.agregar_oso("Paco")
zoo1.agregar_oso("Juanita")
zoo1.imprimir_toda_info()
zoo1.alimentarZoo()
zoo1.imprimir_toda_info()
