import matplotlib.pyplot as plt
from helpers import (random_neighbor, random_empty_position, sort_animals,
                     remove_dead)


class Animal:
    """ Represents an animal in the ecosystem
    """
    def __init__(self, species, row, column):
        """ Initializes a new animal
        Args:
           self (Animal): the object being created
           species (str): species name ("Lion" or "Zebra")
           row (int): row for the new animal in the grid
           column (int): column for the new animal in the grid
        """
        self.species = species
        self.row = row
        self.col = column
        self.age = 0
        self.starving_duration = 0
        self.is_alive = True

    def __str__(self):
        """ Creates a string from an object
        Args:
           self (Animal): the object on which the method is called
        Returns:
           str: String summarizing the object
        """
        string = ("<species:" + self.species + ", row:" + str(self.row) +
                  ", col:" + str(self.col) + ", age:" + str(self.age) +
                  ", starving_duration:" + str(self.starving_duration) +
                  ", is_alive:" + str(self.is_alive) + ">")
        return string

    def can_eat(self, other):
        """ Checks if self can eat other
        Args:
           self (Animal): the object on which the method is called
           other (Animal): another animal
        Returns:
           boolean: True if self can eat other, and False otherwise
        """
    
        Eat = False #Initializing bool eat
        if self.species == "Lion" and other.species == "Zebra": #if lion can eat zebra, eat is true
            Eat = True
        
        return Eat
    
    def time_passes(self):
        """ Increases age and starving_duration
        Args:
           self (Animal): the object on which the method is called
        Returns:
           Nothing
        """
        
        self.age +=1 #age plus one
        self.starving_duration +=1 #starving duration plus one
    
    def dies_of_old_age(self):
        """ If an animal dies of old age, sets is_alive to False
        Args:
           self (Animal): the object on which the method is called
        Returns: None
        """
        
        if self.species =="Lion" and 20>=self.age>=18: #If the species is Lion and make it to 18 months it is dead
            self.is_alive = False
        if self.species =="Zebra" and 20>=self.age>=7: #if the species ia Zebra and make it to 7 months it is dead
            self.is_alive = False

        
    def dies_of_hunger(self):
        """ If an animal dies of hunger, sets is_alive to False
        Args:
           self (Animal): the object on which the method is called
        Returns: None
        """
        
        if self.species =="Lion" and self.starving_duration>=6: #if the species is Lion and it has not eaten in 6 months, it dies of hunger
            self.is_alive = False
        
    def will_reproduce(self):
        """ Determines if an animal will reproduce at their current age
        Args:
           self (Animal): the object on which the method is called
        Returns:
           bool: True if ready to reproduce, False otherwise
        """
        
        reproduce = False #Initializing reproduce bool
        if self.species == "Lion": #If species is Lion
            if self.age >0 and self.age%7==0: #If the age is the multiple of 7, it can reproduce
                reproduce = True
        if self.species == "Zebra":#If species is Zebra
            if self.age>0 and self.age%3==0: #If the age is the multiple of 3, it can reproduce
                reproduce = True
        
        return reproduce

        
        
### end of Animal class ###


def initialize_population(grid_size):
    """ Initializes the grid by placing animals onto it.
    Args:
       grid_size (int): The size of the grid
    Returns:
       list of animals: The list of animals in the ecosystem
    """
    all_animals = []
    all_animals.append(Animal("Lion", 3, 5))
    all_animals.append(Animal("Lion", 7, 4))
    all_animals.append(Animal("Zebra", 2, 1))
    all_animals.append(Animal("Zebra", 5, 8))
    all_animals.append(Animal("Zebra", 9, 2))
    all_animals.append(Animal("Zebra", 4, 4))
    all_animals.append(Animal("Zebra", 4, 8))
    all_animals.append(Animal("Zebra", 1, 2))
    all_animals.append(Animal("Zebra", 9, 4))
    all_animals.append(Animal("Zebra", 1, 8))
    all_animals.append(Animal("Zebra", 5, 2))

    return all_animals


def move_animal(current_animal, grid_size, all_animals):
    """ Move an animal to a neighboring cell and either make it eat the
        neighboring animal or get eaten.
    Args:
        current_animal (Animal): The animal to be moved
        grid_size (int): The size of the grid
        all_animals (list of animals): The animals in the ecosystem
    Returns: None
    """
    
    neighbor_row, neighbor_col, neighbor_animal = random_neighbor(current_animal,grid_size, all_animals) #call random_neighbor function to obtain neighbor_row, neighbor_col and neighbor_animal

    if neighbor_animal == None: #If neighbor_animal is none, set row and col attributes of current_animal to neighbor_row and neighbor_col
        current_animal.row = neighbor_row
        current_animal.col = neighbor_col
    elif current_animal.can_eat(neighbor_animal) == True: #If current_animal can eat neighbor_animal, set row and col attributes of current_animal to neightbor_row and neighbor_col
        current_animal.row = neighbor_animal.row
        current_animal.col = neighbor_animal.col
        neighbor_animal.is_alive = False #set is_alive of neighbor_animal to False
        current_animal.starving_duration = 0 #reset starving_duration of current_animal to zero
    elif neighbor_animal.can_eat(current_animal) == True: #If neighbor_animal can eat current_animal.
        current_animal.is_alive = False #set is_alive of current_animal to False
        neighbor_animal.starving_duration = 0 #reset starving_duration of neighbor_animal to zero
    
    
