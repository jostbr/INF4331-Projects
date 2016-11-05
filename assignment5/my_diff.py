
import sys, os
from itertools import zip_longest

help_string = """\n------------------------------------------------------------------\
-----------------
This program takes in an original file and a modified file. Then it computes which
changes has been made to the original file in order to make the modified file. Below
are examples on how to run this script.

> python highlighter.py <original_file> <modified_file>
> pyhton highlighter.py --help
-----------------------------------------------------------------------------------\n"""

def handle_input(cmd_line_args):
    """Function that handles cmd-line args sent in by user and checks if there
    was invalid input and similar. If everything is OK, it returns filenames
    for the original file and the modified file."""
    try:
        if ("--help" in cmd_line_args):
            print(help_string)
            sys.exit()

        original_filename = cmd_line_args[0]    # Try to extract original filename
        modified_filename = cmd_line_args[1]    # Try to extract modified filename

        for filename in cmd_line_args[0:2]:
            if (not os.path.exists(filename)):
                raise IOError    # Check if all files are valid, else raise IOError

    except IndexError:
        sys.exit("\nError: Invalid use of cmd-line args. See --help.\n")

    except IOError:
        sys.exit("\nError: File {0} is not an existing file\n".format(filename))

    return original_filename, modified_filename


def compute_difference(original_fn, modified_fn):
    """Function that computes the differences between the original and the modified
    file and stores the result in a new string in which each line that was not modified
    between the two files is preceeded by a "0". If a line was deleted it gets preceeded
    by a "-" and if it was deleted it gets preceeded by a "+".

    Args:
        original_fn (str): Filename of the original file
        modified_fn (str): Filename of the modified file.

    Returns:
        "".join(diff_line_list) (str): String with the computed difference
    """
    diff_line_list = list()     # List to hold each line in the diff string

    # Open both files and loop over each line in both of them simulatnously
    with open(original_fn, "r") as og_file, open(modified_fn, "r") as mod_file:
        for og_line, mod_line in zip_longest(og_file, mod_file):
            if (og_line is None and mod_line is not None):
                diff_line_list.append("+  {0}".format(mod_line))    # Append "+" mod_line if totally new

            elif (og_line is not None and mod_line is None):
                diff_line_list.append("-  {0}".format(og_line))     # Append "-" og_line if totally removed

            else:
                if (not og_line.endswith("\n")):
                    og_line = og_line + "\n"        # Add newline character if og_line is last line of file

                if (not mod_line.endswith("\n")):
                    mod_line = mod_line + "\n"      # Add newline character if mod_line is last line of file

                if (og_line == mod_line):
                    diff_line_list.append("0  {0}".format(og_line))     # Append "0" og_line if not modified

                else:
                    diff_line_list.append("-  {0}".format(og_line))     # Append "-" og_line if replaced
                    diff_line_list.append("+  {0}".format(mod_line))    # Append "+" mod_line as replacement

    return "".join(diff_line_list)


def write_diff_to_file(diff_string, filename):
    """Function that writes string diff_string to file filename"""
    with open(filename, "w") as diff_output_file:
        diff_output_file.write(diff_string)

if (__name__ == "__main__"):
    original_filename, modified_filename = handle_input(sys.argv[1:])          # Get filenames from cmd-line
    diff_string = compute_difference(original_filename, modified_filename)     # Get difference between files
    write_diff_to_file(diff_string, "diff_output.txt")                         # Write difference string to file
    os.system("python highlighter.py diff.syntax diff.theme diff_output.txt")  # Highlight it using highlighter.py
