from util.data import *
from state import *

def run():
    path = input("Masukkan folder: ")
    print("Saving...")
    write_data(path, (get_user(), get_candi(), get_bahan()))
    print("Data berhasil di save")