
import sys
import math

class ReversedPolishNotationCalc:
	def __init__(self):
		self.internal_stack = []
		self.operator_int_OK = ["+", "-", "*"]
		self.operator_float_req = ["/", "v", "sin", "cos"]
		self.allowed_exit_cmds = ["exit", "exit()", "quit", "end"]	# Acceptable cmds for exiting session

	def process_user_input(self, input_list):
		for input_element in input_list:
			if (object_is_type_int(input_element) == True):
				self.add_to_stack(int(input_element))
				#print("Added int to stack!")

			elif (object_is_type_float(input_element) == True):
				self.add_to_stack(float(input_element))
				#print("Added float to stack!")

			else:
				if (input_element in (self.operator_int_OK + self.operator_float_req)):
					print("Legal operator!")
					self.apply_operator_on_stack(input_element)

				elif (input_element == "p"):
					print(self.internal_stack[-1])

				else:
					if (input_element not in self.allowed_exit_cmds):
						print("Error, invalid input: '{0}'".format(input_element))

						# If user enter multiple inputs on single line, the program will remember
						# input to the left of the invalid input, but ignores input to the right.
						if (len(input_list) > 1):
							print("Kept input to the left of '{0}', but aborted parsing of input at '{0}'".format(input_element))
						
						break

	def apply_operator_on_stack(self, operator):
		if (operator in self.operator_int_OK):
			result = eval(str(self.internal_stack[-2]) + operator + str(self.internal_stack[-1]))

			self.remove_from_stack(2)
			self.add_to_stack(result)

		elif (operator in self.operator_float_req):
			self.internal_stack[-2] = float(self.internal_stack[-2])	# To avoid int-div and errors using math module
			self.internal_stack[-1] = float(self.internal_stack[-1])	# To avoid int-div and errors using math module

			if (operator == "/"):
				result = self.internal_stack[-2] / self.internal_stack[-1]
			elif (operator == "v"):
				result = math.sqrt(self.internal_stack[-1])
			elif (operator == "sin"):
				result = math.sin(self.internal_stack[-1])
			elif (operator == "cos"):
				result = math.cos(self.internal_stack[-1])

			self.remove_from_stack(1)
			self.add_to_stack(result)

	
	def add_to_stack(self, value_to_be_added):
		self.internal_stack.append(value_to_be_added)
		#print(self.internal_stack)

	def remove_from_stack(self, num_elements):
		for i in range(-num_elements, 0):
			del self.internal_stack[i]



def object_is_type_int(test_object):
	try:
		temp_var_01 = float(test_object)
		temp_var_02 = int(temp_var_01)

	except ValueError:
		return False

	else:
		return temp_var_01 == temp_var_02

def object_is_type_float(test_object):
	try:
		temp_var = float(test_object)

	except ValueError:
		return False

	else:
		return True


if (__name__ == "__main__"):
	calc_session = ReversedPolishNotationCalc()				# Creating instance of class for this session	
	input_list = []											# List to hold input arguments from user


	while (not any(x in input_list for x in calc_session.allowed_exit_cmds)):
		input_list = input("> ").split()					# User gives in argument(s) to calc session
		calc_session.process_user_input(input_list)			# Processing input when user submits argument(s)