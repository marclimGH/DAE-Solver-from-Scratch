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