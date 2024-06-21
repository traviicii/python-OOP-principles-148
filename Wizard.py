from Character import Character
from helper import d, fancy

class Wizard(Character):
    
    def __init__(self, name, hp, defense, mana, exp= 0, lvl= 1):
        super().__init__(name, hp, defense, exp= 0, lvl= 1)
        self.mana = mana

    def cast_fireball(self, target):
        damage = self.calculate_damage()
        print(f"{self.name} casts fireball on {target.name}")
        target.hp -= damage
        self.mana -= 15
        self.get_info()
        d()
        print("\n")



gandalf = Wizard("Gandalf", 100, 100, 100)
saruon = Wizard("Sauron", 100, 100, 100)

# gandalf.attack(saruon)
# gandalf.attack(saruon)
# gandalf.cast_fireball(saruon)
# gandalf.attack(saruon)
# gandalf.cast_fireball(saruon)
# gandalf.attack(saruon)
# gandalf.attack(saruon)
# gandalf.cast_fireball(saruon)
# gandalf.attack(saruon)
# gandalf.attack(saruon)
# gandalf.attack(saruon)

gandalf.cast_fireball(saruon)
gandalf.cast_fireball(saruon)
gandalf.cast_fireball(saruon)
gandalf.cast_fireball(saruon)
gandalf.cast_fireball(saruon)