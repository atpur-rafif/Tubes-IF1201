from state import *
def run():
    if get_role() == None:
        print("=========== HELP ===========")
        print(f"1. login\n   Untuk masuk akun")
        print(f'2. exit\n   Untuk keluar program')
    elif get_role() == "bandung_bondowoso":
        print("=========== HELP ===========")
        print(f'1. logout\n   Untuk keluar dari akun yang digunakan sekarang')
        print(f'2. summonjin\n   Untuk memanggil jin')
        print(f'3. hapusjin\n   Untuk menghapus jin dengan username yang diinput')
        print(f'4. ubahjin \n   Untuk mengubah tipe jin dengan menginput username jin yang ingin diubah\n   tipe jin yang tersedia adalah jin pengumpul atau jin pembangun')
        print(f'5. batchkumpul\n   Untuk memerintahkan jin tipe pengumpul mengumpulkan bahan\n   tidak bisa digunakan untuk jin tipe pembangun')
        print(f'6. batchbangun\n   Untuk memerintahlan jin tipe pembangun akan membangun candi\n   tidak bisa digunakan untuk jin tipe pengumpul')
        print(f'7. laporanjin \n   Untuk mengetahui data statistik tentang kinerja para jin\n   data terdiri dari jumlah total jin pengumpul dan pembagun, jin terajin, jin termalas, dan jumlah bahan yang terkumpul ')
        print(f'8. laporancandi\n   Untuk mengetahui progres pembagunan candi\n   mulai dari total candi, total masing-masing bahan yang digunakan, ID candi termahal, dan ID candi termurah')
        print(f'9. save\n   untuk menjalankan prosedur penyimpanan data sesuai dengan struktur data external')
    elif get_role() == "roro_jonggrang":
        print("=========== HELP ===========")
        print(f'1. logout\n   Untuk keluar dari akun yang digunakan sekarang')
        print(f'2. hancurkancandi\n   Untuk menghancurkan candi yang tersedia')
        print(f'3. ayamberkokok\n   Untuk menyelesaikan permainan dengan memalsukan pagi hari ')
        print(f'4. save\n   untuk menjalankan prosedur penyimpanan data sesuai dengan struktur data external')
    elif get_role() == 'jin_pembangun':
        print("=========== HELP ===========")
        print(f'1. logout\n   Untuk keluar dari akun yang digunakan sekarang')
        print(f'2. bangun\n  Untuk membangun candi dengan bahan-bahan yang tersedia\n  jika bahan tidak mencukupi maka tidak dapat membangun')
        print(f'3. save\n   untuk menjalankan prosedur penyimpanan data sesuai dengan struktur data external')
    elif get_role() == 'jin_pengumpul':
        print("=========== HELP ===========")
        print(f'1. logout\n   Untuk keluar dari akun yang digunakan sekarang')
        print(f'2. kumpul\n   Untuk mengumpulkan bahan-bahan yang diperlukan untuk membangun candi secara random')
        print(f'3. save\n   untuk menjalankan prosedur penyimpanan data sesuai dengan struktur data external')