import numpy as np
from numpy import linalg as LA
from r_values import AIR_Cp, AIR_p
import control


class Controller:
    def __init__(self, sim):
        self.sim = sim
        self.l = sim.hl
        self.v = sim.room['volume'] * AIR_p * AIR_Cp
        self.h = sim.room['heater']
        self.gen_abcd()
        self.check_eig()

    def gen_abcd(self):
        self.A = np.array([
            [self.l/self.v, -self.l/self.v],
            [0, 0],
        ])
        self.B = np.array([
            [self.h/self.v, 0],
            [0, 1]
        ])
        self.C = np.array([
            [1, 0],
            [0, 1]
        ])
        self.D = np.array([
            [0, 0],
            [0, 0]
        ])

    def check_eig(self):
        D, T = LA.eig(self.A)
        print("Eigenvalues of system: ")
        print(str(D))


"""
\\
x = \begin{bmatrix}
Room Temp\\ 
Outdoor Temp
\end{bmatrix} \\

u = \begin{bmatrix}
Heat Output\\ 
Outdoor Change
\end{bmatrix} \\

y = \begin{bmatrix}
Room Temp \\ 
Outdoor Temp
\end{bmatrix} \\

\dot x = Ax + Bu \\
y = Cx + Du \\

v = volume * density * Cp\\
l = Heat Loss \\
c = Heater Constant \\

A = \begin{bmatrix}
\frac{l}{v} & -\frac{l}{v} \\
0 & 0 \\
\end{bmatrix}
\\

B = \begin{bmatrix}
\frac{1}{v} & 0 \\
0 & 1
\end{bmatrix}
\\

C = \begin{bmatrix} 
1 & 0 \\
0 & 1 \\
\end{bmatrix}
\\

D = \begin{bmatrix} 
0 & 0 \\
0 & 0
\end{bmatrix}
"""