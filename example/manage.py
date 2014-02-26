#!/usr/bin/env python
import os
import sys

# As per http://stackoverflow.com/questions/3560225/django-not-finding-apps-in-virtualenv-when-using-manage-py-syncdb
activate_this = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", ".env", "bin", "activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
