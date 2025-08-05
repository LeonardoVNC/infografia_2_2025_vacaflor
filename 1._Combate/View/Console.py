import os
import time

class Console:
    def cls(self):
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def inputInt(self, msg: str):
        try:
            return int(input(msg))
        except ValueError:
            print("Ingrese un número válido por favor")
            return 