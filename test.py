import numpy as np
import matplotlib
import paddle 
from paddle import matmul
from paddle_quantum.circuit import UAnsatz
from paddle_quantum.utils import random_pauli_str_generator, pauli_str_to_matrix, dagger
#参数设置
num_qubit = 3  
num_shots = 10**6 # Number of quantum measurements
tot_qubits = num_qubit+1 # Addition of an ancillary qubit
ancilla_idx = num_qubit #Index of the ancillary qubit (last position)
ITR = 80 #训练迭代次数
LR = 0.5 #学习速率
q_delta = 0.001 #Initial spread of random quantum weights
seed = 0 # Seed for random number generator
#构造cz gate
a= np.array([np.pi/2])
cz_theta = paddle.to_tensor(a)
#coefficient of A=c_0 A_0 + c_1 A_1 ...
c = np.array([1,0.2,0.2])

#定义门电路U和A
def U_b():
    for idx in range(num_qubit):
        cir.h(idx)
def CA(idx):
    if idx == 0:
        # Identity operation
        None
    elif idx == 1:
        cir.cnot([ancilla_idx,0])
        #cz gate
        cir.s(ancilla_idx)
        cir.s(ancilla_idx)
        cir.s(ancilla_idx)
        cir.cnot([ancilla_idx,1])
        cir.rz(cz_theta,1)
        cir.cnot([ancilla_idx,1])
        cir.rz(-cz_theta,1)
    elif idx == 2:
        cir.cnot(ancilla_idx, 0)
#定义变分量子电路 使得|x> = V|0>
def variational_block(theta):
    '''
    QNN
    '''
    #第一层是给除附加位外所有量子比特施加h门
    for idx in range(num_qubit):
        cir.h(idx)
    #单层的全y门
    for idx, element in enumerate(theta):
        cir.ry(element,idx)
    
 
