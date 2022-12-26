
class Producto:
    id=0
    def __init__(self, nombre, precio, categoria):
        self.nombre=nombre
        self.precio=precio
        self.categoria=categoria
        self.id=Producto.id
        Producto.id+=1

    def actualizarPrecio(self, cambioPorcentaje, elevado):
        if(elevado):
            self.precio+=(self.precio*cambioPorcentaje)
        else:
            self.precio-=(self.precio*cambioPorcentaje)

    def infoProducto(self):
        print(f"{self.nombre}, precio: G{self.precio}, categoria: {self.categoria}, id: {self.id}")
