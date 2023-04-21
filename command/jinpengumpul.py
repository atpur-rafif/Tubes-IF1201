from state import *
from util.random import create_random_range

def run():
    if get_role() != "jin_pengumpul":
        show_error("Anda tidak memiliki akses ke command ini")
        return

    gen = create_random_range(0, 5)
    jumlah_pasir = gen()
    jumlah_batu = gen()
    jumlah_air = gen()

    print (f"Jin menemukan {jumlah_pasir} pasir, {jumlah_batu} batu, dan {jumlah_air} air.")
    set_bahan(slice_update(get_bahan(), lambda b, _: Bahan((b[0], b[1], b[2] + jumlah_pasir)) if b[0] == "pasir" else None))
    set_bahan(slice_update(get_bahan(), lambda b, _: Bahan((b[0], b[1], b[2] + jumlah_batu)) if b[0] == "batu" else None))
    set_bahan(slice_update(get_bahan(), lambda b, _: Bahan((b[0], b[1], b[2] + jumlah_air)) if b[0] == "air" else None))
