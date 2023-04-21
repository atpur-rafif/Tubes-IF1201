from state import *
def run():
    if get_role() != 'roro_jonggrang':
        show_error('Anda tidak memiliki akses ke command ini')
        return
    id = int(input('Masukkan ID candi: '))
    candi = slice_get_element(get_candi(), lambda b, _: b[0] == id)
    if candi == None:
        show_error('Tidak ada candi dengan ID tersebut.')
        return
    prompt = input_validator(
        f"Apakah anda yakin ingin menghancurkan candi dengan id {id} (Y/N)? ",
        lambda v: f"Input \"{v}\" tidak valid",
        lambda v: v == "Y" or v == "N"
    )
    if prompt == "N":
        print("Candi batal dihapus.")
        return
    set_candi(slice_remove(get_candi(), lambda b,_: b[0] == id))
    empty_candi_id(id)
    print('Candi telah berhasil dihancurkan.')