from env import *
from util.csv import *
from custom_typing import *
from os.path import exists

META_LIST = [
    (
        3,
        "username;password;role"
    ),
    (
        5,
        "id;pembuat;pasir;batu;air"
    ),
    (
        3,
        "nama;deskripsi;jumlah"
    )
]

def read_data(path: str, target_meta: CSV_Meta, wrap: Callable[[Any], A]) -> Slice[A]:
    raw = open(path, "r").read()
    (parsed, meta) = csv_parser(raw)

    if meta != target_meta:
        show_error("Format file csv salah")
        exit()
    
    wrapped: Slice[A] = slice_map(parsed, lambda r, _: wrap(r))

    return wrapped

USER_PATH = f"{FOLDER}/user.csv"
CANDI_PATH = f"{FOLDER}/candi.csv"
BAHAN_PATH = f"{FOLDER}/bahan_bangunan.csv"

if not (exists(USER_PATH) and exists(CANDI_PATH) and exists(BAHAN_PATH)):
    show_error("Format folder tidak valid")
    exit()


USER_SLICE = read_data(USER_PATH, META_LIST[0], lambda r: User((r[0], r[1], r[2])))
CANDI_SLICE = read_data(CANDI_PATH, META_LIST[1], lambda r: Candi((int(r[0]), r[1], int(r[2]), int(r[3]), int(r[4]))))
BAHAN_SLICE = read_data(BAHAN_PATH, META_LIST[2], lambda r: Bahan((r[0], r[1], int(r[2]))))