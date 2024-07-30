from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import Protocol

ZERO = 0
MAX_STARTING_POSITION = 1000
MIN_STARTING_POSITION = 1
MAX_HEALTH = 1000
MAX_STAMINA = 100
MAX_POWER = 300
MAX_LEGS = 4
MAX_WINGS = 2
MAX_CLAWS = 4
MAX_TEETH = 3
MIN_TEETH = 1
MIN_CLAWS = 2
POWER_BOOST = 3


@dataclass
class Characteristics:
    is_prey: bool = False
    position: int = ZERO
    stamina: int = ZERO
    legs: int = ZERO
    wings: int = ZERO
    claws: int = ZERO
    teeth: int = ZERO
    power: int = ZERO
    health: int = ZERO

    def evolve(self) -> None:
        if self.is_prey:
            self.position = random.randint(MIN_STARTING_POSITION, MAX_STARTING_POSITION)
        self.stamina = random.randint(ZERO, MAX_STAMINA)
        self.legs = random.randint(ZERO, MAX_LEGS)
        self.wings = random.randint(ZERO, MAX_WINGS)
        self.claws = random.randint(MIN_CLAWS, MAX_CLAWS)
        self.teeth = random.randint(MIN_TEETH, MAX_TEETH)
        self.power = random.randint(ZERO, MAX_POWER)
        self.health = random.randint(ZERO, MAX_HEALTH)

    def log(self) -> None:
        if self.is_prey:
            creature = "Prey"
        else:
            creature = "Predator"
        print("\n" + creature + "'s characteristics:")
        print("position = " + str(self.position))
        print("stamina = " + str(self.stamina))
        print("legs = " + str(self.legs))
        print("wings = " + str(self.wings))
        print("claws = " + str(self.claws))
        print("teeth = " + str(self.teeth))
        print("power = " + str(self.power))
        print("health = " + str(self.health))

    def get_stamina(self) -> int:
        return self.stamina

    def get_position(self) -> int:
        return self.position

    def get_legs(self) -> int:
        return self.legs

    def get_wings(self) -> int:
        return self.wings

    def get_attacking_power(self) -> int:
        power = self.power * self.claws
        power += self.teeth * POWER_BOOST
        return self.power

    def is_dead(self) -> bool:
        if self.health <= ZERO:
            if self.is_prey:
                print("\nSome R-rated things have happened")
            else:
                print("\nPrey ran into infinity")
            return True
        return False

    def update_position(self, step: int) -> None:
        self.position += step

    def update_stamina(self, cost: int) -> None:
        self.stamina -= cost

    def update_health(self, cost: int) -> None:
        self.health -= cost


class Creature(Protocol):
    def evolve(self) -> None:
        pass

    def get_characteristics(self) -> Characteristics:
        pass


@dataclass
class CreatureDecorator:
    characteristics: Characteristics

    def evolve(self) -> None:
        self.characteristics.evolve()
        self.characteristics.log()

    def get_characteristics(self) -> Characteristics:
        return self.characteristics


@dataclass
class Prey(CreatureDecorator):
    characteristics: Characteristics = field(default_factory=Characteristics)

    def evolve(self) -> None:
        self.characteristics = Characteristics(True)
        super().evolve()


@dataclass
class Predator(CreatureDecorator):
    characteristics: Characteristics = field(default_factory=Characteristics)

    def evolve(self) -> None:
        self.characteristics = Characteristics(False)
        super().evolve()
