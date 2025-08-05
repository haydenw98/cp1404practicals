from random import randint
from prac_09.car import Car

class UnreliableCar(Car):
    """Unreliable version of Car class."""

    def __init__(self, name, fuel, reliability):
        """Initialise an unreliable car instance with a name, fuel and reliability (1-100)"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car based on reliability."""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven

