from state import *
from util.random import create_random_range

def run():
    if get_role() != "bandung_bondowoso":
        show_error("Anda tidak memiliki akses ke command ini")
        return

    pengumpul_size = slice_count(get_user(), lambda u, _: u[2] == "jin_pengumpul")

    if pengumpul_size == 0:
        show_error("Anda tidak memiliki jin pengumpul")
        return

    def gen():
        s = 0
        g = create_random_range(0, 5)
        for _ in range(pengumpul_size):
            s += g()
        return s

    bahan_dapat = [gen() for _ in range(BAHAN_SIZE)]
    bahan_str = ""

    for i in range(BAHAN_SIZE):
        nama_bahan = BAHAN_LIST[i][0]
        set_bahan(slice_update(get_bahan(), lambda b, _: Bahan((b[0], b[1], b[2] + bahan_dapat[i])) if b[0] == nama_bahan else None))
        bahan_str += ("dan " if i + 1 == BAHAN_SIZE else "") + f"{bahan_dapat[i]} {nama_bahan}" + (", " if i + 1 != BAHAN_SIZE else "")

    print(f"Mengerahkan {pengumpul_size} jin")
    print(f"Menemukan {bahan_str}")