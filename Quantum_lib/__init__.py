# __init__.py

"""
my_quantum_lib: Biblioteca para programação quântica.

Este pacote contém implementações de portas quânticas, qubits e algoritmos quânticos, como o algoritmo de Grover e o algoritmo de Shor.
"""

# Importando as classes de portas quânticas
from .gates import (
    HadamardGate,
    PauliXGate,
    PauliYGate,
    PauliZGate,
    CNOTGate,
    TGate,
    SGate,
    RotationXGate,
    RotationYGate,
    RotationZGate,
    SWAPGate,
)

from .qubit import Quibit
# Se você tiver os algoritmos Grover e Shor, também importe-os
# from .grover import GroverAlgorithm
# from .shor import ShorAlgorithm

__all__ = [
    "HadamardGate",
    "PauliXGate",
    "PauliYGate",
    "PauliZGate",
    "CNOTGate",
    "TGate",
    "SGate",
    "RotationXGate",
    "RotationYGate",
    "RotationZGate",
    "SWAPGate",
    "Quibit",
    # "GroverAlgorithm",  # Descomente se adicionar o Grover
    # "ShorAlgorithm",    # Descomente se adicionar o Shor
]
