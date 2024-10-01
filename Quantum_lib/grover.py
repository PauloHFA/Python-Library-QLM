import math
import numpy as np
from .gates import HadamardGate, PauliXGate, CNOTGate

class GroverAlgorithm:
    """Classe que implementa o algoritmo de Grover para busca em um espaço de estados."""
    
    def __init__(self, n):
        """
        Inicializa o algoritmo de Grover.
        
        :param n: Número de qubits
        """
        self.n = n
        self.target_state = None
        self.state = None
    
    def initialize(self):
        """Inicializa os qubits em estado |s⟩ (superposição igual)."""
        self.state = [1 / math.sqrt(2**self.n)] * (2**self.n)

        # Aplica a porta Hadamard em todos os qubits
        for i in range(self.n):
            self.state = HadamardGate.apply(HadamardGate.get_matrix(), self.state)
    
    def set_target(self, target):
        """
        Define o estado alvo para a busca.
        
        :param target: Estado alvo (inteiro representando o índice do estado)
        """
        if target < 0 or target >= 2**self.n:
            raise ValueError("O estado alvo deve estar dentro do espaço de estados.")
        self.target_state = target
    
    def oracle(self):
        """Implementa o oráculo que marca o estado alvo."""
        if self.target_state is None:
            raise ValueError("O estado alvo não foi definido.")
        
        # Inverte o sinal do estado alvo
        target_index = self.target_state
        self.state[target_index] = -self.state[target_index]

    def diffusion_operator(self):
        """Aplica a operação de difusão (ou reflexão)."""
        # Aplica a porta Hadamard
        for i in range(self.n):
            self.state = HadamardGate.apply(HadamardGate.get_matrix(), self.state)
        
        # Reflete em torno do estado médio
        mean = sum(self.state) / len(self.state)
        self.state = [2 * mean - amplitude for amplitude in self.state]
        
        # Aplica a porta Hadamard novamente
        for i in range(self.n):
            self.state = HadamardGate.apply(HadamardGate.get_matrix(), self.state)

    def grover_iteration(self):
        """Executa uma iteração do algoritmo de Grover."""
        self.oracle()              # Aplica o oráculo
        self.diffusion_operator()  # Aplica a operação de difusão

    def run(self, iterations):
        """
        Executa o algoritmo de Grover por um número específico de iterações.
        
        :param iterations: Número de iterações do algoritmo de Grover
        """
        self.initialize()  # Inicializa os qubits
        for _ in range(iterations):
            self.grover_iteration()  # Executa as iterações

    def measure(self):
        """Mede o estado final dos qubits."""
        probabilities = [abs(amplitude)**2 for amplitude in self.state]
        return np.random.choice(range(2**self.n), p=probabilities)

# Exemplo de uso:
# grover = GroverAlgorithm(n=2)
# grover.set_target(3)  # Defina o estado alvo
# grover.run(iterations=1)  # Execute o algoritmo
# result = grover.measure()  # Medir o estado
# print("Estado medido:", result)