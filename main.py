import numpy as np
import matplotlib.pyplot as plt
import time
from methods.ode_methods import backward_euler
from methods.dae_methods import backward_euler_dae

t0 = 0
t_end = 10
dt = 0.001

#DAE Analytical Jacobian vs Numerically computed Jacobian
from models.pendulum import pendulum_DAE_F, pendulum_DAE_JF
#initial condition 
theta0 = np.pi / 4
x0 = np.sin(theta0)
y0 = -np.cos(theta0)
vx0 = 0
vy0 = 0
lam0 = 0
y0 = np.array([x0,y0,vx0,vy0,lam0])

# ANALYTICAL JACOBIAN
start_time_AN = time.time()
t_values_AN, y_values_AN, residuals_AN = backward_euler_dae(pendulum_DAE_F, pendulum_DAE_JF, t0, y0, t_end, dt)
end_time_AN = time.time()
time_AN = end_time_AN - start_time_AN

# NUMERICAL JACOBIAN (finite differences)
start_time_NUM = time.time()
t_values_NUM, y_values_NUM, residuals_NUM = backward_euler_dae(pendulum_DAE_F, None, t0, y0, t_end, dt)
end_time_NUM = time.time()
time_NUM = end_time_NUM - start_time_NUM

# Print computation times
print(f"Computation Time with Analytical Jacobian: {time_AN:.4f} seconds")
print(f"Computation Time with Numerically computed Jacobian: {time_NUM:.4f} seconds")

# Extract x, y, vx, vy for both solutions
y_values_AN = np.array(y_values_AN)
y_values_NUM = np.array(y_values_NUM)

x_AN, y_AN, vx_AN, vy_AN, lam_AN = y_values_AN.T
x_NUM, y_NUM, vx_NUM, vy_NUM, lam_NUM = y_values_NUM.T

# Plot position comparison (x and y coordinates)
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.plot(t_values_AN, x_AN, label='Analytical Jacobian')
plt.plot(t_values_NUM, x_NUM, '--', label='Numerical Jacobian')
plt.title('Position X vs Time')
plt.xlabel('Time [s]')
plt.ylabel('X [m]')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(t_values_AN, y_AN, label='Analytical Jacobian')
plt.plot(t_values_NUM, y_NUM, '--', label='Numerical Jacobian')
plt.title('Position Y vs Time')
plt.xlabel('Time [s]')
plt.ylabel('Y [m]')
plt.legend()
plt.grid(True)

plt.show() 

# #with and without ALGEBRAIC LOOPs 
# from models.AlgebraicLoops import F_noAlgLoop,JF_noAlgLoop, F_withAlgLoop, JF_withAlgLoop
# # Initial Conditions
# y0_noAlg = np.array([0.0, 0.0])  # [x0, v0]
# y0_withAlgLoop = np.array([0.0, 0.0, 0.0, 0.0])  # [x0, v0, F_drag0, vSquared0]

# # (No Algebraic Loop)
# start_time_noAlg = time.time()
# t_values_noAlg, y_values_noAlg, residuals_noALg = backward_euler_dae(F_noAlgLoop, JF_noAlgLoop, t0, y0_noAlg, t_end, dt)
# end_time_noAlg = time.time()
# time_noAlg = end_time_noAlg - start_time_noAlg

# # # (With Strong Algebraic Loop)
# start_time_withAlgLoop = time.time()
# t_values_withAlgLoop, y_values_withAlgLoop, residuals_withAlgLoop = backward_euler_dae(F_withAlgLoop, JF_withAlgLoop, t0, y0_withAlgLoop, t_end, dt)
# end_time_withAlgLoop = time.time()
# time_withAlgLoop = end_time_withAlgLoop - start_time_withAlgLoop

# print(f"Computation Time without Algebraic Loop: {time_noAlg:.4f} seconds")
# print(f"Computation Time with Algebraic Loop: {time_withAlgLoop:.4f} seconds")


# # Extract positions and velocities
# x_noAlg, v_noAlg = zip(*y_values_noAlg)
# x_withAlgLoop, v_withAlgLoop, D_withAlgLoop, vSquared_withAlgLoop = zip(*y_values_withAlgLoop)

# # Plot Position
# plt.figure(figsize=(12, 6))
# plt.subplot(2, 1, 1)
# plt.plot(t_values_noAlg, x_noAlg, label='No Algebraic Loop')
# plt.plot(t_values_withAlgLoop, x_withAlgLoop, label='With Algebraic Loop', linestyle='--')
# plt.title('Position vs Time')
# plt.xlabel('Time (s)')
# plt.ylabel('Position (m)')
# plt.legend()
# plt.grid(True)

# # Plot Velocity
# plt.subplot(2, 1, 2)
# plt.plot(t_values_noAlg, v_noAlg, label='No Algebraic Loop')
# plt.plot(t_values_withAlgLoop, v_withAlgLoop, label='With Algebraic Loop', linestyle='--')
# plt.title('Velocity vs Time')
# plt.xlabel('Time (s)')
# plt.ylabel('Velocity (m/s)')
# plt.legend()
# plt.grid(True)

# plt.tight_layout()
# plt.show()

# #DAE
# from models.pendulum import pendulum_DAE_F, pendulum_DAE_JF
# #initial condition 
# theta0 = np.pi / 4
# x0 = np.sin(theta0)
# y0 = -np.cos(theta0)
# vx0 = 0
# vy0 = 0
# lam0 = 0
# y0 = np.array([x0,y0,vx0,vy0,lam0])

# t_values, y_values = backward_euler_dae( pendulum_DAE_F, pendulum_DAE_JF, t0, y0, t_end, dt )
# plt.plot(t_values,y_values)
# plt.show()

#ODE
# from models.pendulum import pendulum_dynamics,pendulum_jacobian
# #initial condition
# theta0 = np.pi / 4
# omega0 = 0.0
# y0 = np.array([theta0, omega0])

# t_values, y_values = backward_euler( pendulum_dynamics, pendulum_jacobian, t0, y0, t_end, dt )
# plt.plot(t_values,y_values)
# plt.show()




