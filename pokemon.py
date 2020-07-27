class Pokemon:
    def __init__(self, name, level, type, max_HP, current_HP, knocked_out):
        self.type = type
        self.weaknesses = {"Fire": "Water", "Water": "Grass", "Grass": "Fire", "Ground": "Flying", "Poison":"Ground","Electric":"Dragon","Dark":"Psychic"}
        self.weakness = self.weaknesses.get(self.type)
        self.resistances = {value: key for key, value in self.weaknesses.items()}
        self.resistance = self.resistances.get(self.type)
        self.name = name
        self.level = level
        self.max_HP = max_HP
        self.current_HP = current_HP
        self.knocked_out = knocked_out

    def lose_health(self, damage_dealt):
        self.current_HP -= damage_dealt
        if self.current_HP <= 0:
            self.knocked_out = True
            print("{} was knocked out. RIP".format(self.name))
        else:
            print("{} now has {}/{} health left".format(self.name, self.current_HP, self.max_HP))

    def attack(self, victim, damage):
        if not(self.knocked_out):
            if victim.weakness == self.type:
                damage *= 2
            elif victim.resistance == self.type:
                damage /= 2

            print('{} inflicted {} damage on {}'.format(self.name, damage, victim.name))
            victim.lose_health(damage)
        else:
            print("This pokemon can not attack as it is knocked out :P")

class Trainer:
    def __init__(self,name,pokemen,currently_active,current_pokemon):
        self.name = name
        self.pokemen = pokemen
        self.currently_active = currently_active
        self.current_pokemon = current_pokemon

    def use_potion(self,potion_power):
        self.current_pokemon.current_HP += potion_power * 10
        if self.current_pokemon.current_HP > self.current_pokemon.max_HP:
            self.current_pokemon.current_HP = self.current_pokemon.max_HP
            print("{} is now at full HP!".format(self.current_pokemon.name))
        else:
            print('{} just healed {} HP points'.format(self.current_pokemon.name, potion_power * 10))

    def switch_pokemon(self,replacement_pokemon):
        # print(self.pokemen)
        # print(replacement_pokemon)
        if replacement_pokemon in self.pokemen and replacement_pokemon.knocked_out == False:
            self.current_pokemon = replacement_pokemon
            print('{} switched to {}'.format(self.name, replacement_pokemon.name))
        else:
            print("{} doesn't have the pokemon or it is knocked out {}".format(self.name,replacement_pokemon.name))

charzard = Pokemon("Charzard",2,"Fire",150,150,False)
kyogre = Pokemon("Kyogre",2,"Water",150,150,False)
groudon = Pokemon("Groudon",2,"Ground",150,150,False)

colin = Trainer("Colin",[charzard,kyogre,groudon],3,charzard)
colin.use_potion(2)
colin.switch_pokemon(kyogre)

charzard.lose_health(20)
colin.use_potion(5)