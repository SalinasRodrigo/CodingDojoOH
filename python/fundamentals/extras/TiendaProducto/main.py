from classes.producto import Producto
from classes.tienda import Tienda


tienda1 = Tienda("Jose'i")
leche = Producto("Leche", 5000, "Lacteo")
queso = Producto("Queso", 10000, "Lacteo")
pan = Producto("Pan", 3000, "Panificado")
jamon = Producto ("Jamon", 9000, "Carnico")

tienda1.agregarProducto(leche)
tienda1.agregarProducto(queso)
tienda1.agregarProducto(pan)
tienda1.agregarProducto(jamon)
tienda1.mostrarStock()
tienda1.venderProducto(2)
print("")
tienda1.mostrarStock()
print("")
tienda1.inflacion(0.02)
tienda1.mostrarStock()
print("")
tienda1.hacerLiquidacion("Lacteo", 0.02)
tienda1.mostrarStock()