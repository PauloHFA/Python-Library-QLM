# Python-Library-QLM
A Python library for simulating quantum computing operations, implementing various quantum gates and qubits for learning and experimentation. This library is designed to provide an intuitive interface for creating and manipulating quantum states, enabling users to explore quantum algorithms and operations.

Documentação dos Gates Quânticos

QuantumGate
Classe base para portas quânticas.

Métodos Estáticos
apply(matrix, state)
Aplica uma porta quântica representada por uma matriz ao estado do qubit.

Parâmetros:
matrix: matriz que representa a porta quântica.
state: estado do qubit a ser transformado.

Retorno:
O novo estado do qubit após a aplicação da porta.

HadamardGate
Classe que representa a porta Hadamard.

Métodos Estáticos
get_matrix()
Retorna a matriz da porta Hadamard.
Retorno:
[[1 / √2, 1 / √2], [1 / √2, -1 / √2]]

PauliXGate
Classe que representa a porta Pauli-X (NOT quântico).

Métodos Estáticos
get_matrix()
Retorna a matriz da porta Pauli-X.
Retorno:
[[0, 1], [1, 0]]

PauliYGate
Classe que representa a porta Pauli-Y.

Métodos Estáticos
get_matrix()
Retorna a matriz da porta Pauli-Y.
Retorno:
[[0, -1j], [1j, 0]]

PauliZGate
Classe que representa a porta Pauli-Z.

Métodos Estáticos
get_matrix()
Retorna a matriz da porta Pauli-Z.
Retorno:
[[1, 0], [0, -1]]

CNOTGate
Classe que representa a porta CNOT (Controlled-NOT).

Métodos Estáticos
apply(control, target)
Aplica a porta CNOT, invertendo o qubit alvo se o qubit de controle estiver no estado |1⟩.
Parâmetros:
control: estado do qubit de controle (0 ou 1).
target: estado do qubit alvo (0 ou 1).
Retorno:
O novo estado dos qubits de controle e alvo.

TGate
Classe que representa a porta T (Phase rotation).

Métodos Estáticos
get_matrix()
Retorna a matriz da porta T.
Retorno:
[[1, 0], [0, e^(iπ/4)]]

SGate
Classe que representa a porta S.

Métodos Estáticos
get_matrix()
Retorna a matriz da porta S.
Retorno:
[[1, 0], [0, 1j]]

RotationXGate
Classe que representa a porta de rotação em torno do eixo X.
Métodos Estáticos
get_matrix(theta)
Retorna a matriz da porta Rx para o ângulo θ.
Parâmetros:
theta: ângulo de rotação em radianos.

RotationYGate
Classe que representa a porta de rotação em torno do eixo Y.

Métodos Estáticos
get_matrix(theta)
Retorna a matriz da porta Ry para o ângulo θ.
Parâmetros:
theta: ângulo de rotação em radianos.

RotationZGate
Classe que representa a porta de rotação em torno do eixo Z.
Métodos Estáticos
get_matrix(theta)
Retorna a matriz da porta Rz para o ângulo θ.
Parâmetros:
theta: ângulo de rotação em radianos.

SWAPGate
Classe que representa a porta SWAP.

Métodos Estáticos
apply(qubit1, qubit2)
Troca o estado de dois qubits.
Parâmetros:
qubit1: estado do primeiro qubit.
qubit2: estado do segundo qubit.
Retorno:
Os novos estados dos qubits trocados.

Como Usar
Para usar estas portas quânticas, você pode importar as classes necessárias e aplicar as portas ao estado de um 

qubit como no exemplo abaixo:

python
from gates import HadamardGate

# Estado inicial do qubit
state = [1, 0]  # |0⟩

# Aplica a porta Hadamard
new_state = HadamardGate.apply(HadamardGate.get_matrix(), state)
print(new_state)  # Mostra o novo estado do qubit
