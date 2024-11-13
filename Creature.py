import Entity
from abc import abstractmethod


class Creature(Entity):
    def __init__(self, speed, hp):
        self.speed = speed
        self.hp = hp

    @abstractmethod
    def make_move(self):
        pass

