from dataclasses import dataclass, field
from typing import Protocol

from evolution import Characteristics

ZERO = 0
CRAWLING_REQUIRED_STAMINA = 0
CRAWLING_USED_STAMINA = 1
CRAWLING_SPEED = 1
HOPPING_REQUIRED_STAMINA = 20
HOPPING_USED_STAMINA = 2
HOPPING_SPEED = 3
WALKING_REQUIRED_STAMINA = 40
WALKING_USED_STAMINA = 2
WALKING_SPEED = 4
RUNNING_REQUIRED_STAMINA = 60
RUNNING_USED_STAMINA = 4
RUNNING_SPEED = 6
FLYING_REQUIRED_STAMINA = 80
FLYING_USED_STAMINA = 4
FLYING_SPEED = 8
REQUIRED_LEGS_HOPPING = 1
REQUIRED_LEGS_WALKING = 2
REQUIRED_LEGS_RUNNING = 2
REQUIRED_WINGS_FLYING = 2


class Movement(Protocol):
    def move(self, characteristics: Characteristics) -> None:
        pass


@dataclass
class NoMovement:
    def move(self, characteristics: Characteristics) -> None:
        pass


@dataclass
class MovementDecorator:
    following: Movement = field(default_factory=NoMovement)
    required_stamina: int = ZERO
    used_stamina: int = ZERO
    speed: int = ZERO
    requirement: int = ZERO
    actual: int = ZERO

    def move(self, ch: Characteristics) -> None:
        if self.actual >= self.requirement and ch.get_stamina() > self.required_stamina:
            ch.update_stamina(self.used_stamina)
            ch.update_position(self.speed)
            return
        self.following.move(ch)


@dataclass
class Crawling(MovementDecorator):
    required_stamina: int = CRAWLING_REQUIRED_STAMINA
    used_stamina: int = CRAWLING_USED_STAMINA
    speed: int = CRAWLING_SPEED

    def move(self, characteristics: Characteristics) -> None:
        super().move(characteristics)


@dataclass
class Hopping(MovementDecorator):
    required_stamina: int = HOPPING_REQUIRED_STAMINA
    used_stamina: int = HOPPING_USED_STAMINA
    speed: int = HOPPING_SPEED
    requirement: int = REQUIRED_LEGS_HOPPING

    def move(self, characteristics: Characteristics) -> None:
        self.actual = characteristics.get_legs()
        super().move(characteristics)


@dataclass
class Walking(MovementDecorator):
    required_stamina: int = WALKING_REQUIRED_STAMINA
    used_stamina: int = WALKING_USED_STAMINA
    speed: int = WALKING_SPEED
    requirement: int = REQUIRED_LEGS_WALKING

    def move(self, characteristics: Characteristics) -> None:
        self.actual = characteristics.get_legs()
        super().move(characteristics)


@dataclass
class Running(MovementDecorator):
    required_stamina: int = RUNNING_REQUIRED_STAMINA
    used_stamina: int = RUNNING_USED_STAMINA
    speed: int = RUNNING_SPEED
    requirement: int = REQUIRED_LEGS_RUNNING

    def move(self, characteristics: Characteristics) -> None:
        self.actual = characteristics.get_legs()
        super().move(characteristics)


@dataclass
class Flying(MovementDecorator):
    required_stamina: int = FLYING_REQUIRED_STAMINA
    used_stamina: int = FLYING_USED_STAMINA
    speed: int = FLYING_SPEED
    requirement: int = REQUIRED_WINGS_FLYING

    def move(self, characteristics: Characteristics) -> None:
        self.actual = characteristics.get_wings()
        super().move(characteristics)


def check_positions(predator: Characteristics, prey: Characteristics) -> bool:
    if predator.get_position() >= prey.get_position():
        return False
    if predator.get_stamina() == ZERO:
        print("\nPrey ran into infinity")
        return False
    return True
