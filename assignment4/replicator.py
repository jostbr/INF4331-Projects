# This is a program which self replicates.
# When run it will print its own source code.
ASCII = [chr(i) for i in range(128)]    # String array of ASCII chars
quote = ASCII[34]   # String with double quotation mark
comma = ASCII[44]   # String with comma sign
list_of_lines = [   # List with the source code lines
"# This is a program which self replicates.",
"# When run it will print its own source code.",
"ASCII = [chr(i) for i in range(128)]    # String array of ASCII chars",
"quote = ASCII[34]   # String with double quotation mark",
"comma = ASCII[44]   # String with comma sign",
"list_of_lines = [   # List with the source code lines",
"",
"]",
"for current_line in list_of_lines[:6]:",
"    print(current_line)                 # Print lines down to 'list_of_lines'",
"for current_line in list_of_lines:",
"    print(quote + current_line + quote + comma) # Print list of source code",
"for current_line in list_of_lines[7:]",
"    print(current_line)                 # Print these three for-loops"
]
for current_line in list_of_lines[:6]:
    print(current_line)                 # Print lines down to 'list_of_lines'
for current_line in list_of_lines:
    print(quote + current_line + quote + comma) # Print list of source code
for current_line in list_of_lines[7:]:
    print(current_line)                 # Print these three for-loops