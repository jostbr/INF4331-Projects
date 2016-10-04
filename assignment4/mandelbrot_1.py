
import time
from matplotlib import pyplot as plt

def mandelbrot_python(x_min, x_max, y_min, y_max, grid_size = 200, max_escape_iter = 1000):
    image_array = [[[0.0 for i in range(3)] for j in range(grid_size)] for k in range(grid_size)]
    delta_x = (x_max - x_min) / (grid_size - 1.0)
    delta_y = (y_max - y_min) / (grid_size - 1.0)

    for i in range(grid_size):
        for j in range(grid_size):
            c_complex = complex(x_min + i * delta_x, y_min + j * delta_y)
            z_complex = complex(0, 0)
            current_iter = 0

            while (abs(z_complex) < 2 and current_iter < max_escape_iter):
                z_complex = z_complex ** 2 + c_complex
                current_iter = current_iter + 1

            image_array[j][i] = get_pixel_RGB(current_iter / max_escape_iter)

    plt.imshow(image_array, extent = [x_min, x_max, y_min, y_max])
    plt.show()

def get_pixel_RGB(norm_iter):
    if (norm_iter == 1):
        return [0.0, 0.0, 0.0]

    else:
        return [8 * norm_iter, 8 * norm_iter, 8 * norm_iter]

if (__name__ == "__main__"):
    time_start = time.clock()
    mandelbrot_python(-2.5, 1, -1, 1)
    time_stop = time.clock()
    print("Execution took {0:.2f} seconds".format(time_stop - time_start))
