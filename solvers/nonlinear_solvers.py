# solve for a root of non-linear function
# we want to find x such that f(x) = 0 
# iteration xnext = xpre - (f(xpre)/f'(xpre));
import numpy as np

def newtonsmethod(G, JG, x_guess,  tol=1e-6, max_iter = 100):
    x_old = np.array(x_guess, dtype=float)
    G_x = G(x_old)
    JG_x = JG(x_old)
    isScalar = np.isscalar(G_x) and np.isscalar(JG_x)

    if isScalar:
        for i in range(1,max_iter):
            G_x = G(x_old)
            JG_x = JG(x_old)
            
            if JG_x == 0:
                print("Division by zero")
            else:
                Dx = G_x/JG_x
                
            x_new = x_old - Dx
            print(f"Iteration {i}: x_new = {x_new}")

            if np.abs(Dx) < tol:
                print(f"Converged in {i+1} iterations.")
                return x_new
            
            x_old = x_new 
    else:
        for i in range(1,max_iter):
            G_x = G(x_old)
            JG_x = JG(x_old)
            
            #check if jacobian is singular G = JG*Δx  ( y = y'*dx )
            # print("G_x")
            # print(G_x)
            # print("JG_x")
            # print(JG_x)
            
            try:
                Dx = np.linalg.solve(JG_x, G_x)
                # Dx = np.array([1,1])
            except np.linalg.LinAlgError:
                print("Jacobian is singular or ill conditioned")

            
            x_new = x_old - Dx
            print(f"Iteration {i}: x_new = {x_new}")

            if np.linalg.norm(Dx,ord=np.inf) < tol:
                print(f"Converged in {i+1} iterations.")
                return x_new
            
            x_old = x_new 
    

    print("Exceeded maximum iterations. No solution found.")
    return None




# def newton_raphson():
#     y_new = 0

#     return y_new



 

# fun = lambda x: x**2 - 2
# funDer = lambda x: 2*x
# x0 =0.1

fun = lambda x: np.array([
    x[0]**2 + x[1]**2 - 4,
    x[0] - x[1]
])

funDer = lambda x: np.array([
    [2*x[0], 2*x[1]],
    [1, -1]
])
x0 = np.array([0.1, 0.1])



res = newtonsmethod(fun,funDer, x0)
print(f"res is {res}")


 
      