from state import *

def run():
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

    candi_dihapus = slice_filter(get_candi(), lambda u,_:u[1]==usn_jin_dihapus)
    (candi_dihapus_size, candi_dihapus_array, _) = candi_dihapus
    for i in range (candi_dihapus_size):
        empty_candi_id(candi_dihapus_array[i][0])
    set_candi(slice_remove(get_candi(), lambda u,_:u[1]==usn_jin_dihapus))

    print("Jin telah berhasil dihapus dari alam gaib.")