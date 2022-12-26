
# -hacer_liquidación(self, category, porcentaje_descuento): actualiza todos los productos que coinciden con
#  la categoría dada al reducir el precio por el porcentaje_descuento dado (¡usa el método que escribiste en la clase Producto!)
class Tienda:
    def __init__(self, nombre):
        self.nombre=nombre
        self.productos=[]

    def agregarProducto(self, nuevoProducto):
        self.productos.append(nuevoProducto)

    def venderProducto(self, id):
        for i in self.productos:
            if (i.id==id):
                self.productos.remove(i)

    def mostrarStock(self):
        for i in self.productos:
            i.infoProducto()

    def inflacion(self, porcentajeAumento):
        for i in self.productos:
            i.actualizarPrecio(porcentajeAumento, True)

    def hacerLiquidacion(self, categoria, porcentajeDescuento):
        for i in self.productos:
            if(i.categoria==categoria):
                i.actualizarPrecio(porcentajeDescuento, False)

    