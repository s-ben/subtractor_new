#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "subtractor.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


    # SECRET_KEY = 'v5i%t-2)!&uateyb7jzml%k8@fgo4fxgb#2@1!7gmce40%yc@&'

