# same system modeled with and without algrebraic loops

import numpy as np

# System Parameters
m = 1500.0           # Mass 
c = 50                 # drag coeff
F_traction = 4000

# NO ALGEBRAIC LOOP
def F_noAlgLoop(t, y, y_dot):
    x, v = y
    dx, dv = y_dot
    

    res1 = dx -v
    res2 = m*dv - F_traction + c*v**2
    return np.array([res1, res2])

def JF_noAlgLoop(t, y, y_dot, dt):
    x, v = y
    dx, dv = y_dot
    dF_dy = np.array([
        [0, -1],
        [0,  2 * c * v]
    ])
    dF_dy_dot = np.array([
        [1, 0],
        [0, m ]
    ])

    JF = dF_dy + dF_dy_dot*(1.0/dt)
    return JF


# WITH ALGEBRAIC LOOP
def F_withAlgLoop(t, y, y_dot):
    x, v, F_drag, vSquared= y
    dx, dv, dF_drag, dvSquared= y_dot
    

    res1 = dx -v
    res2 = m*dv - F_traction + F_drag
    res3 = F_drag - c*vSquared  # Algebraic constraint
    res4 = vSquared -v**2       # Algebraic constraint
    return np.array([res1, res2, res3, res4])

def JF_withAlgLoop(t, y, y_dot, dt):
    x, v, F_drag, vSquared= y
    dx, dv, dF_drag, dvSquared= y_dot

    dF_dy = np.array([
        [0,     -1,     0,      0],
        [0,     0,      1,      0],
        [0,     0,      1,      -c],
        [0,     -2*v,   0,      1]
    ])
    dF_dy_dot = np.array([
        [1, 0, 0,   0],
        [0, m, 0,   0],
        [0, 0, 0,   0],
        [0, 0, 0,   0]
    ])

    JF = dF_dy + dF_dy_dot*(1.0/dt)
    return JF