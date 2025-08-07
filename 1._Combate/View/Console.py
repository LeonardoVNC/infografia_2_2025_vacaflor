import os
import time
import sys

class Console:
    def cls(self):
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

    def wait(self):
        input("\nPresione enter para continuar\n")
    
    def inputInt(self, msg: str):
        try:
            return int(input(msg))
        except ValueError:
            print("Ingrese un número válido por favor")
            print("Cerrando programa")
            sys.exit()
        
    def endGame(self):
        print("Fin de la partida!")
        sys.exit()