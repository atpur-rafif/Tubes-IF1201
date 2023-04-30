from state import *

def run() -> None:
    if get_role() != "bandung_bondowoso":
        show_error("Anda tidak memiliki akses ke command ini")
        return

    usn_jin_dihapus = input("Masukkan username jin : ")
    jin_dihapus = slice_get_element(get_user(), lambda u,_:(u[0]==usn_jin_dihapus) and (u[2]=="jin_pengumpul" or u[2]=="jin_pembangun"))

    if jin_dihapus == None:
        show_error("Tidak ada jin dengan username tersebut.")
        return

    prompt = input_validator(
        f"Apakah anda yakin ingin menghapus jin dengan username {usn_jin_dihapus} (Y/N)? ",
        lambda v: f"Input \"{v}\" tidak valid",
        lambda v: v == "Y" or v == "N"
    )

    if prompt == "N":
        print("Jin batal dihapus")
        return
    
    print("Menghapus jin...")
    set_user(slice_remove(get_user(), lambda u,_:u[0]==usn_jin_dihapus))

    # (username jin dihapus, slice candi dihapus)
    S: Any = [usn_jin_dihapus, slice_create()]
    def filter_fn(c: Candi, _: Any):
        if S[0] == c[1]:
            S[1] = slice_append(S[1], c)
            empty_candi_id(c[0])
            return True
        return False
    set_candi(slice_remove(get_candi(), filter_fn))
    set_undo_stack(slice_append(get_undo_stack(), (jin_dihapus, S[1][0], S[1][1])))

    print("Jin telah berhasil dihapus dari alam gaib.")