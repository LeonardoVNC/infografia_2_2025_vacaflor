import random
from Model.Character import Character
from View.Console import Console

class Ring:
    num_players = 0
    num_turns = 0
    players: list[Character] = []
    cons = Console()

    def standReady (self):
        self.num_players = self.cons.inputInt("Cuántos jugadores van a entrar a la partida?\n")
        if (self.num_players > 4):
            print("El máximo de jugadores es 4... asi que digamos que 4...")
            self.num_players = 4
        if (self.num_players < 2):
            print("El mínimo de jugadores es 2... asi que digamos que 2...")
            self.num_players = 2
        self.cons.cls()
        
        self.num_turns = self.cons.inputInt("Cúantas rondas máximo planean jugar??\n")
        if (self.num_turns < 1):
            print("Dale hermano, mínimo 1 turno pues")
            self.num_turns = 1
        if (self.num_turns > 100):
            print("Dudo que llegue a tanto... pero tu mandas")
        self.cons.cls()

        self._setCharacters()
        
    def _setCharacters(self):
        for i in range(1, self.num_players+1):
            print("Empecemos a crear el PJ del jugador",i)

            charaName = input("Qué nombre tendrá el personaje?\n")
            self.cons.cls();

            charaClass = self.cons.inputInt("Qué clase de PJ quiere?\n1 - Rogue\n2 - Tank\n3 - Wizard\n4 - Paladin\n")
            if (charaClass < 1 or charaClass > 4):
                print("Jaja por chistoso te pongo una al azar >:c")
                charaClass = random.randint(1,4)
            self.cons.cls();

            #currentChar: Character = Character() Metele las subclases aca
            print("Listo el PJ para el jugador",i)
            self.cons.cls()
        print("Terminada la creación de PJs :D")
        self.cons.cls();
        
