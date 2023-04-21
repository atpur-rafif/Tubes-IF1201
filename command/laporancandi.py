from state import *

def run():
    if get_role() != "bandung_bondowoso":
        show_error("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.")
        return

    candi = get_candi()
    candi_array = slice_get_array(candi)
    candi_size = slice_get_size(candi)
    print(f"\n> Total Candi: {candi[0]}")

    if candi_size == 0:
        candi_array = [[-1]] # id candi selalu > -1

    min_cost = (candi_array[0][0], 0)
    max_cost = (candi_array[0][0], 0)
    # (ID candi (integer), biaya yang dihabiskan (integer))

    bahan_digunakan = (0, 0, 0)

    for i in range(candi_size):
        cost = 10000 * candi_array[i][2] + 15000 * candi_array[i][3] + 7500 * candi_array[i][4]
        if min_cost[1] == 0 or cost < min_cost[1]:
            min_cost = (candi_array[i][0], cost)
        if min_cost[1] == 0 or cost > max_cost[1]:
            max_cost = (candi_array[i][0], cost)
        bahan_digunakan = (bahan_digunakan[0] + candi_array[i][2], bahan_digunakan[1] + candi_array[i][3], bahan_digunakan[2] + candi_array[i][4])
        # jika terdapat 2 atau lebih candi termahal atau termurah, output mengeluarkan candi yang terlebih dahulu dibangun

    print(f"> Total Pasir yang digunakan: {bahan_digunakan[0]}")
    print(f"> Total Batu yang digunakan: {bahan_digunakan[1]}")
    print(f"> Total Air yang digunakan: {bahan_digunakan[2]}")
    print(f"> ID Candi Termahal: {'-' if max_cost[0] == -1 else f'{max_cost[0]} (Rp ' + '{:,}'.format(max_cost[1]).replace(',', '.') + ')'}")
    print(f"> ID Candi Termurah: {'-' if min_cost[0] == -1 else f'{min_cost[0]} (Rp ' + '{:,}'.format(min_cost[1]).replace(',', '.') + ')'}")