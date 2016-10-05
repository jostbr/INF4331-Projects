
import time
import numpy as np
from matplotlib import pyplot as plt
from mandelbrot_1 import visualize_mandelbrot

def mandelbrot_numpy(x_min, x_max, y_min, y_max, grid_size, max_escape_iter = 1000):
    """Function that computes the escape times (number of iterations of the sequence f_c(0),f_c(f_c(0)),..., where f_c(z) = z² + c,
    before it encounters an element of the sequence for which the absolute value (modulus) exceeds 2) for all the complex numbers
    in the xy-plane defined by the arguments supplied to the function. This implementation utilises NumPy-arrays and vectorization.

    Args:
        x_min (float): Parameter specifying the minimum x-value for the grid
        x_max (float): Parameter specifying the maximum x-value for the grid
        y_min (float): Parameter specifying the minimum y-value for the grid
        y_max (float): Parameter specifying the maximum y-value for the grid
        grid_size (int): The number of points in the grid (both x- and y-direction)
        max_escape_iter (int): The number of iterations to be carried out (on each point) before we conclude a point is in the M-set

    Returns:
        escape_iter_array (array[int]): 2D-array with number of iterations before a point is recognised to be outside the M-set
    """
    x, y = np.meshgrid(np.linspace(x_min, x_max, grid_size), np.linspace(y_min, y_max, grid_size))  # Create mesh-matrices x and y
    escape_iter_array = np.zeros((grid_size, grid_size), dtype = np.int)        # 2D-array to store escape times for gridpoints
    outside_current_iter = np.zeros((grid_size, grid_size), dtype = np.bool)    # 2D-array to be mak for gridpoints outside M-set
    z_complex = np.zeros((grid_size, grid_size), dtype = np.complex128)         # 2D-array to store evolution of sequence at each gridpoint
    c_complex = x + y * 1j      # Let c be the complex number made up of x- and y-coordinate as real and imaginary part respectively
    current_iter = 1            # Variable to hold the current number of iterations of the computation of the sequence f(0),f(f(0)),...

    while (current_iter < max_escape_iter):                     # While we haven't exceeded the maximum set escape time
        z_complex = z_complex ** 2 + c_complex                  # Computing (vecorization) the sequence mandelbrot sequence f(0),f(f(0)),...
        outside_current_iter = (abs(z_complex) > 2)             # 2D-mask with True for gridpoints that gives abs() > 2
        escape_iter_array[outside_current_iter] = current_iter  # Store escape time for all gridpoints outside M-set on this iteration
        z_complex[outside_current_iter] = 0.0                   # "Terminate" sequence for gridpoints outside M-set on this iteration
        c_complex[outside_current_iter] = 0.0                   # "Terminate" sequence for gridpoints outside M-set on this iteration
        current_iter = current_iter + 1                         # Increment iteraton variable with one to keep track of current iteration

    escape_iter_array[(escape_iter_array == 0)] = max_escape_iter   # Escape time for gridpoints within within M-set is set to max_escape_iter
    return escape_iter_array                                        # Return escape time array and exit function

if (__name__ == "__main__"):
    x_min = -2.5; x_max = 1; y_min = -1; y_max = 1;     # Set parameters
    grid_size = 200; max_escape_iter = 1000;           # Set parameters

    time_start = time.clock()
    escape_iter_array = mandelbrot_numpy(x_min, x_max, y_min, y_max, grid_size, max_escape_iter)    # Call to the pure Python version
    time_stop = time.clock()
    print("Execution took {0:.2f} seconds".format(time_stop - time_start))

    visualize_mandelbrot(escape_iter_array, x_min, x_max, y_min, y_max, grid_size, max_escape_iter) # Visualize the results using matplotlib