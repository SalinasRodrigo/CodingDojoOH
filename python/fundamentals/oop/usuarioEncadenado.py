
class Usuario:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.balanceCuenta=0

    def hacerDeposito(self, amount):
        self.balanceCuenta += amount
        return self

    def hacerRetiro(self, amount):
        self.balanceCuenta-=amount
        return self

    def mostrarBalanceUsuario(self):
        print(f"Usuario:{self.name}, Balance: ${self.balanceCuenta}")
        return self
    
    @property    
    def transferDinero(self,otherUser,amount):
        self.balanceCuenta-=amount
        otherUser.balanceCuenta+=amount
        return self
    
        
    

usuario1=Usuario("Martin","marti@gmail.com")
usuario2=Usuario("Adrian","adrian@gmail.com")
usuario3=Usuario("Maria","maria@gmail.com")

usuario1.hacerDeposito(100).hacerDeposito(200).hacerDeposito(300).hacerRetiro(150).mostrarBalanceUsuario()
usuario2.hacerDeposito(100).hacerDeposito(200).hacerRetiro(50).hacerRetiro(200).mostrarBalanceUsuario()
usuario3.hacerDeposito(800).hacerRetiro(200).mostrarBalanceUsuario()
usuario1.transferDinero(usuario3, 50).mostrarBalanceUsuario()
usuario3.mostrarBalanceUsuario()