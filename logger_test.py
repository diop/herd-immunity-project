from logger import Logger
from person import Person
from virus import Virus
from simulation import Simulation
import pytest
import io
import sys
import os.path

# Test Logger Class

def test_create_file():
    file_name = 'logs.txt'
    logger = Logger(file_name)
    # Maybe delete file after creation
    # Then test that it was actually deleted.
    # assert not os.path.isfile(file_name)

    assert os.path.isfile(file_name)

def test_write_metadata():
    file_name = 'logs.txt'
    logger = Logger(file_name)
    logger.write_metadata(1000,50,'Melissa', 0.8, 1.1)

def test_log_interaction():
    file_name = 'log_interactions.txt'
    logger = Logger(file_name)
    person1 = Person(100, False, None)
    person2 = Person(50, True, None)
    logger.log_interaction(person1, person2, did_infect=None, person2_vacc=None, person2_sick=None)

def test_log_infection_survival():
    pass

def test_log_time_step():
    pass
