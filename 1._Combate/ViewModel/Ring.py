import random
from Model.Character import Character
from View.Console import Console
from Model.CharacterSubclasses import *

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
        
        self.num_turns = self.cons.inputInt("Cuántas rondas máximo planean jugar??\n")
        if (self.num_turns < 1):
            print("Dale hermano, mínimo 1 turno pues")
            self.num_turns = 1
        if (self.num_turns > 100):
            print("Dudo que llegue a tanto... pero tu mandas")
        self.cons.cls()

        self._setCharacters()
        
    def _setCharacters(self):
        for i in range(self.num_players):
            print("Empecemos a crear el PJ del jugador",i+1)

            charaName = input("Qué nombre tendrá el personaje?\n")
            self.cons.cls();

            charaClass = self.cons.inputInt("Qué clase de PJ quiere?\n1 - Rogue\n2 - Tank\n3 - Wizard\n4 - Paladin\n")
            if (charaClass < 1 or charaClass > 4):
                print("Jaja por chistoso te pongo una al azar >:c")
                charaClass = random.randint(1,4)
            self.cons.cls();

            currenctChara: Character
            if (charaClass == 1):
                #Rogue
                currenctChara = Rogue(charaName)
            elif (charaClass == 2):
                #Tank
                currenctChara = Tank(charaName)
            elif (charaClass ==3):
                #Wizard
                currenctChara = Wizard(charaName)
            elif (charaClass == 4):
                #Paladin
                currenctChara = Paladin(charaName)

            print("Selecciona la habilidad que tendrá tu PJ:")
            currenctChara.mostrarHabilidad()
            selectedHab = self.cons.inputInt("")
            if (selectedHab < 1 or selectedHab > 2):
                print("Jaja por chistoso te pongo una al azar >:c")
                selectedHab = random.randint(1,2)
            currenctChara.setHab(selectedHab)
            self.cons.cls();

            self.players.insert(i,currenctChara)

            print("Listo el PJ para el jugador",i+1)
            self.cons.cls()
        print("Terminada la creación de PJs :D")
        self.cons.cls();

        self._beginGame()
    
    def _beginGame(self):
        print("Iniciando la partida, en sus puestos!")
        self.cons.cls();
        for turn in range(1, self.num_turns):
            print("Iniciando Ronda",turn)
            self.cons.cls()
            self._playTurn()
            
            print("Resumen:")
            self._updatePlayers()
            self.cons.wait()

            if(self.num_players == 1):
                print(f"El último PJ en pie es {self.players[0].name}!!!")
                self.cons.endGame()
            if(self.num_players == 0):
                print(f"Increible, hemos llegado a un empate!!!")
                self.cons.endGame()

            print("Fin de la Ronda",turn)
            self.cons.cls()
        print("Se ha alcanzado el máximo de rondas")
        max: Character = self.players[0]
        for i in self.players:
            if (i.hp > max.hp):
                max = i
        print(f"El PJ con más vida es {max.name}, felicidades por la victoria!!")

    def _playTurn(self):
        random.shuffle(self.players)
        for i in self.players:
            print("Empieza el turno de",i.name)
            act = self.cons.inputInt(f"Qué hará {i.name} en este turno?\n1 - Atacar\n2 - Usar habilidad\n")
            if (act > 2):
                print("Por gracioso te pongo uno al azar >:c")
                act = random.randint(1,2)
            self.cons.cls()

            msg = f"Quién es el objetivo de {i.name}"
            for j in range(1, self.num_players+1):
                msg = msg+f"\n{j} - {self.players[j-1].name}"
            obj = self.cons.inputInt(msg+"\n")
            if (obj > self.num_players):
                obj = random.randint(1,self.num_players-1)
                print("Por gracioso te pongo uno al azar >:c")
            self.cons.cls()

            if (act == 1):
                i.atacar(self.players[obj-1])
            elif (act == 2):
                i.usarHabilidad(self.players[obj-1])
            self.cons.wait()
            self.cons.cls()

    def _updatePlayers(self):
        alivePlayers: list[Character] = []
        numPlay = 0
        for i in range(0, self.num_players):
            if(not self.players[i].isKO()):
                print(f"A {self.players[i].name} le quedan {self.players[i].hp}HP")
                numPlay = numPlay+1
                alivePlayers.insert(i, self.players[i])
            else:
                print(f"{self.players[i].name} fue debilitado")
        self.players = alivePlayers
        self.num_players = numPlay