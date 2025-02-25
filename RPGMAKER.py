from random import *


class Weapon:
    def __init__(self, name: str, range: tuple, enchantment=None):
        self.name = name
        self.range = range
        self.enchantment = enchantment

    def deal_damage(self):
        # You can add damage boost enchantments here
        base_damage = choice(self.range)
        if self.enchantment == "fire_burst":
            additional_damage = randint(5, 10)
            base_damage += additional_damage
            print(
                f"The {self.name} glows in fiery spirit and adds {additional_damage} damage.")
        elif self.enchantment == "lightning_strike" and randint(0, 10) <= 5:
            additional_damage = 7
            base_damage += additional_damage
            print(
                f"The {self.name} strikes a lightning bolt down and adds 7 damage.")
        elif self.enchantment == "critical_strike":
            if randint(1, 10) <= 3:
                base_damage *= 2
                print("Critical hit! Damage is multiplied by two!")
        return base_damage


class Character:
    def __init__(self, name: str, age: int, hp: int, weapon: Weapon, armour: 'Armour' = None):
        self.name = name
        self.age = age
        self.hp = hp
        self.max_hp = hp
        self.weapon = weapon
        self.armour = armour
        self.strength = 0
        self.inventory = []

    def attack(self, target: 'Character'):
        # You can add enchantments related to the player here
        damage = self.weapon.deal_damage()
        total_damage = damage + self.strength
        if self.weapon.enchantment == "health_stealer":
            if self.hp <= self.max_hp:
                self.hp += 10
                print(
                    f"{self.name}'s {self.weapon.name} has the enchantment HEALTH_STEALER and heals its owner 10 hp.")
        if target.armour is not None:
            total_damage -= target.armour.damage_reduction
            total_damage = max(total_damage, 0)
        target.hp -= total_damage
        target.hp = max(target.hp, 0)
        print(f"{self.name} attacks {target.name} and deals {total_damage} hp to it.")

    def use_potion(self, index: int):
        if 0 <= index < len(self.inventory):
            potion = self.inventory.pop(index)
            potion.use(self)
        else:
            print("Invalid potion index or no potions available.")


class HealthBar:
    def __init__(self, hp: int):
        self.hp = hp
        self.max_hp = hp

    def show(self, bars):
        filled_bars = round(self.hp / self.max_hp * bars)
        empty_bars = bars - filled_bars
        print(f"{'█' * filled_bars}{'_' * empty_bars}")


class Armour:
    def __init__(self, name: str, damage_reduction: int):
        self.name = name
        self.damage_reduction = damage_reduction


class Potion:
    def __init__(self, name: str, effect: str, impact_num: int):
        self.name = name
        self.effect = effect
        self.impact_num = impact_num

    def use(self, target: 'Character'):
        # Add custom potion effects here
        if self.effect == "heal":
            target.hp = min(target.hp + self.impact_num, target.max_hp)
            print(
                f"{target.name} uses {self.name} and increases their health by {self.impact_num}.")
        elif self.effect == "strength":
            target.strength += self.impact_num
            print(
                f"{target.name} uses {self.name} and increases their strength by {self.impact_num}.")
