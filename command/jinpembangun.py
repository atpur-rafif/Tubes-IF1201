from state import *
from env import *
from util.random import random_range

def run():
    user = get_logged_as()
    if user == None or user[2] != "jin_pembangun":
        show_error("Anda tidak memiliki akses ke command ini")
        return
    
    bahan = get_bahan()
    pasir = slice_get_element(bahan, lambda b, _: b[0] == "pasir")
    batu = slice_get_element(bahan, lambda b, _: b[0] == "batu")
    air = slice_get_element(bahan, lambda b, _: b[0] == "air")

    if pasir == None or batu == None or air == None:
        show_error("Tidak ditemukan bahan tersebut")
        return

    jumlah_pasir = pasir[2]
    jumlah_batu = batu[2]
    jumlah_air = air[2]

    butuh_pasir = random_range(1, 5)
    butuh_batu = random_range(1, 5)
    butuh_air = random_range(1, 5)

    if (jumlah_pasir < butuh_pasir) or (jumlah_batu < butuh_batu) or (jumlah_air < butuh_air):
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun")
        return
    
    set_bahan(slice_update_target(get_bahan(), pasir, Bahan((pasir[0], pasir[1], pasir[2] - butuh_pasir))))
    set_bahan(slice_update_target(get_bahan(), batu, Bahan((batu[0], batu[1], batu[2] - butuh_batu))))
    set_bahan(slice_update_target(get_bahan(), air, Bahan((air[0], air[1], air[2] - butuh_air))))
    set_candi(slice_append(get_candi(), Candi((create_candi_id(), user[0], butuh_pasir, butuh_batu, butuh_air))))

    (jumlah_candi, _, _) = get_candi()
    perlu_bangun = CANDI_MAKS - jumlah_candi
    if perlu_bangun < 0:
        perlu_bangun = 0

    print("Candi berhasil dibangun.")
    print(f"Sisa candi yang perlu dibangun: {perlu_bangun}")