
class Usuario:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.balanceCuenta=0

    def hacerRetiro(self, amount):
        self.balanceCuenta-=amount

    def mostrarBalanceUsuario(self):
        print(f"Usuario:{self.name}, Balance: ${self.balanceCuenta}")

    def transferDinero(self,otherUser,amount):
        self.balanceCuenta-=amount
        otherUser.balanceCuenta+=amount

    def hacerDepósito(self, amount):
    	self.balanceCuenta += amount

usuario1=Usuario("Martin","marti@gmail.com")
usuario2=Usuario("Adrian","adrian@gmail.com")
usuario3=Usuario("Maria","maria@gmail.com")
usuario1.hacerDepósito(100)
usuario1.hacerDepósito(200)
usuario1.hacerDepósito(300)
usuario1.hacerRetiro(150)
usuario1.mostrarBalanceUsuario()
usuario2.hacerDepósito(100)
usuario2.hacerDepósito(200)
usuario2.hacerRetiro(50)
usuario2.hacerRetiro(200)
usuario2.mostrarBalanceUsuario()
usuario3.hacerDepósito(800)
usuario3.hacerRetiro(200)
usuario3.mostrarBalanceUsuario()
usuario1.transferDinero(usuario3, 50)
usuario3.transferDinero(usuario2, 300)
usuario3.transferDinero(usuario1, 50)
usuario1.mostrarBalanceUsuario()
usuario2.mostrarBalanceUsuario()
usuario3.mostrarBalanceUsuario()


