
class UnitTest(object):
    """Class that executes testing of a function func which takes arguments
    *args, keyword arguments **kwargs and has the expected result res when
    run. See __call_ docstring for more details on how the testung is done.

    Methods in class:
        __init__: Constructor that stores the input arguments (from instance creation)
        __call__: Call method that tests if a function gives its expected results
    """
    def __init__(self, func, args, kwargs, res):
        """Constructor that stores input arguments as attributes for the
        instance being created and makes them available to __call__.

        Args:
            func (function): Function to be tested that takes arguments *args, and **kwargs.
            args (list): List of positional arguments for the function func.
                kwargs (dict): Dictionary of keyword arguments that func take as input.
            res (ANY): A result (arbitrary type) that func is expected to produce given
                the arguments *args and **kwargs.
        """
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.res = res

    def __call__(self):
        """Call function (run when instance is called) that executes test; it tries to call func
        with the arguments provided in *self.args and **self.kwargs and produce the exected result
        self.res. If the expected result is produced successfuly, the function returns True, and
        if an exception is thrown (using Exception (almost top of exception hierarchy) to handle
        all types of errors) the function returns False and we know this particular test failed."""
        try:
            self.func(*self.args, **self.kwargs) == self.res

        except Exception:
            return False
        
        else:
            return True


