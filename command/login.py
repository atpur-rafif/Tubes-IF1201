from state import *
from util.slice import *

# TODO: Validasi apakah user sudah login apa belum    
def run():
    username = input('Username: ')
    user = slice_get_element(get_user(), lambda u,_:u[0]==username)
    if user == None:
        show_error("Username tidak terdaftar!")
        return
    password = input('Password: ')
    if user[1] != password:
        show_error('Password salah!')
        return
    set_logged_as(user)
    print(f'Selamat datang, {username}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.')

    