from state import *
from random import randrange

def run():
    if get_role() != "bandung_bondowoso":
        show_error("Anda tidak memiliki akses ke command ini")
        return


    pembangun = slice_filter(get_user(), lambda u, _: u[2] == "jin_pembangun")
    pembangun_array = slice_get_array(pembangun)
    pembangun_size = slice_get_size(pembangun)

    if pembangun_size == 0:
        show_error("Anda tidak memiliki jin pembangun")
        return

    butuh_str = ""
    kurang_str = ""

    butuh_list = [0 for _ in range(BAHAN_SIZE)]
    butuh_matrix = [[0 for _ in range(BAHAN_SIZE)] for _ in range(pembangun_size)]

    for j in range(BAHAN_SIZE):
        s = 0
        for i in range(pembangun_size):
            r = randrange(1, 5)
            butuh_matrix[i][j] = r
            s += r
        butuh_list[j] = s

    kekurangan = False
    for i in range(BAHAN_SIZE):
        nama_bahan = BAHAN_LIST[i][0]
        bahan = slice_get_element(get_bahan(), lambda b, _: b[0] == nama_bahan)

        if bahan == None:
            continue

        butuh_str += ("dan " if i + 1 == BAHAN_SIZE else "") + f"{butuh_list[i]} {nama_bahan}" + (", " if i + 1 != BAHAN_SIZE else "")

        kurang = 0
        if bahan[2] < butuh_list[i]:
            kekurangan = True
            kurang = butuh_list[i] - bahan[2]

        kurang_str += ("dan " if i + 1 == BAHAN_SIZE else "") + f"{kurang} {nama_bahan}" + (", " if i + 1 != BAHAN_SIZE else "")
    
    if kekurangan:
        show_error("Tidak berhasil membangun")
        show_error(f"Kurang {kurang_str}")
        return

    for i in range(BAHAN_SIZE):
        nama_bahan = BAHAN_LIST[i][0]
        set_bahan(slice_update(get_bahan(), lambda b, _: Bahan((b[0], b[1], b[2] - butuh_list[i])) if b[0] == nama_bahan else None))

    for i in range(pembangun_size):
            set_candi(slice_append(get_candi(), Candi((create_candi_id(), pembangun_array[i][0], butuh_matrix[i][0], butuh_matrix[i][1], butuh_matrix[i][2]))))

    print(f"Mengerahkan {pembangun_size} jin")
    print(f"Berhasil membangun {pembangun_size} candi")