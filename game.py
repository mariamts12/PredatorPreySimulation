from typing import Tuple

from chase import Crawling, Flying, Hopping, Running, Walking, check_positions
from evolution import Predator, Prey
from fight import attack


def evolution_phase() -> Tuple[Predator, Prey]:
    predator = Predator()
    predator.evolve()
    prey = Prey()
    prey.evolve()
    return predator, prey


def chase_phase(predator: Predator, prey: Prey) -> bool:
    movement = Flying(Running(Walking(Hopping(Crawling()))))

    while check_positions(predator.get_characteristics(), prey.get_characteristics()):
        movement.move(predator.get_characteristics())
        movement.move(prey.get_characteristics())

    return predator.get_characteristics().get_stamina() == 0


def fight_phase(predator: Predator, prey: Prey) -> None:
    while True:
        if attack(predator, prey):
            return
        if attack(prey, predator):
            return


def game() -> None:
    for i in range(0, 100):
        predator, prey = evolution_phase()
        if chase_phase(predator, prey):
            continue
        fight_phase(predator, prey)


if __name__ == "__main__":
    game()
