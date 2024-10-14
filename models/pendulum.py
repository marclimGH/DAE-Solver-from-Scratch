import numpy as np

g = 9.81

def pendulum_dynamics(t, y, L = 1.0):
   
    theta, omega = y
    dTheta_dt = omega
    dOmega_dt = -(g/L)*np.sin(theta)
    return np.array([dTheta_dt, dOmega_dt] )

def pendulum_jacobian(t, y, L = 1.0):
    
    theta, omega = y
    jacobian_matrix = np.array([ 
                                    [0.0,                       1.0],
                                    [-(g/L)*np.cos(theta),      0.0]    ])

    return jacobian_matrix


#as DAE system

def pendulum_DAE_F(t, y, y_dot, L = 1, m = 1):
    x_pos, y_pos, v_x, v_y, lam = y
    dx, dy, dv_x, dv_y, _ = y_dot

    F = np.zeros(5)
    F[0] = dx - v_x
    F[1] = dy - v_y
    F[2] = m * dv_x + lam * x_pos
    F[3] = m * dv_y + m * g + lam * y_pos
    F[4] = x_pos**2 + y_pos**2 - L**2
    return F

def pendulum_DAE_JF(t, y, y_dot, dt, L = 1, m = 1):
    x_pos, y_pos, v_x, v_y, lam = y

    # Partial derivatives
    dF_dy = np.array([
        [0,    0,   -1,    0,     0],
        [0,    0,    0,   -1,     0],
        [lam,  0,    0,    0,    x_pos],
        [0,   lam,   0,    0,   y_pos],
        [2*x_pos, 2*y_pos, 0,  0,     0]
    ])

    dF_dy_dot = np.array([
        [1,     0,    0,     0,   0],
        [0,     1,    0,     0,   0],
        [0,     0,    m,     0,   0],
        [0,     0,    0,     m,   0],
        [0,     0,    0,     0,   0]
    ]) 

    JF = dF_dy + dF_dy_dot* (1/dt)
    return JF
