""" this is from all imports should be originated """

import sys
import os

PACKAGE_PARENT = ".."
CURRENT_PATH = os.getcwd()
THIS_FILE_PATH = os.path.expanduser(__file__)
JOINED_PATHS = os.path.join(CURRENT_PATH, THIS_FILE_PATH)
THIS_FILE_REAL_PATH = os.path.realpath(JOINED_PATHS)
THIS_FILE_OS_PATH = os.path.dirname(THIS_FILE_REAL_PATH)
THIS_FILE_PARENT_PATH = os.path.join(THIS_FILE_OS_PATH, PACKAGE_PARENT)
sys.path.append(os.path.normpath(THIS_FILE_PARENT_PATH))

# pylint: disable=wrong-import-position,unused-import
import my_package
