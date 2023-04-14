from env import *
import command.exit
import command.login
import command.save
import command.batchbangun
import command.batchkumpul
import command.hapusjin
import command.help

while True:
    cmd = input(">>> ")

    if cmd == "exit":
        command.exit.run()
    elif cmd == 'login':
        command.login.run()
    elif cmd == 'save':
        command.save.run()
    elif cmd == "batchbangun":
        command.batchbangun.run()
    elif cmd == 'batchkumpul':
        command.batchkumpul.run()
    elif cmd == 'hapusjin':
        command.hapusjin.run()
    elif cmd == 'help':
        command.help.run()
    else:
        show_error(f"Command \"{cmd}\" tidak ditemukan")