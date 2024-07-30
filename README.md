# PredatorPreySimulation

## Intro

This project is inspired by the 2008 life simulation RTS game [Spore](https://www.spore.com/). Spore allows you to evolve creatures with different characteristics such as claws, sharp teeth, wings, and many many more.

## Simulation

The aim is to model a simple simulation of the interaction between two creatures Predator and Pray. For now, let's imagine that the shape of the world we are modeling is an infinite ray illustrated below. It starts at position 0 and goes on and on as shown below.

```
012345678...
------------
```

The simulation is divided into three phases:

Evolution phase:

- Evolve a random creature at a 0 location (log characteristics)
  This creature will play the role of the predator in the simulation

- Evolve a random creature at a random location between 0 and 1000 (log characteristics)
  This creature will play the role of the pray in the simulation

Chase Phase:

- Predator chases pray, pray runs away until:
  * Predator runs out of `stamina`. (log message: "Pray ran into infinity")
  * Predator catches pray. In this case, they enter the fight

Fight Phase:

- In the fight, both creatures attack until:
  * Predator runs out of `health`. (log message: "Pray ran into infinity")
  * Pray runs out of `health`. (log message: "Some R-rated things have happened") :D

This process is repeated for 100 simulations, with results logged after each simulation.

Note: During the chase phase it is up to you to decide how smart or desperate you want your creatures to be.
I decide on a greedy approach (always choose the fastest movement available), but it is easy to change this
behavior in future development if there is a need.

## Functional requirements

- Ability to evolve `Legs`. Creature needs
  * At least one leg to `Hop`
  * At least two legs to `Walk` or `Run`

- Ability to evolve `Wings`. Creature needs
  * At least two wings to `Fly`

- Ability to evolve `Claws`
  * Small claws multiply creatures attacking `power` x2
  * Medium claws multiply creatures attacking `power` x3
  * Big claws multiply creatures attacking `power` x4

- Ability to evolve mouth with `Teeth`
  * Different degree of sharpness with +3, +6, +9 boost to attacking power

- Ability to `move` the creature in the world
  * Creatures with no limbs or wings can Crawl

- Ability to `attack` other creatures

Movement | requires stamina | uses stamina | speed |
---------|------------------|--------------|-------|
Crawling | 0+               | 1            | 1     |
Hopping  | 20+              | 2            | 3     |
Walking  | 40+              | 2            | 4     |
Running  | 60+              | 4            | 6     |
Flying   | 80+              | 4            | 8     |


## Development Setup

To maintain code quality, ensure the following tools are configured:

- **Formatting**: Use `black` auto formatter.
- **Import Sorting**: Use `isort`.
- **Type Checking**: Use `mypy`.
- **Linting**: Use `flake8`.
