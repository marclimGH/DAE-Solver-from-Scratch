import numpy as np
from solvers.nonlinear_solvers import newtonsmethod

def backward_euler_dae(F, JF, t0, y0, t_end, dt):
    t_values = np.arange(t0, t_end + dt, dt)
    y_values = [y0]
    for i in range(1, len(t_values)):
        y_old = y_values[i - 1]
        t_new = t_values[i]

        
        #DAE -> F(t,y,y') = 0 
        def G(y_new):
            y_dot = (y_new - y_old) / dt
            return F(t_new, y_new, y_dot )

        if JF is not None:
            #JF(y,y') = dF/dy + (dF/dy')*(dy'/dy)
            #also (dy'/dy) -> 1/dt   (from  backward differentiation yn+1' = (yn+1 - yn)/Dt )
            #JF(y,y') = dF/dy + (dF/dy')*(1/dt)
            def JG(y_new):
                y_dot = (y_new - y_old) / dt
                return JF(t_new, y_new, y_dot, dt) 
        else:
            JG = None
        

        y_new, residuals = newtonsmethod(G, JG, y_old)
        y_values.append(y_new)

    return t_values, y_values, residuals
