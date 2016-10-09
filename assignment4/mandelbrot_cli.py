
import MandelbrotPkg.visualize_mandelbrot as vm
import MandelbrotPkg.compute as cm
import time, sys, os
import numpy as np

class CommandLineInterface(object):
    """Class that operates the Comamnd-Line-Interface. The constructor initates some lists/dicts holding
    info about the various parameters needed for the mandelbrot computations. The get_parameters_from_user()
    method interacts with the user in order get the values which the user wants to use."""
    help_text = """
\n-------------------------------------------------------------------------------------
HOW TO RUN AND USE mandelbrot_cli.py:
> python mandelbrot_cli.py
    Run with no command line arguments to start a CLI-session and then follow the
    on-screen instructions to set up the mandelbrot computations with you preferred
    implementation and parameter values Here each step gives you help underways.

> python mandelbrot_cli.py <implemenatation>
    Run with CLI-session with implementation type given on the command line. When
    doing this the CLI-session will skip the question about which implementation
    to use an instead use the one supplied on the command line

> python mandelbrot_cli.py --help
    Run with command line argument --help to view this help message.
-------------------------------------------------------------------------------------\n\n"""
    def __init__(self):
        """Defining attributes to store values of arguments needed for compute_mandelbrot().
        In self.arg_vals, values for arguments are stored and are also given default values."""
        self.args =["x_min", "x_max", "y_min", "y_max", "width", "height", "max_escape_iter", "filename"]
        self.arg_vals = {"x_min": -2.25, "x_max": 1.0, "y_min": -1.25, "y_max": 1.25,
            "width": 200, "height": 200, "max_escape_iter": 1000, "filename": None}
        self.arg_help = {"x_min": "Minimum x-value for the wanted region", "x_max": "Maximum x-value for the wanted region",
            "y_min": "Minimum y-value for the wanted region", "y_max": "Maximum y-value for the wanted region",
            "width": "Number of points in x-direction in region", "height": "Number of points in y-direction in region",
            "max_escape_iter": "Max number of iterations on each point"}
        self.valid_implementations = ["python", "numpy", "cython", "swig"]
        self.implementation = None

    def get_parameters_from_user(self):
        """Method handles interaction with user to get parameters for compute_mandelbrot()."""
        os.system("cls" if os.name == "nt" else "clear")    # Clear terminal for aesthetics
        print("\n\nWelcome to the Command-Line_Interface for the MandelbrotPkg package.")
        print("You'll be taken through som steps to customize computations to your liking")
        print("------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------")

        if (self.implementation is None):   # Only ask for implementation when it is not supplied by cmd-line arg
            print("\nIn this package there are four different implementations:\npython -- numpy -- cython -- swig\n")
            implementation_registered = False
        else:
            implementation_registered = True

        while (not implementation_registered):  # Keep asking for implementation until user enters valid
            user_implementation = input("Which implementation would you like to use? \n").rstrip().lower()

            if (user_implementation in self.valid_implementations):
                self.implementation = user_implementation       # Accept valid implementation
                implementation_registered = True                # Has been registered -> move on
            else:
                print("\nInvalid implementation. See above for allowed names and try again.")

        if (input("\nWould you like to save an image of the results when done [y/n]? ").rstrip() == "y"):
            self.arg_vals["filename"] = input("Filename for image (without extension): ") + ".png"
        else:
            print("Okey; you either choose not to save image or answered invalidally")

        if (input("\nDo you want to enter custom parameters (if not, default is used) [y/n]? ").rstrip() == "y"):
            for arg in self.args:               # Ask user for value for each parameter
                value_registered = False

                while (not value_registered):   # Keep asking user, per parameter, until valid type entered
                    if (arg in self.args[0:4]): # The parameters of type float
                        try:
                            self.arg_vals[arg] = float(input(self.arg_help[arg] + " - {0}: ".format(arg)).rstrip())
                        except ValueError:
                            print("Invalid type for parameter {0}. Must be type '{1}'\n".format(arg, "float"))
                            continue

                    elif (arg in self.args[4:-1]):  # The parameters of type int
                        try:
                            self.arg_vals[arg] = int(input(self.arg_help[arg] + " - {0}: ".format(arg)).rstrip())
                        except ValueError:
                            print("Invalid type for parameter {0}. Must be type '{1}'\n".format(arg, "int"))
                            continue

                    value_registered = True     # Has eneterd valid type -> move on to next parameter

        else:
            print("Default parameter values will be used")

if (__name__ == "__main__"):
    """This part initiates a Comamnd-Line-Interface session and queries user to obtain
    values for parameters which are then passed on to the compute_mandelbrot()-function."""
    cli_session = CommandLineInterface()

    if ((len(sys.argv) == 2) and (sys.argv[1] == "--help")):
        print(CommandLineInterface.help_text)   # Display instructions when user gives --help on command line
        sys.exit()

    elif ((len(sys.argv) <= 2)):
        if (len(sys.argv) == 1):
            pass    # Pass and ask user for implenetation type in CLI instead
        
        elif ((len(sys.argv) == 2) and (sys.argv[1].replace("-", "") in cli_session.valid_implementations)):
            cli_session.implementation = sys.argv[1].replace("-", "")   # Accept user requested implementation

        else:
            print("\nError: Invalid implementation. Valids are: \n{0}\n".format(" - ".join(cli_session.valid_implementations)))
            sys.exit()

        cli_session.get_parameters_from_user()  # Get parameters and update instance attributes

        # Call compute_mandelbrot()-function with the parameters specified by the user.
        escape_iter_array = cm.compute_mandelbrot(cli_session.arg_vals["x_min"], cli_session.arg_vals["x_max"],
            cli_session.arg_vals["y_min"], cli_session.arg_vals["y_max"], cli_session.arg_vals["width"],
            cli_session.arg_vals["height"], cli_session.arg_vals["max_escape_iter"], cli_session.implementation,
            cli_session.arg_vals["filename"])

        # Call visualize_mb()-function to plot the escape times in the xy-plane
        vm.visualize_mb(escape_iter_array, cli_session.arg_vals["x_min"], cli_session.arg_vals["x_max"],
            cli_session.arg_vals["y_min"], cli_session.arg_vals["y_max"], cli_session.arg_vals["width"],
            cli_session.arg_vals["height"], cli_session.arg_vals["max_escape_iter"], cli_session.arg_vals["filename"])

    else:
        print("\nError: Invalid use of command line arguments. Run 'mandelbrot_cli.py --help' fro more info\n")