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
        print("TODO")

class Tank(Character):
    def __init__(self, name: str):
        super().__init__("Tanque " + name, hp.get('high'), dmg.get('med'), parry.get('high'), crit.get('low'))

    def usarHabilidad(self, objetivo):
        print("TODO")

class Wizard(Character):
    def __init__(self, name: str):
        super().__init__("Mago " + name, hp.get('high'), dmg.get('low'), parry.get('high'), crit.get('med'))

    def usarHabilidad(self, objetivo):
        print("TODO")

class Paladin(Character):
    def __init__(self, name: str):
        super().__init__("Paladín " + name, hp.get('high'), dmg.get('low'), parry.get('high'), crit.get('low'))

    def usarHabilidad(self, objetivo):
        print("TODO")