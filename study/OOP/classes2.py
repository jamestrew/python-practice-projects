class Character(object):
    num_chars = 0

    def __init__(self, name):
        self.health = 100
        self.name = name

        Character.num_chars += 1

    def __str__(self):
        return f"Name: {self.name} | HP: {self.health}"

    @staticmethod
    def countChars():
        print(Character.num_chars)


class Blacksmith(Character):
    def __init__(self, name, forgeName):
        super().__init__(name)
        self.forge = Forge(forgeName)


class Forge:
    def __init__(self, forgeName):
        self.name = forgeName


class NPC(Character):
    def __init__(self, name, faction):
        super().__init__(name)
        self.faction = faction  # enemy or friendly

        if self.faction == "Enemy":
            self.attackDamage = 5
        else:
            self.attackDamage = 4

    def attack(self, other):
        other.health -= self.attackDamage
        print(self.name, "dealt", self.attackDamage, "damage to", other.name)


class PC(Character):
    def __init__(self, name, class_type, weapon_type):
        super().__init__(name)
        self.class_type = class_type
        self.weapon = Weapon(weapon_type)


class Weapon():
    def __init__(self, weapon_type):
        self.name = weapon_type


bs = Blacksmith("Bob", "Rick's Forge")
print(bs)
print(bs.forge.name)


James = PC("James", "Druid", "Bow")
print(James)

orc = NPC("smegal", "Enemy")
print(orc)

orc.attack(James)
print(James)

print(James.weapon.name)
Character.countChars()
