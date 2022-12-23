import mascota

class Ninja:
    def __init__( self,nombre, apellido, premios, comidaMascota, mascota ):
        self.nombre=nombre
        self.apellido=apellido
        self.premios=premios
        self.comidaMascota=comidaMascota
        self.mascota=mascota

    def caminar(self):
        print(f"Vas de paseo con {self.mascota.nombre}")
        self.mascota.jugar()

    def alimentar(self):
        if len(self.comidaMascota)>0:
            print(f"alimentando a {self.mascota.nombre} con {self.comidaMascota.pop()}")
            self.mascota.comer()
        else:
            print("oh no! necesitas mas comida")

    def bañar(self):
        print(f"Limpias a {self.mascota.nombre} ")
        self.mascota.sonido()





mascota1 = mascota.Mascota("paco","perro","galleta");
ninja1= Ninja("juan","perez","galleta",["Pienzo","pizza"],mascota1)
ninja1.caminar()
ninja1.alimentar()
ninja1.alimentar()
ninja1.alimentar()
ninja1.bañar()
mascota2 = mascota.Gato("pimienta","leche")
ninja2= Ninja("juan","perez","galleta",["Pienzo","pizza"],mascota2)
ninja2.caminar()
ninja2.alimentar()
ninja2.alimentar()
ninja2.alimentar()
ninja2.bañar()