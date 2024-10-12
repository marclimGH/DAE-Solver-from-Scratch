import numpy as np
import matplotlib.pyplot as plt
from methods.ode_methods import backward_euler
from models.pendulum import pendulum_dynamics,pendulum_jacobian

#initial condition
theta0 = np.pi / 4
omega0 = 0.0

t0 = 0
y0 = np.array([theta0, omega0])
t_end = 10
dt = 0.001
t_values, y_values = backward_euler( pendulum_dynamics, pendulum_jacobian, t0, y0, t_end, dt )

plt.plot(t_values,y_values)
plt.show()