
from matplotlib import pyplot as plt

def mb_visualize(escape_iter_array, x_min, x_max, y_min, y_max, width, height, max_escape_iter):
    """Function that takes in a list/array of escape times for the mandelbrot computations and creates an image
    giving a visual representation of the mandelbrot set. Here the coloring is such that each gridpoints is given
    a RGB (list with 3 values) value that depends on the number of iterations before exceeding 2 in absolute value.

    Args:
        escape_iter_array (array/list[int]): 2D-array/list of escape times for all gridpoints
        x_min (float): Parameter specifying the minimum x-value for the grid
        x_max (float): Parameter specifying the maximum x-value for the grid
        y_min (float): Parameter specifying the minimum y-value for the grid
        y_max (float): Parameter specifying the maximum y-value for the grid
        width (int): The number of points in the grid in the x-direction
        height (int): The number of points in the grid in the y-direction
        max_escape_iter (int): Number of iterations to be carried out (on each point) before we conclude a point is in the M-set
    """
    image_array = [[[0.0 for k in range(3)] for j in range(width)] for i in range(height)]   # 3D-list to store RGB values for gridpoints
    
    for i in range(height):
        for j in range(width):
            if (escape_iter_array[i][j] == max_escape_iter):    # If current point is inside the M-set
                image_array[i][j] = [0.0, 0.0, 0.0]             # Give points in the M-set "color" black

            else:                                               # If current point not inside the M-set
                norm_iter = escape_iter_array[i][j] / max_escape_iter                   # Normalize escape time to give value in [0, 1]
                image_array[i][j]  = [20 * norm_iter, 20 * norm_iter, 20 * norm_iter]   # Assign a RGB value to point depending on the escape time

    plt.imshow(image_array, extent = [x_min, x_max, y_min, y_max])      # Use imshow()-function to display the escape time RGB array
    plt.show()                                                          # Make plot stay on screen