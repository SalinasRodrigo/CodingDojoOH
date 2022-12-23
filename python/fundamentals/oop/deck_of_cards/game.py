from classes.deck import Deck
from classes.jugador import Jugador
from classes.jugador import Crupier
import os



def jugar():
    bicycle = Deck()
    jugador1 = Jugador()
    crupier1 = Crupier(bicycle)
    bicycle.barajar()
    bicycle.barajar()
    bicycle.barajar()
    terminado=False

    while(not terminado):
        crupier1.repartir(jugador1)
        if(crupier1.valorMano<17 and crupier1.valorMano2<17 ):
            crupier1.repartir(crupier1)
            
        imprimirMesa(jugador1,crupier1)

        resultado=victoria(jugador1)
        if (resultado==0):
            print("Juego terminado, ¡Ganaste!")
            terminado=True
            break
        if (resultado==1):
            print("Juego terminado, gana la casa")
            terminado=True
            break

        resultado=victoria(crupier1)
        if (resultado==0):
            print("Juego terminado, gana la casa")
            terminado=True
            break
        if (resultado==1):
            print("Juego terminado, ¡Ganaste!")
            terminado=True
            break
        

        repsuesta = input("Desea otra carta? s/n")
        if(repsuesta=="n"):
            while (crupier1.valorMano<17 and crupier1.valorMano2<17 ):
                crupier1.repartir(crupier1)
                imprimirMesa(jugador1,crupier1)
                os.system("Pause")
                resultado=victoria(crupier1)
                if (resultado==0):
                    print("Juego terminado, gana la casa")
                    terminado=True
                    break
                if (resultado==1):
                    print("Juego terminado, ¡Ganaste!")
                    terminado=True
                    break
            if(not terminado):
                if (crupier1.valorMano<crupier1.valorMano2 and crupier1.valorMano2<22):
                    crupier1.valorMano=crupier1.valorMano2

                if(jugador1.valorMano>crupier1.valorMano or jugador1.valorMano2>crupier1.valorMano ):
                    print("Juego terminado, ¡Ganaste!")
                    terminado=True
                else:
                    print("Juego terminado, gana la casa")
                    terminado=True 

            break

def imprimirMesa(jugador, crupier):
    print("\nMesa:")
    for i in crupier.mano:
        print(i.string_val,"of",i.suit, end="\t")

    print("\nMano:")
    for i in jugador.mano:
        print(i.string_val,"of",i.suit, end="\t")
    print("Fichas: ",jugador.fichas)
    
def victoria(jugador):
    if(jugador.valorMano==21 or jugador.valorMano2==21):
        return 0
    if(jugador.valorMano>21 and jugador.valorMano2>21):
        return 1
    return 2



jugar()
        

        
    


