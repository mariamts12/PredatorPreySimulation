from evolution import Characteristics, Predator, Prey
from fight import attack


def test_attack() -> None:
    predator_characteristics = Characteristics(False, 15, 30, 0, 2, 1, 0, 150, 100)
    prey_characteristics = Characteristics(True, 13, 50, 0, 2, 2, 0, 100, 100)
    prey = Prey(prey_characteristics)
    predator = Predator(predator_characteristics)
    health_before = prey.get_characteristics().health
    power_of_predator = predator_characteristics.get_attacking_power()
    attack(predator, prey)
    assert prey.get_characteristics().health == health_before - power_of_predator
