
import MandelbrotPkg.mandel_python.mandelbrot_1 as mpy
import MandelbrotPkg.mandel_numpy.mandelbrot_2 as mnp
import MandelbrotPkg.mandel_cython.mandelbrot_cython as mcy
import MandelbrotPkg.mandel_swig.mandelbrot_swig as msw
import numpy as np
import time

def compute_mandelbrot(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time = 1000, impl_type = "numpy", plot_filename = None):
    """Function that calls a mandelbrot implementation (depending on impl_type) and
    computes the escape time array (Mandelbrot set) for the given region and resolution.

    Args:
        xmin (float): Parameter specifying the minimum x-value for the grid
        xmax (float): Parameter specifying the maximum x-value for the grid
        ymin (float): Parameter specifying the minimum y-value for the grid
        ymax (float): Parameter specifying the maximum y-value for the grid
        Nx (int): The number of points in the grid in the x-direction
        Ny (int): The number of points in the grid in the y-direction
        max_escape_time (int): Number of iterations to be carried out (on each point) before we conclude a point is in the M-set
        impl_type (str): String specifying which of the four mandelbrot implementations to call
        filename (str): [Optional] Name of image file to which the plot will be saved (if not None)

    Returns:
        escape_iter_array (array[int]): 2D-array with number of iterations before a point is recognised to be outside the M-set
    """
    time_start = time.clock()   # Initial time before execution of implementation impl_type

    if (impl_type == "python"):
        escape_iter_array = mpy.mb_python(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time)

    elif (impl_type == "numpy"):
        escape_iter_array = mnp.mb_numpy(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time)

    elif (impl_type == "cython"):
        escape_iter_array = mcy.mb_cython(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time)

    elif (impl_type == "swig"):
        escape_iter_array = msw.mb_swig(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time, Nx * Ny)
        escape_iter_array = np.reshape(escape_iter_array, (Nx, Ny))     # reshape 1D- into 2D-array.

    else:
        print("Error: Invalid implementation type. Valids are: python - numpy - cython - swig")

    time_end = time.clock()     # Final time after execution of implementation impl_type
    print("Execution with {0}-implementation took {1:.2f} seconds".format(impl_type, time_end - time_start))

    return np.asarray(escape_iter_array)
