
import time
from matplotlib import pyplot as plt

def mandelbrot_python(x_min, x_max, y_min, y_max, grid_size, max_escape_iter = 1000):
    """Function that computes the escape times (number of iterations of the sequence f_c(0),f_c(f_c(0)),..., where f_c(z) = z² + c,
    before it encounters an element of the sequence for which the absolute value (modulus) exceeds 2) for all the complex numbers
    in the xy-plane defined by the arguments supplied to the function. This implementation uses only basic Python for computation.

    Args:
        x_min (float): Parameter specifying the minimum x-value for the grid
        x_max (float): Parameter specifying the maximum x-value for the grid
        y_min (float): Parameter specifying the minimum y-value for the grid
        y_max (float): Parameter specifying the maximum y-value for the grid
        grid_size (int): The number of points in the grid (both x- and y-direction)
        max_escape_iter (int): The number of iterations to be carried out before we conclude a point is in the M-set

    Returns:
        escape_iter_array (array[int]): 2D-array with number of iterations before a point is recognised to be outside the M-set
    """
    escape_iter_array = [[0 for j in range(grid_size)] for k in range(grid_size)]   # 2D-list to store escape times for gridpoints
    delta_x = (x_max - x_min) / (grid_size - 1.0)   # Distance between gridpoints in the x-direction
    delta_y = (y_max - y_min) / (grid_size - 1.0)   # Distance between gridpoints in the y-direction

    for i in range(grid_size):
        for j in range(grid_size):
            c_complex = complex(x_min + i * delta_x, y_min + j * delta_y)   # Current c-value is the (i, j)'th gridpoint made complex
            z_complex = complex(0, 0)   # z initally has the value 0 + 0j before computing the sequence f(0),f(f(0)),...
            current_iter = 0            # Variable to hold the current number of iterations of the computation of the sequence

            while (abs(z_complex) < 2 and current_iter < max_escape_iter):  # While sequence doesn't exceed 2 in abs-val and max esc-time not reached
                z_complex = z_complex ** 2 + c_complex      # Computing the sequence mandelbrot sequence f(0),f(f(0)),...
                current_iter = current_iter + 1             # Increment iteraton variable with one to keep track of current iteration

            escape_iter_array[j][i] = current_iter      # Store escape time for gridpoint (escape time is max_escape_time for points in the M-set)

    return escape_iter_array    # Return escape time list and exit function


def visualize_mandelbrot(escape_iter_array, x_min, x_max, y_min, y_max, grid_size, max_escape_iter):
    """Function that takes in a list/array of escape times for the mandelbrot computations and creates an image
    giving a visual representation of the mandelbrot set. Here the coloring is such that each gridpoints is given
    a RGB (list with 3 values) value that depends on the number of iterations before exceeding 2 in absolute value.

    Args:
        x_min (float): Parameter specifying the minimum x-value for the grid
        x_max (float): Parameter specifying the maximum x-value for the grid
        y_min (float): Parameter specifying the minimum y-value for the grid
        y_max (float): Parameter specifying the maximum y-value for the grid
        grid_size (int): The number of points in the grid (both x- and y-direction)
        max_escape_iter (int): The number of iterations to be carried out before we conclude a point is in the M-set
    """
    image_array = [[[0.0 for i in range(3)] for j in range(grid_size)] for k in range(grid_size)]   # 3D-list to store RGB values for gridpoints
    for i in range(grid_size):
        for j in range(grid_size):
            if (escape_iter_array[i][j] == max_escape_iter):    # If current point is inside the M-set
                image_array[i][j] = [0.0, 0.0, 0.0]             # Give points in the M-set color black

            else:                                               # If current point not inside the M-set
                norm_iter = escape_iter_array[i][j] / max_escape_iter                   # Normalize escape time to give value in [0, 1]
                image_array[i][j]  = [15 * norm_iter, 15 * norm_iter, 15 * norm_iter]   # Assign a RGB value to point depending on the escape time

    plt.imshow(image_array, extent = [x_min, x_max, y_min, y_max])      # Use imshow()-function to display the escape time RGB array
    plt.show()                                                          # Make plot stay on screen

if (__name__ == "__main__"):
    x_min = -2.5; x_max = 1; y_min = -1; y_max = 1
    grid_size = 200; max_escape_iter = 1000

    time_start = time.clock()
    escape_iter_array = mandelbrot_python(x_min, x_max, y_min, y_max, grid_size, max_escape_iter)
    time_stop = time.clock()
    print("Execution took {0:.2f} seconds".format(time_stop - time_start))

    visualize_mandelbrot(escape_iter_array, x_min, x_max, y_min, y_max, grid_size, max_escape_iter)
