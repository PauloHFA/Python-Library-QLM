#biblioteca quantica python implementação.

from .gates import HadamardGate
import math
import random

class Quibit:
    """classe que representa um qubit."""

    def __init__(self):
        #estado inicial do quibit é |0⟩
        self.state = [1,0] # Representa o estado quântico |0⟩

    def measure(self):
        """mede o estado qubit, rernando 0 ou 1."""
        #Simula uma medição onde o estado colapsa para |0⟩ ou |1⟩.
        prob_zero = abs(self.state[0]) ** 2
        return 0 if random.random() < prob_zero else 1