from util.data import *
from state import *

def run():
    if not (get_role() == "bandung_bondowoso" or get_role() == "roro_jonggrang"):
        show_error("Anda tidak memiliki akses ke command ini")
        return


    path = input("Masukkan folder: ")

    prompt = input_validator(
        f"Apakah anda yakin ingin save pada {path} (Y/N)? ",
        lambda v: f"Input \"{v}\" tidak valid",
        lambda v: v == "Y" or v == "N"
    )

    if prompt == "N":
        print("Save dibatalkan")
        return

    print("Saving...")
    write_data(path, (get_user(), get_candi(), get_bahan()))
    print("Data berhasil di save")