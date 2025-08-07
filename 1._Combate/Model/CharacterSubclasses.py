from Model.Character import Character
# hp: int, baseDamage: int, probParry: float, probCrit: float
hp = {'low': 90, 'med': 100, 'high': 115}
dmg = {'low': 12, 'med': 15, 'high': 18}
parry = {'low': 0.2, 'med': 0.3, 'high': 0.4}
crit = {'low': 0.2, 'med': 0.3, 'high': 0.4}

class Rogue(Character):
    def __init__(self, name: str):
        super().__init__("Rogue " + name, hp.get('low'), dmg.get('high'), parry.get('low'), crit.get('med'))

    def usarHabilidad(self, objetivo):
        if (self.selectedHab == 1):
            print(f"La vida de {objetivo.name} se ha reducido, pero el daño base de {objetivo.name} ha subido")
            self.hp = self.hp - 15
            objetivo.baseDamage = objetivo.baseDamage + 5
        else:
            print(f"La vida de {objetivo.name} se ha reducido, pero  la defensa de {objetivo.name} ha subido")
            self.hp = self.hp - 20
            objetivo.probParry = objetivo.probParry + 0.15

    def mostrarHabilidad(self): 
        print("1 - Pierdes 15HP pero incrementa el daño base en 5 puntos")
        print("2 - Pierdes 20HP pero incrementa la probabilidad de parry un 15%")

class Tank(Character):
    def __init__(self, name: str):
        super().__init__("Tanque " + name, hp.get('high'), dmg.get('med'), parry.get('high'), crit.get('low'))

    def usarHabilidad(self, objetivo):
        if (self.selectedHab == 1):
            print(f"{objetivo.name} concentra su energía perdida y sube su ataque!")
            objetivo.baseDamage = int(objetivo.baseDamage + (hp.get('high')-objetivo.hp)*0.1)
        else:
            print(f"{objetivo.name} se prepara para el combate, sube daño y crítico")
            objetivo.baseDamage = objetivo.baseDamage + 3
            objetivo.probCrit = objetivo.probCrit + 0.1

    def mostrarHabilidad(self): 
        print("1 - Sube el daño base en proporción a la cantidad HP que ha perdido")
        print("2 - Sube el daño base 5 puntos y la probabilidad de crítico un 10%")

class Wizard(Character):
    def __init__(self, name: str):
        super().__init__("Mago " + name, hp.get('high'), dmg.get('low'), parry.get('high'), crit.get('med'))

    def usarHabilidad(self, objetivo):
        if (self.selectedHab == 1):
            if (self.probParry < 0.1):
                print(f"{self.name} ya no tiene energía, la habilidad ha fallado")
                return
            print(f"{objetivo.name} ha recuperado 25HP")
            print(f"{self.name} ha bajado su defensa por el cansancio")
            objetivo.hp = objetivo.hp + 25
            self.probParry = self.probParry - 0.1
        else:
            print(f"{self.name} pone toda su concentración en un ataque devastador!!!")
            objetivo.recibirDanio(self.baseDamage*3, self)
            self.probCrit = 0.0
            self.probParry = 0.0

    def mostrarHabilidad(self): 
        print("1 - Cura 25HP pero reduce tu probabilidad de parry")
        print("2 - Carga un ataque devastador contra tu objetivo, pero ya no podrás hacer críticos ni parrys")

class Paladin(Character):
    def __init__(self, name: str):
        super().__init__("Paladín " + name, hp.get('high'), dmg.get('low'), parry.get('high'), crit.get('low'))

    def usarHabilidad(self, objetivo):
        if (self.selectedHab == 1):
            if (self.probParry < 0.1):
                print(f"{self.name} ya no tiene energía, la habilidad ha fallado")
                return
            objetivo.recibirDanio(self.baseDamage*1.8, self)
            self.probParry = self.probParry - 0.1
            print(f"{self.name} ha bajado su defensa por el cansancio")
        else:
            print(f"{self.name} se concentra y sube su capacidad ofensiva")
            self.baseDamage = self.baseDamage + 3

    def mostrarHabilidad(self): 
        print("1 - Concentra energía en un ataque fuerte, pero reduce un poco tu defensa")
        print("2 - Sube en 3 puntos tu daño base sin penalizaciones")