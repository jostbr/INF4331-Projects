
! Fortran program that solves the advection equation in one spatial dimension and
! time with, cyclic boundary conditions. This program is used fortesting the syntax
! highlighting in the python script highlighter.py

PROGRAM advection_solver
    IMPLICIT NONE
    ! ------------------------------- VARIABLE DECLARATIONS -------------------------------
    double precision, parameter :: L = 50000.0                      ! Location where bell is max
    double precision, parameter :: sigma = L / 10.0                 ! Width of Gaussian bell
    double precision, parameter :: theta_0 = 10.0                   ! Max initial value
    double precision, parameter :: u_0 = 1.0                        ! Advection speed

    double precision, parameter :: C = 0.50                         ! Courant number
    double precision, parameter :: delta_x = sigma / 10.0           ! Spatial resolution
    double precision, parameter :: delta_t = C * delta_x / u_0      ! Temporal resolution

    integer :: j, n                                                 ! Counter variables
    integer :: n_temp, n_curr = 1, n_next = 2                       ! Indicies for timesteps
    integer, parameter :: j_max = idint(L / delta_x + 1)            ! Max number of space points
    integer, parameter :: n_05c = idint((5 * L) / (u_0 * delta_t))  ! Num time points 5 cycles
    integer, parameter :: n_10c = idint((10 * L) / (u_0 * delta_t)) ! Num time points 10 cycles
    integer, parameter :: n_max = idint((15 * L) / (u_0 * delta_t)) ! Num time points 15 cycles

    double precision, dimension(j_max, 2) :: theta = 0.0            ! To store theta at n, n + 1

    character :: output_filename                                    ! Filename for output file
    logical :: some_random_bool1 = .TRUE.                           ! For syntax highlighting
    logical :: some_random_bool2 = .FALSE.                          ! For syntax highlighting

    ! -------------------------------------------------------------------------------------

    ! -------------------------------- INITIAL CONDITION ----------------------------------
    ! Compute initial condition for theta (Gaussian bell)
    do j = 1, j_max
        theta(j, n_curr) = theta_0 * exp(-((2 * &
            ((j - 1) * delta_x) - L) / sigma) ** 2)
    end do
    ! -------------------------------------------------------------------------------------

    ! ---------- GETTING ARGS FROM CMD-LINE AND OPEN .DAT FILE FOR RESULT OUTPUT ----------
    CALL GET_COMMAND_ARGUMENT(1, output_filename)                ! Get filename fomr cmd-line
    open(unit = 10, file = output_filename, form = "formatted")  ! Open that reuslts file
    ! -------------------------------------------------------------------------------------

    ! ------------------- USING UPWIND SCHEME AND BOUNDARY CONDITION ----------------------
    do n = 0, n_max     ! Loop, in time as long as necessary for max num of cycles
        theta(1, n_curr) = theta(j_max, n_curr)     ! BC theta at the left boundary at 0

        do j = 2, j_max
            theta(j, n_next) = theta(j, n_curr) - C * &     ! Use upwind scheme
                (theta(j, n_curr) - theta(j - 1, n_curr))
        end do

        ! Write theta to file for time steps corresponding to the requested cycles.
        if (n == 0 .or. n == n_05c .or. n == n_10c .or. n == n_max) then
            write(unit = 10, fmt = "(102f20.14)") float(n), theta(:, n_curr)

        else if (n == 4.0 * atan(1.0)) then
            print*, "n is not an integer? What?"   ! Random print to show syntax
            exit                                   ! Exit because of strange behaviour

        else
            print*, "n is such that neither of the two above statements got executed"
        end if

        n_temp = n_next     ! Set help index to second theta column (2)
        n_next = n_curr     ! Set next time step index to first theta column (1)
        n_curr = n_temp     ! Set current time step index to second column (2)
    end do
    ! -------------------------------------------------------------------------------------

    close(unit = 10)    ! Close file after writing

    do while (some_random_bool1 .ne. some_random_bool2)
        print("some_random_bool1 is still equal to some_random_bool2")   ! Random stuff
        some_random_bool1 = some_random_bool2                            ! Random stuff
        cycle
    end do

END PROGRAM advection_solver
