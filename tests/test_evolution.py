from evolution import Characteristics, Predator, Prey


def test_predator_evolve_get_position() -> None:
    predator = Predator()
    predator.evolve()
    characteristics = predator.get_characteristics()
    assert characteristics.get_position() == 0


def test_prey_evolve_get_position() -> None:
    prey = Prey()
    prey.evolve()
    characteristics = prey.get_characteristics()
    assert characteristics.get_position() > 0
    assert characteristics.get_position() <= 1000


def test_characteristics_update_position() -> None:
    characteristics = Characteristics(True)
    characteristics.evolve()
    before = characteristics.get_position()
    step = 10
    characteristics.update_position(step)
    assert characteristics.get_position() == before + step


def test_characteristics_update_stamina() -> None:
    characteristics = Characteristics(False)
    characteristics.evolve()
    before = characteristics.get_stamina()
    cost = 50
    characteristics.update_stamina(cost)
    assert characteristics.get_stamina() == before - cost


def test_characteristics_update_health() -> None:
    characteristics = Characteristics(False)
    characteristics.evolve()
    before = characteristics.health
    cost = 30
    characteristics.update_health(cost)
    assert characteristics.health == before - cost


def test_characteristics_is_dead() -> None:
    characteristics = Characteristics(False)
    characteristics.evolve()
    assert characteristics.is_dead() is False
