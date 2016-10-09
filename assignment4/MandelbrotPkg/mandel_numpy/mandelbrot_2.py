
import time
import numpy as np
from matplotlib import pyplot as plt

def mb_numpy(x_min, x_max, y_min, y_max, width, height, max_escape_iter = 1000):
    """Function that computes the escape times (number of iterations of the sequence f_c(0),f_c(f_c(0)),..., where f_c(z) = z² + c,
    before it encounters an element of the sequence for which the absolute value (modulus) exceeds 2) for all the complex numbers
    in the xy-plane defined by the arguments supplied to the function. This implementation utilises NumPy-arrays and vectorization.

    Args:
        x_min (float): Parameter specifying the minimum x-value for the grid
        x_max (float): Parameter specifying the maximum x-value for the grid
        y_min (float): Parameter specifying the minimum y-value for the grid
        y_max (float): Parameter specifying the maximum y-value for the grid
        width (int): The number of points in the grid in the x-direction
        height (int): The number of points in the grid in the y-direction
        max_escape_iter (int): Number of iterations to be carried out (on each point) before we conclude a point is in the M-set

    Returns:
        escape_iter_array (array[int]): 2D-array with number of iterations before a point is recognised to be outside the M-set
    """
    x, y = np.meshgrid(np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height))  # Create mesh-matrices x and y
    escape_iter_array = np.zeros((height, width), dtype = np.int)   # 2D-array to store escape times for gridpoints
    z = np.zeros((height, width), dtype = np.complex64)             # 2D-array to store evolution of sequence at each gridpoint
    c = x + y * 1j      # Let c be the complex number made up of x- and y-coordinate as real and imaginary part respectively

    for current_iter in range(0, max_escape_iter):
        below_limit = (z.real * z.real + z.imag * z.imag < 4.0)    # 2D-mask with True for gridpoints that gives abs() < 2
        z[below_limit] = z[below_limit] ** 2 + c[below_limit]      # Keep computing sequence only for points still abs() < 2
        escape_iter_array[below_limit] = current_iter + 1          # Update escape time for all gridpoints with still abs() < 2

    return escape_iter_array    # Return escape time array and exit function

if (__name__ == "__main__"):
    x_min = -2.5; x_max = 1; y_min = -1.0; y_max = 1.0;
    width = 200; height = 200; max_escape_iter = 1000;

    time_start = time.clock()
    escape_iter_array = mb_numpy(x_min, x_max, y_min, y_max, width, height, max_escape_iter)
    time_stop = time.clock()
    print("Execution took {0:.2f} seconds".format(time_stop - time_start))

    visualize_mandelbrot.visualize_mb(escape_iter_array, x_min, x_max, y_min, y_max, width, height, max_escape_iter)