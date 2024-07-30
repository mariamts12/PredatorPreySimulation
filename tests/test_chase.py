from chase import Crawling, Flying, Hopping, Running, Walking, check_positions
from evolution import Characteristics


def test_crawling() -> None:
    characteristics = Characteristics(False, 0, 10, 2)
    Crawling().move(characteristics)
    assert characteristics.get_position() == 1
    assert characteristics.get_stamina() == 9


def test_crawling_with_zero_stamina() -> None:
    characteristics = Characteristics()
    Crawling().move(characteristics)
    assert characteristics.get_position() == 0
    assert characteristics.get_stamina() == 0


def test_hopping() -> None:
    characteristics = Characteristics(True, 15, 30, 2)
    Hopping().move(characteristics)
    assert characteristics.get_position() == 18
    assert characteristics.get_stamina() == 28


def test_hopping_requirements_not_satisfied() -> None:
    characteristics = Characteristics(False, 0, 25, 0)
    Hopping().move(characteristics)
    assert characteristics.get_position() == 0
    assert characteristics.get_stamina() == 25


def test_walking() -> None:
    characteristics = Characteristics(False, 0, 50, 2)
    Walking().move(characteristics)
    assert characteristics.get_position() == 4
    assert characteristics.get_stamina() == 48


def test_walking_requirements_not_satisfied() -> None:
    characteristics = Characteristics(False, 0, 50, 1)
    Walking().move(characteristics)
    assert characteristics.get_position() == 0
    assert characteristics.get_stamina() == 50


def test_running() -> None:
    characteristics = Characteristics(False, 50, 70, 2)
    Running().move(characteristics)
    assert characteristics.get_position() == 56
    assert characteristics.get_stamina() == 66


def test_running_requirements_not_satisfied() -> None:
    characteristics = Characteristics(False, 50, 70, 1)
    Running().move(characteristics)
    assert characteristics.get_position() == 50
    assert characteristics.get_stamina() == 70


def test_hopping_because_running_requirements_not_satisfied() -> None:
    characteristics = Characteristics(False, 50, 70, 1)
    Running(Hopping()).move(characteristics)
    assert characteristics.get_position() == 53
    assert characteristics.get_stamina() == 68


def test_flying() -> None:
    characteristics = Characteristics(True, 100, 81, 1, 2)
    Flying().move(characteristics)
    assert characteristics.get_position() == 108
    assert characteristics.get_stamina() == 77


def test_flying_requirements_not_satisfied() -> None:
    characteristics = Characteristics(True, 100, 80, 1, 2)
    Flying().move(characteristics)
    assert characteristics.get_position() == 100
    assert characteristics.get_stamina() == 80


def test_running_walking_hopping_crawling() -> None:
    characteristics = Characteristics(True, 0, 80, 1, 2)
    Running(Walking(Hopping(Crawling()))).move(characteristics)
    assert characteristics.get_position() == 3
    assert characteristics.get_stamina() == 78


def test_all() -> None:
    characteristics = Characteristics(True, 0, 5, 2, 2)
    Flying(Running(Walking(Hopping(Crawling())))).move(characteristics)
    assert characteristics.get_position() == 1
    assert characteristics.get_stamina() == 4


def test_check_positions() -> None:
    predator_characteristics = Characteristics(False, 10, 20)
    prey_characteristics = Characteristics(True, 7, 20)
    assert check_positions(predator_characteristics, prey_characteristics) is False
