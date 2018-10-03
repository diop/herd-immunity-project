from virus import Virus

def test_virus_instantiation():
    virus = Virus('MELISSA', 0.8, 0.3)
    assert virus.name == 'MELISSA'
    assert virus.mortality_rate == 0.8
    assert virus.repro_rate == 0.3
