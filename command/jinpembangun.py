from state import *
from random import randrange
import util.data

def run():
    if get_role() != "jin_pembangun":
        show_error("Anda tidak memiliki akses ke command ini")
        return
    
    data = read_data("data")[2][1]
    jumlah_pasir = data[0][2]
    jumlah_batu = data[1][2]
    jumlah_air = data[2][2]

    butuh_pasir = randrange (1,5)
    butuh_batu = randrange (1,5)
    butuh_air = randrange (1,5)
    candi = 0
    candi_perlu = 100

    while (jumlah_pasir > 0) and (jumlah_batu > 0) and (jumlah_air > 0): 
        if (jumlah_pasir >= butuh_pasir) and (jumlah_batu >= butuh_batu) and (jumlah_air >= butuh_air):
            candi += 1
            jumlah_pasir -= butuh_pasir
            jumlah_batu -= butuh_batu
            jumlah_air -= butuh_air

            if (candi >= 100):
                candi_perlu = 0
            else: 
                candi_perlu -= 1
            print("Candi berhasil dibangun.")
            print(f"Sisa candi yang perlu dibangun: {candi_perlu}")
        else: 
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun")
            break
     
    set_bahan(slice_update(get_bahan(), lambda b, _: Bahan((b[0], b[1], b[2] - jumlah_pasir)) if b[0] == "pasir" else None))
    set_bahan(slice_update(get_bahan(), lambda b, _: Bahan((b[0], b[1], b[2] - jumlah_batu)) if b[0] == "batu" else None))
    set_bahan(slice_update(get_bahan(), lambda b, _: Bahan((b[0], b[1], b[2] - jumlah_air)) if b[0] == "air" else None))