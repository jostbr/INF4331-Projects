
from distutils.core import setup, Extension
from Cython.Distutils import build_ext
import numpy
import os

setup(name = "MandelbrotPkg", version = "1.0", cmdclass = {"build_ext": build_ext},
      py_modules = ["MandelbrotPkg.visualize_mandelbrot", "MandelbrotPkg.compute",
      				"MandelbrotPkg.mandel_python.mandelbrot_1", "MandelbrotPkg.mandel_numpy.mandelbrot_2",
      				"MandelbrotPkg.mandel_cython.mandelbrot_3", "MandelbrotPkg.mandel_swig.mandelbrot_4"],
      ext_modules = [Extension("MandelbrotPkg.mandel_cython.mandelbrot_cython", ["MandelbrotPkg/mandel_cython/mandelbrot_cython.pyx"]),
                     Extension("MandelbrotPkg.mandel_swig._mandelbrot_swig", ["MandelbrotPkg/mandel_swig/mandelbrot_swig.c",
                                                                              "MandelbrotPkg/mandel_swig/mandelbrot_swig.i"],
                                                                              include_dirs = [numpy.get_include(), "."])])