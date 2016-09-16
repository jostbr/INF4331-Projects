
import sys

def file_statistics(list_of_filenames):
    """Function that counts the number of lines, words, and characters in all files in list. The
    function uses the with keyword and a for-loop with the iterator enumerate() to make it memory
    efficient and avoid storing the entire file simultaneously, but rather only a line at a time.

    Args:
        list_of_filenames (list[str]): List with files to get statistics on.
    """
    if (len(list_of_filenames) >= 1):
        num_lines_total = 0     # To store number of lines in all files combined
        num_words_total = 0     # To store number of words in all files combined
        num_chars_total = 0     # To store number of chars in all files combined

        for filename in list_of_filenames:
            num_words_in_file = 0       # To store number of words in current file
            num_chars_in_file = 0       # To store number of characters in current file

            with open(filename, "r") as current_file:
                for line_num, current_line in enumerate(current_file):
                    num_words_in_file += len(current_line.split())      # Add num words in current_line
                    num_chars_in_file += len(current_line)              # Add num chars in current_line

            num_lines_in_file = line_num    # The iterator starts ends at the number of new-line chars
            print("{:9} {:9} {:9}       {}".format(num_lines_in_file, num_words_in_file, num_chars_in_file, filename))

            num_lines_total += num_lines_in_file    # Add to total line count
            num_words_total += num_words_in_file    # Add to total word count
            num_chars_total += num_chars_in_file    # Add to total char count

        # Only print "total"-line if more than one file is passed in.
        if (len(list_of_filenames) > 1):
            print("{:9} {:9} {:9}       Total".format(num_lines_total, num_words_total, num_chars_total))

    else:
        print("Error: Provide a minumum of one argument (filename)")
        sys.exit()  # Exit program if user doesn't specify at least one file


if (__name__ == "__main__"):
    # The use of sys.argv below is based on the assumption that bash expands
    # the wildcard notation asked for in the exercise, namely * and *.py.
    # Here bash fills sys.argv with all the requested files in the directory.
    file_statistics(sys.argv[1:])   # Pass in the list of specified filenames
