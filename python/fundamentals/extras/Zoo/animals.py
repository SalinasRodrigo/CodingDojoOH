
class Animal:
    def __init__(self, name) -> None:
        self.name=name
        self.salud=100
        self.felicidad=10

    def mostrarInfo(self):
        print(f"{self.name} Salud: {self.salud} Felicidad: {self.felicidad}")
    
class Leon(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.salud=110
        self.felicidad=20

    def alimentar(self):
        self.salud+=10
        self.felicidad+=5
        
class Tigre(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.salud=100
        self.felicidad=50

    def alimentar(self):
        self.salud+=20
        self.felicidad+=1
    
class Oso(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.salud=150
        self.felicidad=10

    def alimentar(self):
        self.salud+=5
        self.felicidad+=15
