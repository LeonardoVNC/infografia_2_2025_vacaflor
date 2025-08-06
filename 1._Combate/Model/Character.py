import random
from abc import ABC, abstractmethod

class Character(ABC):
    name: str
    knockOut: bool = False
    hp: int
    baseDamage: int
    probParry: float
    probCrit: float
    selectedHab: int

    def isKO (self):
        return self.knockOut
    
    def setHab (self, hab: int):
        self.selectedHab = hab

    def __init__(self, name: str, hp: int, baseDamage: int, probParry: float, probCrit: float):
        self.name = name
        self.hp = hp
        self.baseDamage = baseDamage
        self.probParry = probParry
        self.probCrit = probCrit

    def atacar(self, rival):
        poder = self.baseDamage
        prob = random.random()
        if (prob < self.probCrit):
            print(f"{self.name} prepara un ataque crítico!")
            poder = poder*2
        print(f"{self.name} ataca a {rival.name} por {poder} puntos de daño!")
        rival.recibirDanio(poder, self)

    def recibirDanio(self, dmg: int, rival):
        prob = random.random()
        if (prob < self.probParry):
            print(f"{self.name} le hizo tremendo parry al ataque de {rival.name}!!")
            return
        print(f"{self.name} es impactado por el ataque")
        self.hp = self.hp - dmg
        if (self.hp < 0):
            self.hp = 0
        print(f"A {self.name} le quedan {self.hp}HP")
        if (self.hp == 0):
            print(f"{self.name} se ha debilitado")
            self.knockOut = True
        
    @abstractmethod
    def usarHabilidad(self, objetivo): 
        pass
