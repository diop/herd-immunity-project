import random, sys
random.seed(42)
from person import Person
from virus import Virus
from logger import Logger

class Simulation(object):
    def __init__(self, population_size, vacc_percentage, virus_name,
                 mortality_rate, basic_repro_num, initial_infected=1):
        self.population_size = population_size
        self.population = []
        self.total_infected = 0
        self.current_infected = 0
        self.next_person_id = 0
        self.vacc_percentage = vacc_percentage
        self.virus_name = virus_name
        self.mortality_rate = mortality_rate
        self.basic_repro_num = basic_repro_num
        self.file_name = f'{virus_name}_simulation_pop_{population_size}_vp_{vacc_percentage}_infected_{initial_infected}.txt'

        self.logger = Logger(self.file_name)

        self.newly_infected = []

        self.population = self._create_population(initial_infected)


    def _create_population(self, initial_infected):
        '''
        -- Expects initial_infected as an Int.
        -- Should be called only once, at the end of the __init__ method.
        -- Stores all newly created Person objects in a local variable, population.
        -- Creates all infected person objects first.  Each time a new one is created,
            increments infected_count variable by 1.
        -- Once all infected person objects are created, begins creating healthy
            person objects.  To decide if a person is vaccinated or not, generates
            a random number between 0 and 1.  If that number is smaller than
            self.vacc_percentage, new person object will be created with is_vaccinated
            set to True.  Otherwise, is_vaccinated will be set to False.
        -- Once len(population) is the same as self.population_size, returns population.
        '''
        population = []
        infected_count = 0
        while len(self.population) != self.population_size:
            if infected_count !=  initial_infected:
                infected_person = Person(self.next_person_id, True, self.virus_name)
                self.population.append(infected_person)
                infected_count += 1
                self.next_person_id += 1
            else:
                random_created = random.random()
                if random_created < self.vacc_percentage:
                    vaccinated_person = Person(self.next_person_id, True, None)
                    self.population.append(vaccinated_person)
                    self.next_person_id += 1
                else:
                    non_vaccinated = Person(self.next_person_id, False, None)
                    self.population.append(non_vaccinated)
                    self.next_person_id += 1

        return population

    def _simulation_should_continue(self):
        death_count = 0
        infected_count = 0

        for person in self.population:
            if person.is_alive == False:
                death_count += 1

        for person in self.population:
            if person.infection:
                infected_count += 1

        if death_count == len(self.population):
            return False
        elif infected_count == 0:
            return false
        else:
            return True

    def run(self):
        time_step_counter = 0
        should_continue = self._simulation_should_continue()
        while should_continue:
            self.time_step()
            log_time_step(time_step_counter)
            time_step_counter += 1
            should_continue = self._simulation_should_continue()
        print(f'The simulation has ended after {time_step_counter} turns.')

    def time_step(self):
        for person.infected in population:
            for i in range(100):
                for person in population:
                    if person.is_alive == False:
                        return
                    else:
                        simulation.interaction(person, random_person)
                        interaction.counter += 1
            time_step_counter += 1

    def interaction(self, person, random_person):
        assert person1.is_alive == True
        assert random_person.is_alive == True

        if random_person.is_vaccinated or random_person.infected
            self.logger.log_interaction(person, random_person, False, True, False)
            return

        if random_person.is_vaccinated == False and random_person.is_vaccinated == False:
            random_num = random.random()
            if random_num < basic_repro_num:
                newly_infected.append(random_person._id)
                self.logger.log_interaction()


    def _infect_newly_infected(self):
        for person in self.newly_infected:
            for person.id in self.population:
                person.infected = True

        self.newly_infected = []


if __name__ == '__main__':
    params = sys.argv[1:]
    pop_size = int(params[0])
    vacc_percentage = float(params[1])
    virus_name = str(params[2])
    mortality_rate = float(params[3])
    basic_repro_num = float(params[4])
    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1
    simulation = Simulation(pop_size, vacc_percentage, virus_name, mortality_rate,
                            basic_repro_num, initial_infected)
    simulation.run()
