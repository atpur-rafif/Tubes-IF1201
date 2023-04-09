from env import *
import command.exit
import command.login

while True:
    cmd = input(">>> ")

    if cmd == "exit":
        command.exit.run()
    elif cmd == 'login':
        command.login.run()
    else:
        show_error(f"Command \"{cmd}\" tidak ditemukan")