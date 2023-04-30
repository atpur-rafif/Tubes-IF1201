from state import *

def run() -> None:
    if get_role() != "roro_jonggrang":
        show_error("Anda tidak memiliki akses ke command ini")
        return
    
    candi = get_candi()
    jumlah_candi = slice_get_size(candi)
    print("Kukuruyuk... Kukuruyuk...")
    print(f"Jumlah candi : {jumlah_candi}")
    if (jumlah_candi < 100):
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
    else: #candi >= 100
        print("Yah, Bandung Bondowoso memenangkan permainan!")
    exit()
