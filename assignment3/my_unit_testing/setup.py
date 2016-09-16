"""Installation script (using distutils) for module my_unit_testing. Comment on usage:
- To install this module, run this setup.py (while having my_unit_testing in the same directory) with
	the following command: 'sudo python setup.py install'
- If you have several python versions installed use this command for the specific version you want to
    install the module for: 'sudo <path-to-python-interpreter> setup.py install
    This will (amongst others) copy the module to the lib/site-packages directory to that version,
    at least that is what it did for me.
Now the module my_unit_testing should be available from any directory even if my_unit_testing.py is not
in that directory.
"""
from distutils.core import setup

name = "my_unit_testing"
setup(name = name, version = "1.0", py_modules = [name], scripts = [name + ".py"])