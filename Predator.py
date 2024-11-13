import Creature


class Predator(Creature):
    def __init__(self, power):
        super().__init__()
        self.power = power
