# my_quantum_lib/gates.py

import math

class QuantumGate:
    """Classe base para portas quânticas"""

    @staticmethod
    def apply(matrix, state):
        """Aplica uma porta quântica representada por uma matriz ao estado do qubit"""
        new_state = [
            matrix[0][0] * state[0] + matrix[0][1] * state[1],
            matrix[1][0] * state[0] + matrix[1][1] * state[1]
        ]
        return new_state

class HadamardGate(QuantumGate):
    """Classe que representa a porta Hadamard"""
    
    @staticmethod
    def get_matrix():
        """Retorna a matriz da porta Hadamard."""
        return [[1 / math.sqrt(2), 1 / math.sqrt(2)],
                [1 / math.sqrt(2), -1 / math.sqrt(2)]]

class PauliXGate(QuantumGate):
    """Classe que representa a porta Pauli-X (NOT quântico)"""
    
    @staticmethod
    def get_matrix():
        """Retorna a matriz da porta Pauli-X."""
        return [[0, 1],
                [1, 0]]

class PauliYGate(QuantumGate):
    """Classe que representa a porta Pauli-Y"""
    
    @staticmethod
    def get_matrix():
        """Retorna a matriz da porta Pauli-Y."""
        return [[0, -1j],
                [1j, 0]]

class PauliZGate(QuantumGate):
    """Classe que representa a porta Pauli-Z"""
    
    @staticmethod
    def get_matrix():
        """Retorna a matriz da porta Pauli-Z."""
        return [[1, 0],
                [0, -1]]

class CNOTGate:
    """Classe que representa a porta CNOT (Controlled-NOT)"""
    
    @staticmethod
    def apply(control, target):
        """Aplica a porta CNOT, invertendo o qubit target se o qubit control estiver no estado |1⟩."""
        if control == 1:
            target = 1 - target  # Inverte o qubit alvo
        return control, target

class TGate(QuantumGate):
    """Classe que representa a porta T (Phase rotation)"""
    
    @staticmethod
    def get_matrix():
        """Retorna a matriz da porta T."""
        return [[1, 0],
                [0, math.e ** (1j * math.pi / 4)]]

class SGate(QuantumGate):
    """Classe que representa a porta S"""
    
    @staticmethod
    def get_matrix():
        """Retorna a matriz da porta S."""
        return [[1, 0],
                [0, 1j]]

class RotationXGate(QuantumGate):
    """Classe que representa a porta de rotação em torno do eixo X"""
    
    @staticmethod
    def get_matrix(theta):
        """Retorna a matriz da porta Rx para o ângulo θ."""
        return [[math.cos(theta/2), -1j * math.sin(theta/2)],
                [-1j * math.sin(theta/2), math.cos(theta/2)]]

class RotationYGate(QuantumGate):
    """Classe que representa a porta de rotação em torno do eixo Y"""
    
    @staticmethod
    def get_matrix(theta):
        """Retorna a matriz da porta Ry para o ângulo θ."""
        return [[math.cos(theta/2), -math.sin(theta/2)],
                [math.sin(theta/2), math.cos(theta/2)]]

class RotationZGate(QuantumGate):
    """Classe que representa a porta de rotação em torno do eixo Z"""
    
    @staticmethod
    def get_matrix(theta):
        """Retorna a matriz da porta Rz para o ângulo θ."""
        return [[math.e ** (-1j * theta / 2), 0],
                [0, math.e ** (1j * theta / 2)]]

class SWAPGate:
    """Classe que representa a porta SWAP"""
    
    @staticmethod
    def apply(qubit1, qubit2):
        """Troca o estado de dois qubits"""
        return qubit2, qubit1