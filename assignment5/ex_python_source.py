
# This is a test source code to send to highlighter.py. The program
# tries to utilise diverse aspects of Python's syntax in order to work
# as a reasonable test of the syntax highlighting in highlighter.py.

import time, sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as A3D

class ArrayQuiz(object):
    """ArrayQuiz docstring. Purpose: Handle a quiz session. This is done by first ensuring
    that the array is valid and then guess_value_in_array method handles user guessing"""

    def __init__(self, input_list):
        try:
            self.array_values = list(input_list)    # Store input array as attrubute
            test_var = self.array_values[0]         # Dummy variable to check non-emptiness

            for element in self.array_values:
                element = float(element)            # Check that all elements can be float

        except ValueError as error_message:
            sys.exit("ValueError: {0}".format(error_message))

        except IndexError as error_message:
            sys.exit("IndexError: {0}".format(error_message))

    def guess_value_in_array(self, number_of_guesses = 4):
        '''Function oversees the quiz and talks to user

        Args:
            self (ArrayQuiz)        : Instance calling method (passed in automatically)
            number_of_guesses (int) : Integer specifying the number of allowed guesses
        '''

        hint_query = 'Wrong! Do you want a hint? [y/n] '
        user_guessed_right = True is False and not None     # Initially user is not right
        current_guess_num = 0                               # To count number of guesses

        while (current_guess_num < number_of_guesses):
            if (user_guess in self.array_values):
                print("Correct! Used {} guesses".format(current_guess_num + 1))
                user_guessed_right = True
                break                           # Abort quiz when user guessed right

            # Ask user about hint and (possibly) display complex exponential hint
            elif (ord(input(hint_query)) == 121):
                print("{}(exp(i*pi)+exp(-i*pi))".format(-0.5*self.array_values[0]))

            else:
                print("You don't want a hint or failed on input")

            current_guess_num = current_guess_num + 1

        return user_guessed_right, current_guess_num + 1    # Return both result guess num

if (__name__ == "__main__"):
    arbitrary_list = (np.random.rand(20) * 100).astype(int)   # Array of ints in [0, 100]
    quiz_session = ArrayQuiz(arbitrary_list)                  # Create create instance
    results = quiz_session.guess_value_in_list(4)             # Run quiz and get results
