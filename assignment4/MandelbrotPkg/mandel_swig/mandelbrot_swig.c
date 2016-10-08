
# include <stdio.h>

void mb_swig(double x_min, double x_max, double y_min, double y_max, int width, int height, int max_escape_iter, int grid_points, int* escape_iter_array){
    /*Function that computes the escape times (number of iterations of the sequence f_c(0),f_c(f_c(0)),..., where f_c(z) = z² + c,
    before it encounters an element of the sequence for which the absolute value (modulus) exceeds 2) for all the complex numbers in the
    xy-plane defined by the arguments supplied to the function. This implementation is purely in C na dcallable from Python through SWIG.

    Args:
        x_min (float): Parameter specifying the minimum x-value for the grid
        x_max (float): Parameter specifying the maximum x-value for the grid
        y_min (float): Parameter specifying the minimum y-value for the grid
        y_max (float): Parameter specifying the maximum y-value for the grid
        width (int): The number of points in the grid in the x-direction
        height (int): The number of points in the grid in the y-direction
        max_escape_iter (int): Number of iterations to be carried out (on each point) before we conclude a point is in the M-set

    Returns (more like alters the values in memory locations in the input array. No explicit return statement):
        escape_iter_array (array[int]): 1D-array with number of iterations before each point is recognised to be outside the M-set
    */
    double c_real, c_imag;                              // Real and imaginary part of a given gridpoint
    double z_real, z_imag;                              // Real and imaginary part of sequence f_c(0),f_c(f_c(0)),...
    double z_real_sq, z_imag_sq;                        // Real and imaginary part of square of sequence
    double delta_x = (x_max - x_min) / (width - 1.0);   // Distance between gridponts in x-direction
    double delta_y = (y_max - y_min) / (height - 1.0);  // Distance between gridponts in y-direction
    int i, j, k;

    for (i = 0; i < height; i++){
        for (j = 0; j < width; j++){
            c_real = x_min + j * delta_x;                       // Real part (x-coor) of current gridpoint
            c_imag = y_min + i * delta_y;                       // Imaginary part (y-coor) of current gridpoint
            z_real = 0.0; z_imag = 0.0;                         // Initial value of z for each gridpoint is zero
            escape_iter_array[j + i * width] = max_escape_iter;

            for (k = 0; k < max_escape_iter; k++){
                z_real_sq = z_real * z_real;                // Computing square of real part because needed twice below
                z_imag_sq = z_imag * z_imag;                // Computing square of imag part because needed twice below

                if (z_real_sq + z_imag_sq > 4.0){           // If recogniced outside M-se equvialent with abs(z) > 2
                    escape_iter_array[j + i * width] = k;   // Store (in 1D-array) number of iterations before outside M-set
                    break;                                  // Break the innermost loop and move on to the next gridpoint
                }

                z_imag = 2.0 * z_real * z_imag + c_imag;    // Updating the imaginary part of z
                z_real = z_real_sq - z_imag_sq + c_real;    // Updating the real part of z
            }
        }
    }
}
