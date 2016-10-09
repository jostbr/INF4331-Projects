
import time
import numpy as np
import mandelbrot_swig

if (__name__ == "__main__"):
    """This script is only made for calling/testing mc_swig in mandelbrot_swig.c and was made according to he filename
    mandelbrot_4.py requested in the exercise. Note that the answer to exercise 4.4 is mainly in the mandelbrot.c file,
    but also necessary files consists of mandelbrot_swig.h, mandelbrot_swig.i, numpy.i and setup.py."""

    x_min = -2.5; x_max = 1.0; y_min = -1.0; y_max = 1.0;
    width = 200; height = 200; grid_points = width * height; max_escape_iter = 1000;
    escape_iter_array = np.zeros(grid_points, dtype = np.int16)

    time_start = time.clock()
    escape_iter_array = mandelbrot_swig.mb_swig(x_min, x_max, y_min, y_max, width, height, max_escape_iter, grid_points)
    time_stop = time.clock()
    print("Execution took {0:.2f} seconds".format(time_stop - time_start))
    escape_iter_array = np.reshape(escape_iter_array, (height, width))

    visualize_mandelbrot.visualize_mb(escape_iter_array, x_min, x_max, y_min, y_max, width, height, max_escape_iter)
