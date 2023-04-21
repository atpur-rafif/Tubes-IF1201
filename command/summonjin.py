from state import *

def run():
    if get_role() != "bandung_bondowoso":
        show_error("Anda tidak memiliki akses ke command ini")
        return

    banyak_jin = slice_get_size(get_user())
    if banyak_jin >= 100:
        show_error("Jin terlalu banyak")
        return
    
    jenis = input_validator(
        "(1) Pengumpul\n(2) Pembangun\nJenis jin: ",
        lambda v: f"Input \"{v}\" tidak valid",
        lambda v: v == '1' or v == '2'
    )

    username = input_validator(
        "Masukan username: ",
        lambda v: f"Username \"{v}\" sudah digunakan",
        lambda v: slice_get_element(get_user(), lambda u, _: u[0] == v) == None
    )

    password = input_validator(
        "Masukkan password: ",
        lambda v: f"",
        lambda v: 5 <= str_len(v) and str_len(v) <= 25
    )

    set_user(slice_append(get_user(), User((username, password, "jin_pengumpul" if jenis == '1' else "jin_pembangun"))))
    print("Jin berhasil disummon")


