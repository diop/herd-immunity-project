import random
from virus import Virus

class Person(object):
    # _____Methods_____:
    def __init__(self, _id, is_vaccinated, infection=None):
        '''
        - self.alive should be automatically set to true during instantiation.
        - all other attributes for self should be set to their corresponding parameter
            passed during instantiation.
        - If person is chosen to be infected for first round of simulation, then
            the object should create a Virus object and set it as the value for
            self.infection.  Otherwise, self.infection should be set to None.
        '''
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.infection = infection

    def did_survive_infection(self):
        '''
        - Only called if infection attribute is not None.
        - Takes no inputs.
        - Generates a random number between 0 and 1.
        - Compares random number to mortality_rate attribute stored in person's infection
            attribute.
            - If random number is smaller, person has died from disease.
                is_alive is changed to false.
            - If random number is larger, person has survived disease.  Person's
            is_vaccinated attribute is changed to True, and set self.infected to None.
        '''
        mortality_rate = self.infection.mortality_rate
        if self.infection:
            random_float = random.random()
            if random_float > mortality_rate:
                self.is_vaccinated = True
                self.infected = None
                return True
            else:
                self.is_alive = False
                return False
