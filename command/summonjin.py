from state import *

def run() -> None:
    if get_role() != "bandung_bondowoso":
        show_error("Anda tidak memiliki akses ke command ini")
        return

    banyak_jin = slice_count(get_user(), lambda v, _: v[2] == "jin_pembangun" or v[2] == "jin_pengumpul")
    if banyak_jin >= JIN_MAKS:
        show_error("Jin terlalu banyak")
        return
    
    jenis = input_validator(
        "Jenis jin yang dapat dipanggil:\n(1) Pengumpul - Bertugas mengumpulkan bahan bangunan\n(2) Pembangun - Bertugas membangun candi\nMasukkan nomor jenis jin yang ingin diambil: ",
        lambda v: f"Tidak ada jenis jin bernomor \"{v}\"",
        lambda v: v == '1' or v == '2'
    )

    jenis_text = "Pengumpul" if jenis == "1" else "Pembangun"
    print(f"Memilih jin \"{jenis_text}\".")

    username = input_validator(
        "Masukan username: ",
        lambda v: f"Username \"{v}\" sudah diambil",
        lambda v: slice_get_element(get_user(), lambda u, _: u[0] == v) == None
    )

    password = input_validator(
        "Masukkan password: ",
        lambda _: "Password panjangnya harus 5-25 karakter!",
        lambda v: 5 <= str_len(v) and str_len(v) <= 25
    )

    set_user(slice_append(get_user(), User((username, password, "jin_pengumpul" if jenis == '1' else "jin_pembangun"))))
    print("Mengumpulkan sesajen...\nMenyerahkan sesajen...\nMembacakan mantra...")
    print(f"Jin {username} berhasil dipanggil!")


