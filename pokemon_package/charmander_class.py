from pokemon_package.pokemon_abstract_class import Pokemon


class Charmander(Pokemon):
    # user id  for working  with data
    uid = 0
    # dictionary for evolution  and  family  of  3 pokemons
    evolution = {"Charmander": ["Charmander", "Charmeleon", "Charizard"]}

    def __init__(self, name, level, type, alive, owner=None):
        super().__init__(name, level, type, alive, owner)


    def __repr__(self):
        """ method  for representation  of pokemon"""
        return ("{} - Type {} - {} ({}/{}HPs) - Level {} ({}/100XP)".format(self.name, self.type, self.get_status(),
                                                                            self.health, self.max_health, self.level,
                                                                            self.experience))

    def is_active(self):
        """ method  for  checking whether pokemon active  or in Pokeball"""
        if self.active:
            return "Active"
        else:
            return "Pokeball"

    def get_status(self):
        """ method for checking whether pokemon alive or dead """
        if self.alive:
            return "Alive"
        else:
            return "Dead"

    def is_alive(self):
        """  method that  checks that  pokemon is  really  alive"""
        return self.alive == True

    def is_target_alive(self, target):
        """ method that checks that target-pokemon is  really alive"""
        return target.alive == True

    def knock_out(self):
        """  method that makes a  knock out for pokemon and  shows  it status"""
        if self.is_alive():
            self.alive = False
            self.health = 0
            print("> Oh no! {} is {}".format(self.name, self.get_status()))
        else:
            print("> {} is already dead.".format(self.name))

    def revive(self):
        """ method that reviving  of  pokemon, shows his HP and prints that he  is  alive"""
        print("--- Reviving {} ---".format(self.name))
        if self.alive == False:
            self.alive = True
            self.health = self.max_health // 2
            print("> Reviving {} with {}HPs.\n".format(self.name, self.health))
        else:
            print("> {} is already alive.\n".format(self.name))

    def lose_health(self, lost_hp):
        """ method  of loosing health and  HP comparing  to maximal HP"""
        if self.is_alive():
            self.health -= lost_hp
            if self.health > 0:
                print("> {} Losts {} HPs. Now has {}/{}HPs.\n".format(self.name, lost_hp, self.health, self.max_health))
            elif self.health <= 0:
                self.knock_out()
            else:
                print("> {} is already dead.".format(self.name))

    def restore_health(self, restore_hp):
        """method of healing pokemon and  restoring HP or printing  that he is  dead"""
        if self.is_alive():
            self.health += restore_hp
            if self.health >= self.max_health:
                self.health = self.max_health
            print("> {} heals {} HPs. ({}/{}HPs.)".format(self.name, restore_hp, self.health, self.max_health))
        else:
            print("> Can't heal, {} is dead.".format(self.name))

    def damage_boost(self, target):
        """method that makes the  boost of  pokemon on the basis of pokemon's type"""
        if self.type == "Fire" and target.type == "Water":
            boost = 0.5
            return boost
        elif self.type == "Water" and target.type == "Fire":
            boost = 0.5
            return boost
        elif self.type == "Fire" and target.type == "Grass":
            boost = 2
            return boost
        elif self.type == "Grass" and target.type == "Fire":
            boost = 0.5
            return boost
        elif self.type == "Grass" and target.type == "Water":
            boost = 2
            return boost
        else:
            boost = 1
            return boost

    # если при проверке переменная family с именем  покемона находится  в ключах словаря  evolution,
    # и если во вложенном  ветвлении уровень покемона является level >= 5 and level < 10, то  в переменную name покемона
    # присваиваем наш словарь evolution покемона под индексом 1 (family -  это семья из трех уровней эволюции покемонов),
    # если же  level >= 10 то в переменную name покемона присваиваем наш словарь evolution покемона под индексом 2,
    # в противном случае выходим из ветвления.
    def set_name(self):
        """method that  makes  the  evolution of  pokemon on the basis of family
        that consists of  3 pokemons in the dictionary. After reaching particular level
         pokemon evolves and  changes  name. There are 3  stages  of  evolution in the family list [0], [1], [3]"""
        if self.family in self.evolution.keys():
            if self.level >= 5 and self.level < 10:
                self.name = self.evolution[self.family][1]
            elif self.level >= 10:
                self.name = self.evolution[self.family][2]
        else:
            return

    def level_up(self):
        """ method that levels the pokemon up. after Evolution method sets a new  name of  pokemon"""
        if self.is_alive():
            self.level += 1
            self.max_health = self.level * self.health
            check_name = self.name
            self.set_name()
            if check_name != self.name:
                print("\n--- Hurray! {} has now evolve into a {}! ---".format(check_name, self.name))
            else:
                print("\n--- Level Up ! ---".format(self.name, self.level))
                print("> {} is now on level {}.".format(self.name, self.level))
                print("> {}".format(self))
        else:
            print("> Can't level up, {} is dead.".format(self.name))

    def add_xp(self, xp):
        """ method  that adds  XP to the experience and adds no XP if pokemon is  dead"""
        if self.is_alive:
            self.experience += xp
            if self.experience >= 100:
                self.level_up()
                rest = self.experience - 100
                self.experience = 0 + rest
            return xp
        else:
            print("> Can't xp, {} is dead.".format(self.name))

    def check_xp(self, target):
        "method that checks XP concerning changing of pokemon's level"
        if self.level - 4 >= target.level:
            xp = self.add_xp(40)
        elif self.level + 4 >= target.level:
            xp = self.add_xp(100)
        else:
            xp = self.add_xp(70)
        print("> {} earned {}XP.".format(self.name, xp))
        if xp:
            return xp
        else:
            return

    def attack(self, target):
        """method that attacks the pokemon-target,  shows damage, loosing of  health or that pokemon is dead"""
        if self.is_alive():
            if self.is_target_alive(target):
                damage = self.damage_boost(target) * self.level * 3
                print("> {} attacks {} and deals {} Damages (Boost x{})".format(self.name, target.name, damage,
                                                                                self.damage_boost(target)))
                target.lose_health(damage)
                if not self.is_target_alive(target):
                    self.check_xp(target)
            else:
                print("> Can't attack target, {} is dead.".format(target.name))
        else:
            print("> Can't attack, {} is dead.".format(self.name))
