from state import *
from env import *
from util.random import random_range

def run():
    user = get_logged_as()
    if user == None or user[2] != "jin_pembangun":
        show_error("Anda tidak memiliki akses ke command ini")
        return
    
    (_, data, _) = get_bahan()
    jumlah_pasir = data[0][2]
    jumlah_batu = data[1][2]
    jumlah_air = data[2][2]

    butuh_pasir = random_range(1, 5)
    butuh_batu = random_range(1, 5)
    butuh_air = random_range(1, 5)

    if (jumlah_pasir < butuh_pasir) or (jumlah_batu < butuh_batu) or (jumlah_air < butuh_air):
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun")
        return

    set_bahan(slice_update(get_bahan(), lambda b, _: Bahan((b[0], b[1], b[2] - butuh_pasir)) if b[0] == "pasir" else None))
    set_bahan(slice_update(get_bahan(), lambda b, _: Bahan((b[0], b[1], b[2] - butuh_batu)) if b[0] == "batu" else None))
    set_bahan(slice_update(get_bahan(), lambda b, _: Bahan((b[0], b[1], b[2] - butuh_air)) if b[0] == "air" else None))
    set_candi(slice_append(get_candi(), Candi((create_candi_id(), user[0], butuh_pasir, butuh_batu, butuh_air))))

    (jumlah_candi, _, _) = get_candi()
    perlu_bangun = CANDI_MAKS - jumlah_candi
    if perlu_bangun < 0:
        perlu_bangun = 0

    print("Candi berhasil dibangun.")
    print(f"Sisa candi yang perlu dibangun: {perlu_bangun}")