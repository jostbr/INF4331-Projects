
%module mandelbrot_swig
%{
    #define SWIG_FILE_WITH_INIT
    #include "mandelbrot_swig.h"
%}

%include "numpy.i"
%init %{
import_array();
%}

%apply (int DIM1, int* ARGOUT_ARRAY1) {(int grid_points, int* escape_iter_array)}
%include "mandelbrot_swig.h"