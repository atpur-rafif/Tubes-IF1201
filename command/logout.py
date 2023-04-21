from state import *

def run():
    if get_role() == None:
        show_error("Logout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan\nlogout")
        return
    
    set_logged_as(None)
    print("Anda telah logout")
    return