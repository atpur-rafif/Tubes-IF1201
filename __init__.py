from env import *
import command.exit
import command.login
import command.save

while True:
    cmd = input(">>> ")

    if cmd == "exit":
        command.exit.run()
    elif cmd == 'login':
        command.login.run()
    elif cmd == 'save':
        command.save.run()
    else:
        show_error(f"Command \"{cmd}\" tidak ditemukan")