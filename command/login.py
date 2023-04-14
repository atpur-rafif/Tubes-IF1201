from state import *
from util.slice import *

def run():
    logged_as = get_logged_as()
    if logged_as != None:
        show_error(f'Login gagal!\nAnda telah login dengan username {logged_as[0]}, silahkan lakukan "logout"\nsebelum melakukan login kembali ')
        return
    username = input('Username: ')
    user = slice_get_element(get_user(), lambda u,_:u[0]==username)
    password = input('Password: ')
    if user == None:
        show_error("Username tidak terdaftar!")
        return
    if user[1] != password:
        show_error('Password salah!')
        return
    set_logged_as(user)
    print(f'Selamat datang, {username}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.')