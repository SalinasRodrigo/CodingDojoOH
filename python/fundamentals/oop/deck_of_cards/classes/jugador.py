from . import deck

class Jugador:

    def __init__(self):
        
        self.mano = []
        self.fichas = 1000
        self.valorMano=0
        self.valorMano2=0

    def recibirCarta(self, carta):
        self.mano.append(carta)

    def recibirFicha(self, ficha):
        self.fichas+=ficha

    def darFicha(self, ficha):
        self.fichas-=ficha

    def aumentarValor(self, valor):
        if(valor>10):
            self.valorMano+=10
            self.valorMano2+=10

        elif(valor==1):
            self.valorMano+=1
            self.valorMano2+=11
        else:
            self.valorMano+=valor
            self.valorMano2+=valor


class Crupier (Jugador):
    def __init__(self, deck):
        super().__init__()
        self.deck=deck

    def repartir(self, jugador):
        jugador.recibirCarta(self.deck.cards.pop())
        jugador.aumentarValor(jugador.mano[-1].point_val)
     