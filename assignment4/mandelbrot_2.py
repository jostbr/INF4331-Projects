
import time
import numpy as np
from matplotlib import pyplot as plt
from mandelbrot_1 import get_pixel_RGB

def mandelbrot_numpy(x_min, x_max, y_min, y_max, grid_size = 1000, max_escape_iter = 1000):
    x, y = np.meshgrid(np.linspace(x_min, x_max, grid_size), np.linspace(y_min, y_max, grid_size))
    image_array = np.zeros((grid_size, grid_size, 3), dtype = np.float32)
    outside_current_iter = np.zeros((grid_size, grid_size), dtype = np.bool)
    z_complex = np.zeros((grid_size, grid_size), dtype = np.complex128)
    c_complex = x + y * 1j
    current_iter = 1

    while (current_iter < max_escape_iter):
        z_complex = z_complex ** 2 + c_complex
        outside_current_iter = (abs(z_complex) > 2)
        image_array[outside_current_iter] = np.array(get_pixel_RGB(current_iter / max_escape_iter))
        z_complex[outside_current_iter] = 0.0
        c_complex[outside_current_iter] = 0.0

        current_iter = current_iter + 1

    plt.imshow(image_array, extent = [x_min, x_max, y_min, y_max])
    plt.show()

if (__name__ == "__main__"):
    time_start = time.clock()
    mandelbrot_numpy(-2.5, 1, -1, 1)
    time_stop = time.clock()
    print("Execution took {0:.2f} seconds".format(time_stop - time_start))
