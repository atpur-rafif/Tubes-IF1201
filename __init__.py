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
import command.logout
import command.hancurkancandi
import command.summonjin
import command.ubahjin
import command.undo

print("\nLoading...\nSelamat datang di program \"Manajerial Candi\"")
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
    elif cmd == 'kumpul':
        command.jinpengumpul.run()
    elif cmd == 'bangun':
        command.jinpembangun.run()
    elif cmd == 'logout':
        command.logout.run()
    elif cmd == 'hancurkancandi':
        command.hancurkancandi.run()
    elif cmd == "summonjin":
        command.summonjin.run()
    elif cmd == "ubahjin":
        command.ubahjin.run()
    elif cmd == "undo":
        command.undo.run()
    else:
        show_error(f"Command \"{cmd}\" tidak ditemukan")
    print("")