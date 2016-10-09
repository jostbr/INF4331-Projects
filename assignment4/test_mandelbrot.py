
"""Test script that (through py.test) tests if the compute_mandelbrot function behaves as it
should for regions which are either entirely outside or entirely inside the Mandelbrot set.
In both these tests we run them on all 4 different implementations to verify all of them.

How to run this script:
> pyt.test test_mandelbrot.py

Comment on interpretation of parts of exercise 4.6:
Based on the formulation of the 2 tests that should be created, I interpretated this as making
this test script and calling compute_mandelbrot() and assumed we were not supposed to integrate
the test into for example the CLI so that the user would get a message that she/he choose a
region entirely outside or entirely indide the Mandelbrot set. This is also stated in README.txt.
"""

import numpy as np
from MandelbrotPkg.compute import compute_mandelbrot as cm

def test_compute_mandelbrot():
    """First we conduct a test for the (entirely outside) region [3, 4] x [3, 4]. Here we expect the function
    to return 1 for all gridpoints meaning that for each gridpoint the loop breaks after 1 iteration (which
    in this implementation corresponds to 0 iterations in the exercise text) even if we specify 1000 iterations."""
    expected = np.ones((200, 200), dtype = np.int16)
    assert np.array_equal(cm(3.0, 4.0, 3.0, 4.0, 200, 200, 1000, impl_type = "python"), expected)
    assert np.array_equal(cm(3.0, 4.0, 3.0, 4.0, 200, 200, 1000, impl_type = "numpy"), expected)
    assert np.array_equal(cm(3.0, 4.0, 3.0, 4.0, 200, 200, 1000, impl_type = "cython"), expected)
    assert np.array_equal(cm(3.0, 4.0, 3.0, 4.0, 200, 200, 1000, impl_type = "swig"), expected)

def test_compute_mandelbrot_entirely_inside():
    """Secondly we conduct a test for the (entirely inside) region [-0.5, 0.0] x [-0.20, 0.20]. Here we expect
    the function to return max_escape_iter (in this test case 1000) for all points, meaning that the loop never
    breaks on any gridpoint and it continues all the way up to 1000 iterations for each gridpoint."""
    expected = np.full((200, 200), 1000, dtype = np.int16)
    assert np.array_equal(cm(-0.50, 0.0, -0.20, 0.20, 200, 200, 1000, impl_type = "python"), expected)
    assert np.array_equal(cm(-0.50, 0.0, -0.20, 0.20, 200, 200, 1000, impl_type = "numpy"), expected)
    assert np.array_equal(cm(-0.50, 0.0, -0.20, 0.20, 200, 200, 1000, impl_type = "cython"), expected)
    assert np.array_equal(cm(-0.50, 0.0, -0.20, 0.20, 200, 200, 1000, impl_type = "swig"), expected)
