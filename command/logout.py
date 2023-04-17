from state import *

def run():
    if get_role() == None:
        show_error("Anda belum login")
        return
    
    set_logged_as(None)
    print("Anda telah logout")
    return