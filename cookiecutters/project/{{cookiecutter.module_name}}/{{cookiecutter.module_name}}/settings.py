import os

import dynaconf  # noqa

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# HERE STARTS DYNACONF EXTENSION LOAD (Keep at the very bottom of settings.py)
# Read more at https://dynaconf.readthedocs.io/en/latest/guides/django.html
settings = dynaconf.DjangoDynaconf(__name__)  # noqa
# HERE ENDS DYNACONF EXTENSION LOAD (No more code below this line)
