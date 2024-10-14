import numpy as np
import matplotlib.pyplot as plt
from methods.ode_methods import backward_euler
from models.pendulum import pendulum_dynamics,pendulum_jacobian

from methods.dae_methods import backward_euler_dae
from models.pendulum import pendulum_DAE_F, pendulum_DAE_JF

t0 = 0
t_end = 10
dt = 0.001

#initial condition DAE
theta0 = np.pi / 4
x0 = np.sin(theta0)
y0 = -np.cos(theta0)
vx0 = 0
vy0 = 0
lam0 = 0
y0 = np.array([x0,y0,vx0,vy0,lam0])

t_values, y_values = backward_euler_dae( pendulum_DAE_F, pendulum_DAE_JF, t0, y0, t_end, dt )
plt.plot(t_values,y_values)
plt.show()

# #initial condition
# theta0 = np.pi / 4
# omega0 = 0.0
# y0 = np.array([theta0, omega0])

# t_values, y_values = backward_euler( pendulum_dynamics, pendulum_jacobian, t0, y0, t_end, dt )
# plt.plot(t_values,y_values)
# plt.show()

