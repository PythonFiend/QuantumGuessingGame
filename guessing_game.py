from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
from qiskit.providers.basicaer import QasmSimulatorPy
import matplotlib.pyplot as plt
import pandas as pd


player_guess = 0

def quantum_guessing_game():
    q = QuantumRegister(4,'quantumRegister')
    c = ClassicalRegister(4,'classicalRegister')
    qc = QuantumCircuit(q, c)

    qc.h(q)
    qc.measure(q, c)
    # qc.draw('mpl')
    # plt.show()

    sim = QasmSimulatorPy()
    transpiled_qc = transpile(qc, sim)
    result = sim.run(transpiled_qc).result()
    counts = result.get_counts(qc)
    quantum_guess = list(counts.keys())[0]
    bytes_to_dec = int(quantum_guess, 2)

    return bytes_to_dec
qc_guess = quantum_guessing_game()


def result():
    df = pd.DataFrame({'Quantum Secret':qc_guess,
                       "Player's guess":player_guess},index=[0])
    res = df.reset_index(drop=True)
    return res


if __name__ == '__main__':

    try:
        player_guess = int(input('Enter a number from 0 to 15: '))
    except ValueError:
        print('Incorrect value.')
    else:
        if qc_guess == player_guess:
            print(f"Correct!\n{result()}")
        else:
            print(f'Sorry, that is not correct.\n{result()}')



