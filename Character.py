import random
from helper import d, fancy

# Create a video game-like program. With different character types and abilities.

class Character():

    def __init__(self, name, hp, defense, exp= 0, lvl= 1):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.exp = exp
        self.lvl = lvl
        self.base_dmg = 15

    def still_alive(self):
        '''Returns -> True if a character's HP is > 0, False if character HP is <= 0 (dead)'''
        return self.hp > 0
        
    def defeated(self, target): # perhaps unnecessary
        if target.hp <= 0:
            print(f"{self.name} has defeated {target.name}!!! *****FATALITY*****")

    def attack(self, target):
        if not target.still_alive():
            print(f"{target.name} is already dead!!! X_X")
            return
        print(f"{self.name} just attacked {target.name}!")
        damage = self.calculate_damage()
        target.hp -= damage
        self.defeated(target)
        self.exp += 20
        print(f"{self.name} inflicted {damage} damage!")
        print(f"{target.name} HP: {target.hp}")
        fancy()
        self.get_info()
        d()
        self._exp_check()

    def calculate_damage(self):
        '''Randomize damage based on base damage and considers critical hit.'''
        # randomize damage based off of base damage
        damage = random.randint(self.base_dmg - 5, self.base_dmg + 5)
        if self.critical_hit():
            damage *= 2
            print(f"{self.name} made a critical hit!")
            return damage
        return damage

    def _exp_check(self): # protected method
        '''Level up if experience exceeds 100.'''
        if self.exp > 100:
            self.exp -= 100
            self.lvl += 1
            self.hp += 10
            self.base_dmg += 5
            print(f"{self.name} just gained a level!\n")
            self.get_info()
            
    # Getter for character info
    def get_info(self):
        '''Display character information.'''
        print(f"{self.name}'s current level: {self.lvl}")
        print(f"{self.name}'s current HP: {self.hp}")
        print(f"{self.name}'s current exp: {self.exp}")

    def critical_hit(self):
        # 15% chance of a critical hit
        return random.random() < 0.15


# if __name__ == "__main__":
