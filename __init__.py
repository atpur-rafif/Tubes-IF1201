from env import *
import command.exit
import command.login
import command.save
import command.batchbangun
import command.batchkumpul
import command.hapusjin
import command.help
import command.laporanjin
import command.laporancandi
import command.ayamberkokok
import command.jinpengumpul
import command.jinpembangun

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
    elif cmd == 'laporanjin':
        command.laporanjin.run()
    elif cmd == 'laporancandi':
        command.laporancandi.run()
    elif cmd == 'ayamberkokok':
        command.ayamberkokok.run()
    elif cmd == 'jinpengumpul':
        command.jinpengumpul.run()
    elif cmd == 'jinpembangun':
        command.jinpembangun.run()
    else:
        show_error(f"Command \"{cmd}\" tidak ditemukan")