from person import Person
from simulation import Simulation
from logger import Logger
import pytest
import io
import sys


# Test Simulation Class
def test_simulation_instance():
    simulation = Simulation(1000, 0.1, 'nile_virus', 0.3, 2.1, 10)
    assert simulation.population_size == 1000
    assert simulation.virus_name == 'nile_virus'

def test_create_population():
    pass

def test_simulation_should_continue():
    pass

def test_run():
    pass

def test_time_step():
    pass

def test_interactions():
    pass

def test_infect_newly_infected():
    pass
