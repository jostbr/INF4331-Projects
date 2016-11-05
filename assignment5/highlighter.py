
import re
import sys, os

help_string = """\n------------------------------------------------------------------\
-----------------
This program takes in a syntax file, a theme/coloring file and a source code file
(to color) and prints out the colored source code. Below are examples on how to run
this script to syntax highlight code or to show help:

> python highlighter.py syntax_file.syntax theme_file.theme <source_code_to_color>
> pyhton highlighter.py --help
-----------------------------------------------------------------------------------\n"""

def handle_input(cmd_line_args):
    """Function that handles cmd-line args sent in by user and checks if
    there was invalid input and similar. If everything is OK, it returns
    filenames for the syntax, theme and source file."""
    try:
        if ("--help" in cmd_line_args):
            print(help_string)
            sys.exit()

        syntax_filename = cmd_line_args[0]      # Try to extract syntax filename
        theme_filename = cmd_line_args[1]       # Try to extract theme filename
        source_filename = cmd_line_args[2]      # Try to extract source filename

        for filename in cmd_line_args[0:3]:
            if (not os.path.exists(filename)):
                raise IOError     # Check if all files are valid, else raise IOError

    except IndexError:
        sys.exit("\nError: Invalid use of cmd-line args. See --help.\n")

    except IOError:
        sys.exit("\nError: File {0} is not an existing file\n".format(filename))

    return syntax_filename, theme_filename, source_filename

def get_regex_dict(syntax_filename):
    """Function that opens the file syntax_filename, reads in all data and returns it in a
    dictionary with the "key: value"-structure "syntax_type: regex" where syntax_type is
    a name describing what part of syntax the regular expression regex is referring to."""
    regex_dict = dict()     # Dictionary to store the above mentioned data

    with open(syntax_filename, "r") as syntax_file:
        for line_num, current_line in enumerate(syntax_file):
            regex = ":".join(current_line.split(":")[:-1])[1:-1]   # Read regex from current_line
            syntax_type = current_line.split(":")[-1].strip()      # Read synta_type from current_line
            regex_dict[syntax_type] = regex                        # Put the key-value pair in dict

    return regex_dict

def get_color_dict(theme_filename):
    """Function that opens the file theme_filename, reads in all data and returns it in a
    dictionary with the "key: value"-structure "syntax_type: color_code" where syntax_type
    is a name describing what part of syntax that should be colored with the code color_code."""
    color_dict = dict()     # Dictionary to store the above mentioned data

    with open(theme_filename, "r") as theme_file:
        for line_num, current_line in enumerate(theme_file):
            color_code = current_line.split(":")[-1].strip()    # Read color_code form current_line
            syntax_type = current_line.split(":")[0].strip()    # Read synta_type from current_line
            color_dict[syntax_type] = color_code                # Put the key-value pair in dict

    return color_dict

def get_colored_source(source_filename, regex_dict, color_dict):
    """Function that generates a modified version of the source code in source_filename in which
    each part of the syntax (that is requested to be colored) is encapsulated inside a bash
    color code string gicing the desired color upon a print of the modified source code.

    Args:
        source_filename (str): Filename for the source code file to be colored
        regex_dict (dict): Dictionary describing what parts of the syntax to be colored
        color_dict (dict): Dictionary describing what colors to give the varioues parts of syntax

    Returns:
        source_code (str): Colored version of the source code with bash color codes
    """
    start_color = "\033[{}m"    # Initial part. Color code to be inserted in "{}"
    end_color = "\033[0m"       # Final part of the color sequence. Terminates it.

    with open(source_filename, "r") as source_file:
        source_code = source_file.read()    # Read in entire source code in a string

    # For each syntax_type and regex; color the syntax matched by regex with the color
    # color_dict[syntax_type] using re.sub() and backreferrencing the matching string.
    for syntax_type, regex in regex_dict.items():
        repl = start_color.format(color_dict[syntax_type]) + r"\1" + end_color
        source_code = re.sub(r"(" + regex + r")", repl, source_code, flags = re.MULTILINE)

    return source_code

if (__name__ == "__main__"):
    syntax_fn, theme_fn, source_fn = handle_input(sys.argv[1:])             # Get filenames
    regex_dict = get_regex_dict(syntax_fn)                                  # Read regex data
    color_dict = get_color_dict(theme_fn)                                   # Read color data
    colored_source = get_colored_source(source_fn, regex_dict, color_dict)  # Get colored version
    print(colored_source)                                                   # Finallt print to screen