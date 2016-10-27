

import re
import sys, os

help_text = """\n------------------------------------------------------------------\
-----------------
This program takes in a syntax file, a theme/coloring file and a source code file
(to color) and prints out the colored source code Below are examples on how to run
this script to syntax highlight code or to show help:

> python highlighter.py syntax_file.syntax theme_file.theme <source_code_to_color>
> pyhton highlighter.py --help
-----------------------------------------------------------------------------------\n"""

def handle_input(cmd_line_args):
    try:
        if ("--help" in cmd_line_args):
            print(help_text)
            sys.exit()

        syntax_filename = cmd_line_args[0]
        theme_filename = cmd_line_args[1]
        source_filename = cmd_line_args[2]

        for filename in cmd_line_args[0:3]:
            if (not os.path.exists(filename)):
                raise IOError

    except IndexError:
        sys.exit("\nError: Invalid use of cmd-line args. See --help.\n")

    except IOError:
        sys.exit("\nError: File {0} is not in the current directory\n".format(filename))

    return syntax_filename, theme_filename, source_filename

def get_regex_dict(syntax_filename):
    regex_dict = dict()
    with open(syntax_filename, "r") as syntax_file:
        for line_num, current_line in enumerate(syntax_file):
            regex = ":".join(current_line.split(":")[:-1])[1:-1]
            syntax_type = current_line.split(":")[-1].strip()
            regex_dict[syntax_type] = regex

    return regex_dict

def get_color_dict(theme_filename):
    color_dict = dict()
    with open(theme_filename, "r") as theme_file:
        for line_num, current_line in enumerate(theme_file):
            color_code = current_line.split(":")[-1].strip()
            syntax_type = current_line.split(":")[0].strip()
            color_dict[syntax_type] = color_code

    return color_dict

def color_source(source_filename, regex_dict, color_dict):
    start_color = "\033[{}m"
    end_color = "\033[0m"

    with open(source_filename, "r") as source_file:
        source_code = source_file.read()

    for syntax_type, regex in regex_dict.items():
        repl = start_color.format(color_dict[syntax_type]) + r"\1" + end_color
        source_code = re.sub(r"(" + regex + r")", repl, source_code)

    print(source_code)

if (__name__ == "__main__"):
    syntax_fn, theme_fn, source_fn = handle_input(sys.argv[1:])
    regex_dict = get_regex_dict(syntax_fn)
    print(regex_dict)
    color_dict = get_color_dict(theme_fn)
    print(color_dict)
    color_source(source_fn, regex_dict, color_dict)
