class CuentaBancaria:
    # ¡No olvides agregar algunos valores predeterminados para estos parámetros!
    cuentasClase = []
    def __init__(self, tasaInteres, balance): 
        self.balance=balance
        self.tasaInteres=tasaInteres
        CuentaBancaria.cuentasClase.append(self)
        
        
    def deposito(self, amount):
        self.balance+=amount
        return self

    def retiro(self, amount):
        self.balance-=amount
        return self

    def mostrar_info_cuenta(self):
        print(f"Balance: ${self.balance}")
        return self

    def generarInteres(self):
        self.balance+=(self.balance*self.tasaInteres)
        return self

    @classmethod
    def ifoCuentas(cls):
        for i in cls.cuentasClase:
            print(f"Balance: ${i.balance} Interes: {int(100*i.tasaInteres)}%")


cuenta1=CuentaBancaria(0.01,100)
cuenta2=CuentaBancaria(0.03,250)
cuenta1.deposito(100).deposito(50).deposito(50).retiro(140).generarInteres().mostrar_info_cuenta()
cuenta2.deposito(150).deposito(100).retiro(60).retiro(20).retiro(10).retiro(50).generarInteres().mostrar_info_cuenta()
CuentaBancaria.ifoCuentas()