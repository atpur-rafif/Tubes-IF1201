from state import *

def run():
    if get_role() != "bandung_bondowoso":
        show_error("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
        return

    user = get_user()
    pembangun_size = slice_count(user, lambda u, _: u[2] == "jin_pembangun")
    pengumpul_size = slice_count(user, lambda u, _: u[2] == "jin_pengumpul")
    jin_array = slice_get_array(slice_filter(user, lambda u, _: u[2] == "jin_pembangun" or u[2] == "jin_pengumpul"))
    jin_size = pembangun_size + pengumpul_size

    print(f"\n> Total Jin: {pengumpul_size + pembangun_size}")
    print(f"> Total Jin Pengumpul: {pengumpul_size}")
    print(f"> Total Jin Pembangun: {pembangun_size}")
    
    if jin_size == 0:
        jin_array = [['-']]
    
    min_candi = ('-', 106)
    max_candi = (jin_array[0][0], 0)
    # (nama jin (string), jumlah candi yang dibangun (integer))

    candi = get_candi()
    for i in range(jin_size):
        bangun_candi = slice_count(candi, lambda u, _: u[1] == jin_array[i][0])
        if (((bangun_candi < min_candi[1]) or (bangun_candi == min_candi[1] and jin_array[i][0] > min_candi[0])) and jin_array[i][2] == "jin_pembangun"):
            min_candi = (jin_array[i][0], bangun_candi)
        if (bangun_candi > max_candi[1]) or (bangun_candi == max_candi[1] and jin_array[i][0] < max_candi[0]):
            max_candi = (jin_array[i][0], bangun_candi)

    print(f"> Jin Terajin: {max_candi[0]}")
    print(f"> Jin Termalas: {min_candi[0]}")

    print(f"> Jumlah Pasir: {get_bahan()[1][0][2]} unit")
    print(f"> Jumlah Air: {get_bahan()[1][2][2]} unit")
    print(f"> Jumlah Batu: {get_bahan()[1][1][2]} unit")
    