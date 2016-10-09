
import MandelbrotPkg.mandel_python.mandelbrot_1 as mpy
import MandelbrotPkg.mandel_numpy.mandelbrot_2 as mnp
import MandelbrotPkg.mandel_cython.mandelbrot_cython as mcy
import MandelbrotPkg.mandel_swig.mandelbrot_swig as msw
import MandelbrotPkg.visualize_mandelbrot as vm
import numpy as np

def compute_mandelbrot(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time = 1000, impl_type = "numpy", plot_filename = None):
	if (impl_type == "python"):
		escape_iter_array = mpy.mb_python(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time)
	elif (impl_type == "numpy"):
		escape_iter_array = mnp.mb_numpy(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time)
	elif (impl_type == "cython"):
		escape_iter_array = mcy.mb_cython(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time)
	elif (impl_type == "swig"):
		escape_iter_array = msw.mb_swig(xmin, xmax, ymin, ymax, Nx, Ny, max_escape_time, Nx * Ny)
		escape_iter_array = np.reshape(escape_iter_array, (Nx, Ny))

	return np.asarray(escape_iter_array)
