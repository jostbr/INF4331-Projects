
import sys
import math

class ReversedPolishNotationCalc:
	def __init__(self, command_line_input = None):
		self.internal_stack = []									# Internal stack to hold user input
		self.operator_int_OK = ["+", "-", "*"]						# Operators where ints are okey.
		self.operator_float_req = ["/", "v", "sin", "cos"]			# Operators where numbers need be float
		self.allowed_exit_cmds = ["exit", "exit()", "quit", "end"]	# Acceptable cmds for exiting session
		self.user_requests_exit = False								# Set to True when user enters exit-cmd

		# If program is run with cmd line argument.
		if (command_line_input is not None):
			self.process_user_input(command_line_input)		# Process command line argumen
			self.user_requests_exit = True					# Exit program after processing

	def process_user_input(self, input_list):

		# If none of the elements in the user input line is an exit command.
		if (not any(x in input_list for x in self.allowed_exit_cmds)):
			stack_pre_input_procs = list(self.internal_stack)	# Copy stack before procs input line in case of invalid input

			# Loop over all elements in user input line and process.
			for input_element in input_list:

				# If input_element is of type int (must be checked before float).
				if (object_is_type_int(input_element) == True):
					self.add_to_stack(int(input_element))

				# If input_element is of type float (must be checked after int).
				elif (object_is_type_float(input_element) == True):
					self.add_to_stack(float(input_element))

				# If input_element is a valid operator (defined by the exercise).
				elif (input_element in self.operator_int_OK or input_element == "/"):
					if (len(self.internal_stack) >= 2):
						self.apply_operator_on_stack(input_element)		# Execute operator on stack
					else:
						self.print_error_stack_length(input_element, 2)
						break

				elif (input_element in self.operator_float_req and input_element != "/"):
					if (len(self.internal_stack) >= 1):
						self.apply_operator_on_stack(input_element)		# Execute operator on stack
					else:
						self.print_error_stack_length(input_element, 1)
						break

				# If user wants to print last element in stack.
				elif (input_element == "p"):
					if (len(self.internal_stack) > 0):
						print(self.internal_stack[-1])

					else:
						self.print_error_stack_length(input_element, 0)
						break

				# If user input is not valid.
				else:
					self.internal_stack = list(stack_pre_input_procs)			# Resets stack to state before line with invalid user input
					print("Error; invalid input: '{0}'".format(input_element))	# Gives user message that the input is invalid
					break														# Then breaks loop and aborts parsing of user input line

				print(self.internal_stack)

		# If user has entered an exit command.
		else:
			self.user_requests_exit = True

	def apply_operator_on_stack(self, operator):
		# If the operator is of type that can handle ints.
		if (operator in self.operator_int_OK):
			result = eval(str(self.internal_stack[-2]) + operator + str(self.internal_stack[-1]))	# Execute operation using eval
			self.remove_from_stack(2)		# Remove the last two (involved in operation) elements from the stack
			self.add_to_stack(result)		# Add the result of the operation to the end of the stack.

		# If operator requires floats to function properly.
		elif (operator in self.operator_float_req):
			# If operator is "/"; this requires last two elements to be float.
			if (operator == "/"):
				self.internal_stack[-2] = float(self.internal_stack[-2])	# To avoid int-div and errors using math module
				self.internal_stack[-1] = float(self.internal_stack[-1])	# To avoid int-div and errors using math module

			# If any other operator in self.operator_float_req nonly the last element need sto be float.
			else:
				self.internal_stack[-1] = float(self.internal_stack[-1])	# To avoid int-div and errors using math module


			if (operator == "/"):
				result = self.internal_stack[-2] / self.internal_stack[-1]
				self.remove_from_stack(2)
				self.add_to_stack(result)

			elif (operator == "v"):
				self.internal_stack[-1] = math.sqrt(self.internal_stack[-1])

			elif (operator == "sin"):
				self.internal_stack[-1] = math.sin(self.internal_stack[-1])

			elif (operator == "cos"):
				self.internal_stack[-1] = math.cos(self.internal_stack[-1])
	
	def add_to_stack(self, value_to_be_added):
		self.internal_stack.append(value_to_be_added)		# Append value at end of stack

	def remove_from_stack(self, num_elements):
		# Making loop to make function useable after all operators.
		for i in range(-num_elements, 0):
			del self.internal_stack[i]

	def print_error_stack_length(self, operator, req_stack_length):
		print("Error; Not enough elements in stack to perform operation: '{0}'".format(operator))
		print("This operation requires stack length of at least {0}. Current stack length is: {1}".format(req_stack_length, len(self.internal_stack)))


def object_is_type_int(test_object):
	try:
		temp_var_01 = float(test_object)	# Try creating float from test_object
		temp_var_02 = int(temp_var_01)		# Try creating int from test_object

	except ValueError:
		return False	# False if "try" fails because of ValueError

	else:
		return temp_var_01 == temp_var_02	# True if test_pbject is int.

def object_is_type_float(test_object):
	try:
		temp_var = float(test_object)		# Try creating float from test_object

	except ValueError:
		return False	# False if "try" fails because of ValueError

	else:
		return True		# True if float conversion is successful


if (__name__ == "__main__"):
	if (len(sys.argv) == 1):
		calc_session = ReversedPolishNotationCalc()						# Creating instance without cmd line arg

	elif (len(sys.argv) == 2):
		calc_session = ReversedPolishNotationCalc(sys.argv[1].split())	# Creating instance with cmd line arg

	else:
		print("Error; Invalid number of cmd args (max 1 in addition to filename)")
		sys.exit()

	# Loop and ask for user input until user requests exit.
	while (not calc_session.user_requests_exit):
		input_list = input("> ").split()				# User gives in argument(s) to calc session
		calc_session.process_user_input(input_list)		# Processing input when user submits argument(s)