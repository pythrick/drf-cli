import re
import sys


def validate_module_name():
    module_name = '{{ cookiecutter.module_name }}'

    if not re.match(r'^[a-z][_a-z0-9]+$', module_name):
        print('ERROR: %s is not a valid Python module name!' % module_name)

        # exits with status 1 to indicate failure
        sys.exit(1)


def validate_class_name():
    class_name = '{{ cookiecutter.class_name }}'

    if not re.match(r'^[A-Z][a-zA-Z]+$', class_name):
        print('ERROR: %s is not a valid Python class name!' % class_name)

        # exits with status 1 to indicate failure
        sys.exit(1)


if __name__ == '__main__':
    validate_module_name()
    validate_class_name()
