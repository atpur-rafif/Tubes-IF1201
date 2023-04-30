from env import *
from util.data import *
from state import *

def run() -> None:
    prompt = input_validator(
        f"Apakah Anda ingin menyimpan save file pada \"{Folder}\" (Y/N)? ",
        lambda v: f"Input \"{v}\" tidak valid",
        lambda v: v == "Y" or v == "N"
    )

    if prompt == "N":
        exit()

    write_data(Folder, (get_user(), get_candi(), get_bahan()))
    print("Data berhasil disimpan")

    exit()