# tests/test_qubit.py
from my_quantum_lib.qubit import Qubit

def test_create_qubit():
    qubit = Qubit()
    assert qubit.state == [1, 0], "O qubit deve ser inicializado no estado |0⟩"

def test_apply_hadamard():
    qubit = Qubit()
    qubit.apply_hadamard()
    assert abs(qubit.state[0] - 1/2**0.5) < 1e-9, "O estado |0⟩ deve estar em superposição após Hadamard"
    assert abs(qubit.state[1] - 1/2**0.5) < 1e-9, "O estado |1⟩ deve estar em superposição após Hadamard"

if __name__ == "__main__":
    test_create_qubit()
    test_apply_hadamard()
    print("Todos os testes passaram!")