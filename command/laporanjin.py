from state import *

def run():
    if get_role() != "bandung_bondowoso":
        show_error("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
        return

    user = get_user()
    candi = get_candi()
    bahan = get_bahan()

    pembangun_size = slice_count(user, lambda u, _: u[2] == "jin_pembangun")
    pengumpul_size = slice_count(user, lambda u, _: u[2] == "jin_pengumpul")
    (jin_size, jin_array, _) = slice_filter(user, lambda u, _: u[2] == "jin_pembangun" or u[2] == "jin_pengumpul")

    print(f"\n> Total Jin: {pengumpul_size + pembangun_size}")
    print(f"> Total Jin Pengumpul: {pengumpul_size}")
    print(f"> Total Jin Pembangun: {pembangun_size}")
    
    min_candi = ('-', -1)
    max_candi = ('-', -1)
    # (nama jin (string), jumlah candi yang dibangun (integer))

    candi = get_candi()
    for i in range(jin_size):
        bangun_candi = slice_count(candi, lambda u, _: u[1] == jin_array[i][0])
        jin = jin_array[i]

        if (min_candi[1] == -1 and jin[2] == "jin_pembangun") or (bangun_candi < min_candi[1]) or (bangun_candi == min_candi[1] and jin[0] < min_candi[0]):
            min_candi = (jin[0], bangun_candi)
        if (bangun_candi > max_candi[1]) or (bangun_candi == max_candi[1] and jin[0] < max_candi[0]):
            max_candi = (jin[0], bangun_candi)

    print(f"> Jin Terajin: {max_candi[0]}")
    print(f"> Jin Termalas: {min_candi[0]}")

    print(f"> Jumlah Pasir: {bahan[1][0][2]} unit")
    print(f"> Jumlah Air: {bahan[1][2][2]} unit")
    print(f"> Jumlah Batu: {bahan[1][1][2]} unit")