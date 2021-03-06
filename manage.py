#!/usr/bin/env python
import dotenv
import os
import sys
import configurations

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_CONFIGURATION', 'Development')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    from configurations.management import execute_from_command_line
    execute_from_command_line(sys.argv)
