class Usuario:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.cuentas=[CuentaBancaria(0.01,0)]

    def deposito(self, amount,i):
        self.cuentas[i-1].balance+=amount
        return self

    def retiro(self, amount,i):
        self.cuentas[i-1].balance-=amount
        return self

    def mostrarBalanceUsuario(self):
        print(f"Nombre: {self.name}")
        j=1
        for i in self.cuentas:
            print (f"Balance cuenta {j}: {i.balance}")
            j+=j
        return self

    def mostrarBalanceCuenta(self,i):
        print(f"Baclance cuenta {i}: {self.cuentas[i-1].balance}")
        return self
    
    def nuevaCuenta(self,interes,balance):
        self.cuentas.append(CuentaBancaria(interes,balance))
        return self

class CuentaBancaria:
    # ¡No olvides agregar algunos valores predeterminados para estos parámetros!
    cuentasClase = []
    def __init__(self, tasaInteres, balance): 
        self.balance=balance
        self.tasaInteres=tasaInteres
        CuentaBancaria.cuentasClase.append(self)

    def generarInteres(self):
        self.balance+=(self.balance*self.tasaInteres)
        return self

    @classmethod
    def ifoCuentas(cls):
        for i in cls.cuentasClase:
            print(f"Balance: ${i.balance} Interes: {int(100*i.tasaInteres)}%")

usuario1=Usuario("pedro","pedro@gmail.com")
usuario1.mostrarBalanceUsuario().deposito(1000,1).retiro(600,1).mostrarBalanceUsuario().nuevaCuenta(0.02,600).mostrarBalanceUsuario()
usuario1.mostrarBalanceCuenta(1)
usuario1.cuentas[0].generarInteres()
usuario1.mostrarBalanceCuenta(1)