import numpy as np
from optimize_algorithm import PSO

def rastrigin(x):

    """
    Calculate the Rastrigin function for a given input array.

    The Rastrigin function is a non-convex function used as a performance
    test problem for optimization algorithms. It is a typical example of
    non-linear multimodal functions. The function is defined as:

        f(x) = 10 * n + sum(x_i^2 - 10 * cos(2 * pi * x_i))

    where n is the dimensionality of the input array x.

    Parameters:
    x (array-like): Input array or list of values for which the Rastrigin
                    function is to be calculated.

    Returns:
    float: The calculated value of the Rastrigin function for the input array.
    """


    return 10 * len(x) + sum(xi**2 - 10 * np.cos(2 * np.pi * xi) for xi in x)

bounds = [(-5.12, 5.12)] * 2

pso = PSO(func=rastrigin, dim=2, bounds=bounds, iterations=50)
pso.optimize()

print("Best Solution:", pso.gbest_position)
print("Best Fitness:", pso.gbest_value)
pso.plot_convergence()
