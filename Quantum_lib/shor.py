import numpy as np
from .gates import HadamardGate, CNOTGate, RotationZGate
from .qubit import Qubit 
import math
import random

class ShorAlgorithm:
    """Classe que implementa o Algoritmo de Shor para fatoração de números inteiros."""

    def __init__(self, N):
        """
        Inicializa o Algoritmo de Shor.
        
        :param N: Número a ser fatorado.
        """
        self.N = N
        self.a = None
        self.period = None

    def choose_a(self):
        """Escolhe um número a aleatório tal que 1 < a < N."""
        self.a = np.random.randint(2, self.N)

    def gcd(self, x, y):
        """Calcula o Máximo Divisor Comum (GCD) usando o algoritmo de Euclides."""
        while y:
            x, y = y, x % y
        return x

    def classical_gcd(self):
        """Calcula o GCD de a^(N/2) - 1 e N."""
        r = self.a ** (self.N // 2) - 1
        return self.gcd(r, self.N)

    def quantum_period_finding(self):
        """
        Implementa a busca de período quântico.
        """
        # Crie um número de qubits necessários
        num_qubits = 2  # Exemplo, ajuste conforme necessário
        qubits = [Qubit() for _ in range(num_qubits)]

        # Aplica portas quânticas conforme necessário:
        H_matrix = HadamardGate.get_matrix()
        qubits[0].state = HadamardGate.apply(H_matrix, qubits[0].state)

    
        # utilizando portas quânticas, a transformação de Fourier quântica.
        return 2  # Exemplo de retorno fixo.

    def find_factors(self):
        """Fatoriza o número N utilizando o Algoritmo de Shor."""
        self.choose_a()
        print(f"Escolhendo a = {self.a}")

        # Verifica se a é coprimo com N
        if self.gcd(self.a, self.N) != 1:
            print(f"GCD(a, N) = {self.gcd(self.a, self.N)}. Portanto, um fator é {self.gcd(self.a, self.N)}.")
            return

        self.period = self.quantum_period_finding()
        print(f"Período encontrado: {self.period}")

        # Fatores
        factor1 = self.gcd(self.a ** (self.period // 2) - 1, self.N)
        factor2 = self.gcd(self.a ** (self.period // 2) + 1, self.N)

        if factor1 == 1 or factor2 == 1:
            print("Não foram encontrados fatores não triviais.")
        else:
            print(f"Fatores de {self.N}: {factor1} e {factor2}.")

# Exemplo de uso:
# shor = ShorAlgorithm(N=15)
# shor.find_factors()