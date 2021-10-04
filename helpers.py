# Do not change anything in this file
# This file contains helper functions used in ecosystem_simulator

import random

random.seed(10)


def list_neighbors(current_row, current_col, grid_size):
    """ Produces the list of neighboring positions
    Args:
       current_row (int): Current row of the animal
       current_col (int): Current column of the animal
       grid_size (int): The size of the gride
    Returns:
       list of tuples of two ints: List of all (row, col) tuples that are 
                                   around the current position, without 
                                   including positions outside the grid
    """
    neighbors = []
    for row_offset, col_offset in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),
                                   (1, -1), (1, 0), (1, 1)]:
        new_row = current_row + row_offset
        new_col = current_col + col_offset
        if (new_row >= 0 and new_row < grid_size and new_col >= 0
                and new_col < grid_size):
            neighbors.append((new_row, new_col))
    return neighbors


def my_random_choice(choices):
    """ Picks ones of the elements of choices
    Args:
       choices (list): the choices to choose from
    Returns:
       One of elements in the list
    """
    def getKey(x):
        return x[0] + 0.001 * x[1]

    return min(choices, key=getKey)

    # for actual random selection, we may replace the above with this:
    #return random.choice(choices)


def random_neighbor(current_animal, grid_size, all_animals):
    """ Chooses a random neighboring position from current animal position
    Args:
       current_animal (Animal): The animal whose neighbor to choose
       grid_size (int): Size of the grid
       all_animals (list of Animal): list of all animals in the grid
    Returns:
       a tuple (row, col, animal): where row, col indicate the randomly
            chosen neighboring position in the grid;
            and animal is None if the cell (row, col) in grid is empty,
                otherwise animal is an Animal object.

    """
    all_neighbors = list_neighbors(current_animal.row, current_animal.col,
                                   grid_size)
    row, col = my_random_choice(all_neighbors)
    animal = None
    for x in all_animals:
        if x.is_alive and x.row == row and x.col == col:
            animal = x
    return (row, col, animal)


def random_empty_position(current_animal, grid_size, all_animals):
    """ Chooses a random empty neighboring position from current position
    Args:
       current_animal (Animal): The animal whose neighbor to choose
       grid_size (int): Size of the grid
       all_animals (list of Animal): list of all animals in the grid
    Returns:
       a tuple (row, col) or None: where row, col indicate the randomly
            chosen empty position in the grid. If no empty neighbors are found,
            returns None.
    """
    all_neighbors = list_neighbors(current_animal.row, current_animal.col,
                                   grid_size)

    occupied = set()
    for x in all_animals:
        occupied.add((x.row, x.col))

    neighbors = []
    for x in all_neighbors:
        if x not in occupied:
            neighbors.append(x)

    if len(neighbors) == 0:
        return None

    row, col = my_random_choice(neighbors)
    return (row, col)


def print_grid(all_animals, grid_size):
    """ Prints the grid
    Args:
       all_animals (list of Animal): The animals in the ecosystem
       grid_size (int): The size of the grid
    Returns: None
    """

    # get the set of tuples where lions and zebras are located
    lions_tuples = set()
    zebras_tuples = set()
    for a in all_animals:
        if a.species == "Lion":
            lions_tuples.add((a.row, a.col))
        elif a.species == "Zebra":
            zebras_tuples.add((a.row, a.col))

    print("*" * (grid_size + 2))
    for row in range(grid_size):
        print("*", end="")
        for col in range(grid_size):
            if (row, col) in lions_tuples:
                print("L", end="")
            elif (row, col) in zebras_tuples:
                print("Z", end="")
            else:
                print(" ", end="")
        print("*")
    print("*" * (grid_size + 2))


def sort_animals(all_animals):
    """ Sorts the animals according their position in grid,
        left to right and top to bottom 
    Args:
       all_animals (list of animals): The animals in the ecosystem
    Returns: None
    """
    def get_key(a):
        return a.row + 0.001 * a.col

    all_animals.sort(key=get_key)


def remove_dead(all_animals):
    """ Removes all the dead animals from the list of animals in the ecosystem.
    Args:
       all_animals (list of animals): The animals in the ecosystem
    Returns: None
    """
    dead = []
    for x in all_animals:
        if not x.is_alive:
            dead.append(x)

    for x in dead:
        all_animals.remove(x)
