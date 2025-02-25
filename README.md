# RPGMAKER.py - A Text-Based RPG Framework

Welcome to **RPGMAKER.py**, a simple yet powerful text-based RPG framework built in Python. This project allows you to create characters, weapons, armour, and potions, and simulate turn-based combat between heroes and enemies. It's perfect for learning Python, experimenting with game mechanics, or building your own text-based RPG game.

---

## Features

- **Weapons**: Create weapons with customizable damage ranges and enchantments (e.g., fire burst, lightning strike, critical strike).
- **Characters**: Define characters with attributes like name, age, health points (HP), weapons, and armour.
- **Armour**: Equip characters with armour to reduce incoming damage.
- **Potions**: Use potions to heal, increase strength, or gain other effects during combat.
- **Health Bars**: Visualize character health using ASCII-based health bars.
- **Turn-Based Combat**: Simulate battles between characters with dynamic damage calculations and enchantments.

---

## Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Installation
   ```bash
   git clone https://github.com/Hakerfire1234/RPGMAKER.py.git
   cd RPGMAKER.py
### Importing Module
from RPGMAKER import *
### Making Custom Objects
sword = Weapon("Sword", (7, 10))
hero = Character("Hero", 18, 200, sword)
health_potion = Potion("Health Potion", "heal", 50)
hero.inventory.append(health_potion)
### Simulating Combat
enemy = Character("Enemy", 18, 200, Weapon("Fists", (2, 3)))
while hero.hp > 0 and enemy.hp > 0:
    hero.attack(enemy)
    enemy.attack(hero)
