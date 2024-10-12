import numpy as np
from solvers.nonlinear_solvers import newtonsmethod


def backward_euler(func, dfunc, t0, y0, t_end, dt):
    t_values = np.arange(t0,t_end,dt)
    y_values = [y0]
    for i in range(1,len(t_values)):
        y_old = y_values[i-1]
        t_new = t_values[i]

        def G(y):
            return y - y_old -dt* func(t_new,y)
        def JG(y):
            return np.eye(len(y)) - dt* dfunc(t_new,y)
        
        y_new = newtonsmethod(G, JG ,y_old)
        y_values.append(y_new)
    
    return t_values, y_values