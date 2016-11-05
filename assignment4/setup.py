
"""Installation script (using distutils) for Package MandelbrotPkg. Comment on usage:
- To install this package in the current directory, run this setup.py (while having MandelbrotPkg in
  the same directory) with the following two commands. This will compile and link the cython and swig
  version and make them vailable modules in the package. It will also make the pure python files
  mandelbort_1.py, mandelbrot_2.py, visualize_mandelbrot.py and compute.py available modules.

  > python setup.py build_ext
  > python setup.py install --install-platlib=.
"""
from distutils.core import setup, Extension
from Cython.Distutils import build_ext
import numpy
import os

setup(name = "MandelbrotPkg", version = "1.0", cmdclass = {"build_ext": build_ext},
      py_modules = ["MandelbrotPkg.visualize_mandelbrot", "MandelbrotPkg.compute",
      				"MandelbrotPkg.mandel_python.mandelbrot_1", "MandelbrotPkg.mandel_numpy.mandelbrot_2",
      				"MandelbrotPkg.mandel_cython.mandelbrot_3", "MandelbrotPkg.mandel_swig.mandelbrot_4"],
      ext_modules = [Extension("MandelbrotPkg.mandel_cython.mandelbrot_cython", ["MandelbrotPkg/mandel_cython/mandelbrot_cython.pyx"]),
                     Extension("MandelbrotPkg.get_colors_cython", ["MandelbrotPkg/get_colors_cython.pyx"]),
                     Extension("MandelbrotPkg.mandel_swig._mandelbrot_swig", ["MandelbrotPkg/mandel_swig/mandelbrot_swig.c",
                                                                              "MandelbrotPkg/mandel_swig/mandelbrot_swig.i"],
                                                                              include_dirs = [numpy.get_include(), "."])])