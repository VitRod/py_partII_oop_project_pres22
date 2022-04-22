from abc import ABC, abstractmethod


class Pokemon(ABC):
    uid = 0

    def __init__(self, name, level, type, alive, owner=None):
        self.name = name
        self.level = level
        self.type = type
        self.alive = alive
        self.owner = owner
        self.family = self.name
        self.experience = 0
        self.health = 50
        self.max_health = self.health * self.level
        self.id = name + str(self.uid)
        self.active = False
        Pokemon.uid += 1

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def is_active(self):
        pass

    @abstractmethod
    def get_status(self):
        pass

    @abstractmethod
    def is_alive(self):
        pass

    @abstractmethod
    def is_target_alive(self, target):
        pass

    @abstractmethod
    def knock_out(self):
        pass

    @abstractmethod
    def revive(self):
        pass

    @abstractmethod
    def lose_health(self, lost_hp):
        pass

    @abstractmethod
    def restore_health(self, restore_hp):
        pass

    @abstractmethod
    def damage_boost(self, target):
        pass

    @abstractmethod
    def set_name(self):
        pass

    @abstractmethod
    def level_up(self):
        pass

    @abstractmethod
    def add_xp(self, xp):
        pass

    @abstractmethod
    def check_xp(self, target):
        pass

    @abstractmethod
    def attack(self, target):
        pass


