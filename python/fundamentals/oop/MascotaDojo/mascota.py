class Mascota:
    def __init__( self, nombre, tipo , golosinas):
        self.nombre=nombre
        self.tipo=tipo
        self.golosinas=golosinas
        self.energia=100
        self.salud=100

    def dormir(self):
        self.energia+=25

    def comer(self):
        self.energia+=5
        self.salud+=10

    def jugar(self):
        self.energia-=5

    def sonido(self):
        print("woff")

class Gato(Mascota):
    def __init__( self, nombre, golosinas):
        super().__init__(nombre, "gato" , golosinas)

    def sonido(self):
        print("meow")
