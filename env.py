from util import *
from os.path import exists

import argparse
arg_parse = argparse.ArgumentParser()
arg_parse.add_argument("folder", nargs="?")
arg_parsed = arg_parse.parse_args()
FOLDER = arg_parsed.folder

if FOLDER == None:
    error_exit("Folder tidak diberikan")
elif not exists(FOLDER):
    error_exit("Folter tidak ditemukan")
