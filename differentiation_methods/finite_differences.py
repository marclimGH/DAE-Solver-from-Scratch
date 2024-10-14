import numpy as np

def finite_differences(G, x, epsilon=1e-8):
    n = len(x)
    J = np.zeros((n, n))
    perturb = np.zeros(n)
    
    G_x = G(x)
    
    for j in range(n):
        perturb[j] = epsilon
        G_x_plus = G(x + perturb)
        J[:, j] = (G_x_plus - G_x) / epsilon
        perturb[j] = 0.0
    
    return J