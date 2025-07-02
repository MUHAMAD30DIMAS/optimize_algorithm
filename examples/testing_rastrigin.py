import numpy as np

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

    x = np.array(x)
    n = x.size
    return 10 * n + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))