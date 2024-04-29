while True:

print("1: Wizard")
print("2: Elf")
print("3: Human")
print("4: Dragon")

character_input = input("Choose your character:")

if character_input == "1":
    character = wizard
    my_hp = wizard_hp
    my_damage = wizard_damage
    break
elif charcter_input == "2":
    character = elf
    my_hp = elf_hp
    my_damage = elf_damage
    break
elif character_input == "3":
    character = human
    my_hp = human_hp
    my_damage = human_damage
else:
    print("Unknown Character")




character = "wizard"
my_hp = "wizard_hp"
my_damage = "wizard_damage"

wizard = "Wizard"
elf = "Elf"
human = "Human"
dragon = "Dragon"

wizard_hp = 80
elf_hp= 100
human_hp = 150
dragon_hp = 300

wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_damage = 50



