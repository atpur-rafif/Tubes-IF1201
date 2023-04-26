from util.program import *
from os.path import exists

import argparse
arg_parse = argparse.ArgumentParser()
arg_parse.add_argument("folder", nargs="?")
arg_parsed = arg_parse.parse_args()
Folder = arg_parsed.folder

if Folder != None and not exists(Folder):
    error_exit("Folter tidak ditemukan, kosongkan parameter apabila ingin membuat save baru")

CANDI_MAKS = 100
JIN_MAKS = 100