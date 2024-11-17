from abc import ABC


# class Entity(ABC):
    # Coordinates coorninate
    # def __init__(self, simulation_map):
    #     self.map = simulation_map
    #     self.counter = 0

class Entity(ABC):
    def __init__(self, position: tuple[int, int]) -> None:
        self.position: tuple[int, int] = position
