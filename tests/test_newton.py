import numpy as np
from solvers.nonlinear_solvers import newtonsmethod

def test_newton_simple_system():
    fun = lambda x: np.array([
        x[0] ** 2 + x[1] ** 2 - 4,
        x[0] - x[1]
    ])
    funDer = lambda x: np.array([
        [2 * x[0], 2 * x[1]],
        [1, -1]
    ])
    x0 = np.array([0.1, 0.1])
    root, _ = newtonsmethod(fun, funDer, x0)
    expected = np.array([np.sqrt(2), np.sqrt(2)])
    assert np.allclose(root, expected, atol=1e-6)
