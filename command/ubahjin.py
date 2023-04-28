from state import *

def run():
    if get_role() != "bandung_bondowoso":
        show_error("Anda tidak memiliki akses ke command ini")
        return
    
    username = input("Masukkan username jin: ")
    user = slice_get_element(get_user(), lambda u, _: u[0] == username and (u[2] == "jin_pembangun" or u[2] == "jin_pengumpul"))

    if user == None:
        show_error("Tidak ada jin dengan username tersebut.")
        return

    ke = "jin_pembangun" if user[2] == "jin_pengumpul" else "jin_pengumpul"

    dari_text = "Jin Pengumpul" if user[2] == "jin_pengumpul" else "Jin Pembangun"
    ke_text = "Jin Pembangun" if user[2] == "jin_pengumpul" else "Jin Pengumpul"

    prompt = input_validator(
        f"Apakah anda yakin ingin mengubah jin \"{username}\" dari {dari_text} ke {ke_text} (Y/N)? ",
        lambda v: f"Input \"{v}\" tidak valid",
        lambda v: v == "Y" or v == "N"
    )

    if prompt == "N":
        print("Jin dibatalkan untuk diubah")
        return

    set_user(slice_update_target(get_user(), user, User((user[0], user[1], ke))))
    print("Jin berhasil diubah")