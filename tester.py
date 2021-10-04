# This code calls the different functions and prints out their result.
# Use this to check if your solution produces the correct results.
# Comment out some code if you have not yet completed those functions/methods.

from ecosystem_simulator import (Animal, initialize_population, one_step,
                                 run_whole_simulation, move_animal,
                                 reproduce_animal)
from helpers import print_grid, remove_dead, sort_animals


def Q1():
    print("======== Question 1 =======")
    a = Animal("Lion", 0, 0)
    b = Animal("Zebra", 1, 1)
    print("Lion can eat Zebra?", a.can_eat(b))
    print("Zebra can eat Lion?", b.can_eat(a))
    print("Lion can eat Lion?", a.can_eat(a))


# def Q2():
#     print("======== Question 2 ========")
#     a = Animal("Lion", 0, 0)
#     b = Animal("Zebra", 1, 1)
#     a.time_passes()
#     print(a)
#     b.time_passes()
#     print(b)
#     b.time_passes()
#     print(b)


# def Q3():
#     print("======== Question 3  =========")
#     a = Animal("Lion", 0, 0)
#     for i in range(17):
#         a.time_passes()
#     a.dies_of_old_age()  # should be alive after 17 months
#     print(a.species, a.age, a.starving_duration, a.is_alive)

#     a.time_passes()
#     a.dies_of_old_age()  # should die now after 18 months
#     print(a.species, a.age, a.starving_duration, a.is_alive)

#     b = Animal("Zebra", 1, 1)
#     for i in range(6):
#         b.time_passes()
#     b.dies_of_old_age()  # should be alive after 6 months
#     print(b.species, b.age, b.starving_duration, b.is_alive)

#     b.time_passes()
#     b.dies_of_old_age()  # should die now after 7 months
#     print(b.species, b.age, b.starving_duration, b.is_alive)


# def Q4():
#     print("======== Question 4  =========")
#     a = Animal("Lion", 0, 0)
#     for i in range(5):
#         a.time_passes()
#     a.dies_of_hunger()  # should be alive after 5 months
#     print(a.species, a.age, a.starving_duration, a.is_alive)

#     a.time_passes()
#     a.dies_of_hunger()  # should die now after 6 months
#     print(a.species, a.age, a.starving_duration, a.is_alive)

#     b = Animal("Zebra", 1, 1)
#     for i in range(20):
#         b.time_passes()
#     b.dies_of_hunger()  # Zebras never die of hunger
#     print(b.species, b.age, b.starving_duration, b.is_alive)


# def Q5():
#     print("======== Question 5  =========")
#     a = Animal("Lion", 0, 0)
#     for i in range(6):
#         a.time_passes()
#     print(a.will_reproduce())  # not ready to reproduce

#     a.time_passes()
#     print(a.will_reproduce())  # ready to reproduce at 7 months

#     b = Animal("Zebra", 1, 1)
#     for i in range(2):
#         b.time_passes()
#     print(b.will_reproduce())  # not ready to reproduce

#     b.time_passes()
#     print(b.will_reproduce())  # ready to reproduce at 3 months


# def Q6():
#     print("======== Question 6  =========")
#     grid_size = 10
#     all_animals = initialize_population(grid_size)
#     print_grid(all_animals, grid_size)
    
#     a = all_animals[1]
#     print(a)
#     move_animal(a, grid_size, all_animals)
#     print("After moving: ")
#     print(a)
#     print_grid(all_animals, grid_size)
    
#     move_animal(a, grid_size, all_animals)
#     remove_dead(all_animals)
#     print("After moving again: ")
#     print(a)
#     print_grid(all_animals, grid_size)


# def Q7():
#     print("======== Question 7  =========")
#     grid_size = 10
#     all_animals = initialize_population(grid_size)
#     print_grid(all_animals, grid_size)
    
#     a = all_animals[3]
#     for i in range(3):
#         a.time_passes()
#     print(a)
#     reproduce_animal(a, grid_size, all_animals)
#     # should produce a new Zebra after 3 months
#     print_grid(all_animals, grid_size)
    
#     b = all_animals[0]
#     for i in range(7):
#         b.time_passes()
#     print(b)
#     reproduce_animal(b, grid_size, all_animals)
#     # should produce a new Lion after 7 months
#     print_grid(all_animals, grid_size)
    

# def Q8():
#     print("======== Question 8  =========")
#     grid_size = 10
#     all_animals = initialize_population(grid_size)
#     for time in range(20):
#         print("Time ", time)
#         print_grid(all_animals, grid_size)
#         one_step(all_animals, grid_size)


# def Q9():
#     print("======== Question 9  =========")
#     run_whole_simulation()
    
if __name__ == "__main__":
    Q1()
    Q2()
    Q3()
    Q4()
    Q5()
    Q6()
    Q7()
    Q8()
    Q9()
    
