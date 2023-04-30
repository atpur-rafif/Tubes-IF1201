from util.data import *
from state import *
from os import listdir

def run() -> None:
    path = input("Masukkan folder: ")

    prompt = input_validator(
        f"Apakah anda yakin ingin save pada {path} (Y/N)? ",
        lambda v: f"Input \"{v}\" tidak valid",
        lambda v: v == "Y" or v == "N"
    )

    if prompt == "N":
        print("Save dibatalkan")
        return

    if exists(path) and listdir(path) != []:
        prompt = input_validator(
            f"Sudah terdapat file/folder pada {path}, tetap lakukan save?",
            lambda v: f"Input \"{v}\" tidak valid",
            lambda v: v == "Y" or v == "N"
        )

        if prompt == "N":
            print("Save dibatalkan")
            return

    print("Saving...")
    write_data(path, (get_user(), get_candi(), get_bahan()))
    print("Data berhasil di save")