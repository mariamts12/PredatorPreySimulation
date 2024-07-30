from evolution import Creature


def attack(attacker: Creature, opponent: Creature) -> bool:
    power = attacker.get_characteristics().get_attacking_power()
    opponent.get_characteristics().update_health(power)
    return opponent.get_characteristics().is_dead()