def reproduce_animal(parent_animal, grid_size, all_animals):
    """ Creates a new animal at a neighboring cell if the parent animal
        is ready to reproduce.
        The new animal is added to the list of all animals
    Args:
        parent_animal (Animal): The parent animal which may reproduce
        grid_size (int): The size of the grid
        all_animals (list of animals): The animals in the ecosystem
    """
    
    if parent_animal.will_reproduce()==True: #if parent_animal ready to reproduce
        if random_empty_position(parent_animal,grid_size,all_animals) != None: #only if random_empty_position does not return none
            child_position = random_empty_position(parent_animal,grid_size,all_animals) #obtain random_empty_position
            row = child_position[0] #row is position at 0
            col = child_position[1] #col is position at 1
            child = Animal(parent_animal.species,row,col) #child is position at 2
            all_animals.append(child) #append this new anmimal to all_animal list
    
    
def one_step(all_animals, grid_size):
    """ Simulates the evolution of the ecosystem for one step (1 month)
    Args:
       all_animals (list of animals): The animals in the ecosystem
       grid_size (int): The size of the grid
    Returns: None
    """
    
    sort_animals (all_animals) #Call sort_animals function to sort the all_animals list
    for animal in all_animals: #for animal in all_animals list
        animal.time_passes() #call time_passes
        animal.dies_of_old_age() #call dies_of_old_age
    remove_dead(all_animals) #remove dead animals from all_animals list
    for animal in all_animals: #for animal in all_animals list
        animal.dies_of_hunger() #call dies_of_hunger
    remove_dead(all_animals) #remove dead animals from all_animals list

    for animal in all_animals: #for animal in all_animals list
        if animal.is_alive ==True: #if the animal is alive
            move_animal(animal,grid_size,all_animals) #call move_animal
    remove_dead(all_animals) #remove dead animals
    sort_animals(all_animals) #sort all_animals list

    for animal in all_animals: #for animal in all_animals list
        reproduce_animal(animal,grid_size,all_animals) #call reproduce_animal function


def run_whole_simulation(grid_size=10, duration=20):
    """ Simulates the evolution of the whole ecosystem.
        Generates graph of species abundance and saves it to populations.png
    Args:
       grid_size (int): Size of the grid
       duration (int): Number of steps of the simulation
    Returns:
       Nothing
    """
    all_animals = initialize_population(grid_size)
    
    #initializing list and count
    number_of_zebras_over_time =[]
    number_of_lions_over_time = []
    count_zebra = 0
    count_lions = 0

    for animal in all_animals: #for animal in all_animals list
        if animal.species =="Lion": #if the species is Lion then count_lions +1
            count_lions +=1
        if animal.species =="Zebra":#if the species is Zebra then count_zebra +1
            count_zebra +=1
    
    #append numbers to their respective list
    number_of_lions_over_time.append(count_lions)
    number_of_zebras_over_time.append(count_zebra)
    
    for t in range(0,duration,1): #for number of steps equal to duration argument 
        count_zebra=0
        count_lions=0
        one_step(all_animals,grid_size) #call one_step function
        for animal in all_animals: #count number of zebra and number of lions in the all_animals list
            if animal.species =="Lion":
                count_lions +=1
            if animal.species =="Zebra":
                count_zebra +=1
        #append those numbers to the respective list
        number_of_lions_over_time.append(count_lions)
        number_of_zebras_over_time.append(count_zebra)


    plt.title("Ecosystem simulator",fontsize = 20)
    plt.xlabel("Time in months",fontsize = 14)
    plt.ylabel("Number of animals", fontsize = 14)

    
    x_range = range(0,duration+1) #define x_range
    plt.plot(x_range,number_of_zebras_over_time,"-r",label="Zebras") #plot one for number_of_zebras_over_time in red and labeled Zebras
    plt.plot(x_range,number_of_lions_over_time,"-b",label="Lions") #plot one for number_of_lions_over_time in blue and labeled Lions
    plt.legend()
    plt.savefig("population.png")
    plt.show() #show plot
