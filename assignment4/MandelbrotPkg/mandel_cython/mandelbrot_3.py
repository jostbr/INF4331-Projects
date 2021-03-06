
import time
import numpy as np
import mandelbrot_cython

if (__name__ == "__main__"):
    """This script is made for illustrating the usage of mb_cython in mandelbrot_cython.pyx
    and was made according to he filename mandelbrot_3.py requested in the exercise. Note that
    the answer to exercise 4.3 is mainly in the mandelbrot_cython.pyx file, but setup.py is also
    necessary for the module to wrok and be importable."""

    x_min = -2.5; x_max = 1.0; y_min = -1.0; y_max = 1.0;
    width = 200; height = 200; max_escape_iter = 1000;
    escape_iter_array = np.zeros((height, width), dtype = np.int16)

    time_start = time.clock()
    escape_iter_array = mandelbrot_cython.mb_cython(x_min, x_max, y_min, y_max, width, height, max_escape_iter)
    time_stop = time.clock()
    print("Execution took {0:.2f} seconds".format(time_stop - time_start))
