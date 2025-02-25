from RPGMAKER import *
import time

# Create weapons
sword = Weapon("Sword", (7, 10))
flame_sword = Weapon("Flame Sword", (7, 10), "fire_burst")
fists = Weapon("Fists", (2, 3))
health_bow = Weapon("Health Bow", (5, 6), "health_stealer")
axe = Weapon("Axe", (2, 20))
thors_hammer = Weapon("Thor's Hammer", (5, 12), "lightning_strike")
critical_sword = Weapon("Critical Sword", (7, 10), "critical_strike")

# Create Armour
diamond_armour = Armour("Diamond Armour", 5)

# Create characters
Hero = Character("Hero", 18, 200, axe, diamond_armour)
Enemy = Character("Enemy", 18, 200, thors_hammer)

# Create health bars
hero_health = HealthBar(Hero.hp)
enemy_health = HealthBar(Enemy.hp)

# Create potions
health_potion = Potion("Health Potion", "heal", 50)
strength_potion = Potion("Strength Potion", "strength", 10)

# Add potions to Hero's inventory
Hero.inventory.append(health_potion)
Hero.inventory.append(strength_potion)

while Hero.hp > 0 and Enemy.hp > 0:
    print("\n=== Hero's Turn ===")
    print("1. Attack")
    print("2. Use Potion")
    choice = input("Choose an action: ")

    if choice == "1":
        Hero.attack(Enemy)
    elif choice == "2":
        if Hero.inventory:
            print("Choose a potion to use:")
            for i, potion in enumerate(Hero.inventory):
                print(f"{i + 1}. {potion.name}")
            potion_choice = int(input("Enter the number of the potion: ")) - 1
            Hero.use_potion(potion_choice)
        else:
            print("You have no potions!")
    else:
        print("Invalid choice. You lose your turn.")

    print("Enemy Health:")
    enemy_health.hp = Enemy.hp
    enemy_health.show(10)

    if Enemy.hp <= 0:
        break

    print("\n=== Enemy's Turn ===")
    Enemy.attack(Hero)
    print("Hero Health: ")
    hero_health.hp = Hero.hp
    hero_health.show(10)

    time.sleep(1)  # Add a delay between attacks

if Hero.hp > 0:
    print(f"{Hero.name} wins!")
else:
    print(f"{Enemy.name} wins!")