# tests/test_qubit.py
from Quantum_lib.qubit import Qubit
import random

def test_create_qubit():
    qubit = Qubit()
    assert qubit.state == [1, 0], "O qubit deve ser inicializado no estado |0⟩"

def test_apply_hadamard():
    qubit = Qubit()
    qubit.apply_hadamard()
    assert abs(qubit.state[0] - 1/2**0.5) < 1e-9, "O estado |0⟩ deve estar em superposição após Hadamard"
    assert abs(qubit.state[1] - 1/2**0.5) < 1e-9, "O estado |1⟩ deve estar em superposição após Hadamard"

def test_measure():
    qubit = Qubit()
    measurements = [qubit.measure() for _ in range(1000)]
    # Deve medir 0 com probabilidade de 1 (já que o estado inicial é |0⟩)
    assert measurements.count(0) > 900, "A medição deve retornar 0 com alta probabilidade."

    # Aplique Hadamard e teste a medição novamente
    qubit.apply_hadamard()
    measurements = [qubit.measure() for _ in range(1000)]
    # Após Hadamard, deve medir 0 e 1 com aproximadamente a mesma probabilidade
    assert abs(measurements.count(0) - measurements.count(1)) < 200, "As medições devem ser aproximadamente equilibradas após Hadamard."

def test_reset():
    qubit = Qubit()
    qubit.apply_hadamard()
    assert any(abs(state - 1/2**0.5) < 1e-9 for state in qubit.state), "O qubit deve estar em superposição após Hadamard."
    
    # Supondo que você tenha um método reset()
    qubit.reset()
    assert qubit.state == [1, 0], "O qubit deve ser resetado para o estado |0⟩."

if __name__ == "__main__":
    test_create_qubit()
    test_apply_hadamard()
    test_measure()
    test_reset()
    print("Todos os testes passaram!")
