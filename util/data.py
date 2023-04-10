from util.csv import *
from custom_typing import *
from os.path import exists
from os import makedirs

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

def read_data(path: str) -> tuple[Slice[User], Slice[Candi], Slice[Bahan]]:
    USER_PATH = f"{path}/user.csv"
    CANDI_PATH = f"{path}/candi.csv"
    BAHAN_PATH = f"{path}/bahan_bangunan.csv"

    if not (exists(USER_PATH) and exists(CANDI_PATH) and exists(BAHAN_PATH)):
        show_error("Format folder tidak valid")
        exit()
    
    def fn(path: str, target_meta: CSV_Meta, wrap: Callable[[Any], A]) -> Slice[A]:
        raw = open(path, "r").read()
        (parsed, meta) = csv_parser(raw)
        if meta != target_meta:
            show_error("Format file csv salah")
            exit()

        wrapped: Slice[A] = slice_map(parsed, lambda r, _: wrap(r))
        return wrapped

    return (
        fn(USER_PATH, META_LIST[0], lambda r: User((r[0], r[1], r[2]))),
        fn(CANDI_PATH, META_LIST[1], lambda r: Candi((int(r[0]), r[1], int(r[2]), int(r[3]), int(r[4])))),
        fn(BAHAN_PATH, META_LIST[2], lambda r: Bahan((r[0], r[1], int(r[2]))))
    )

def write_data(path: str, slices: tuple[Slice[User], Slice[Candi], Slice[Bahan]]) -> None:
    (folder_size, folder_array, _) = str_split(path, "/")
    (user, candi, bahan) = slices

    curr = ""
    for i in range(folder_size):
        curr += ("/" if i != 0 else "") + folder_array[i]
        if not exists(curr):
            print(f"Membuat folder {curr}")
            makedirs(curr)

    USER_PATH = f"{path}/user.csv"
    CANDI_PATH = f"{path}/candi.csv"
    BAHAN_PATH = f"{path}/bahan_bangunan.csv"

    def fn(path: str,  slice: Slice[Any], meta: CSV_Meta):
        unwrapped = slice_map(slice, lambda v, _: [str(v[i]) for i in range(meta[0])])
        raw = csv_maker(unwrapped, meta)
        open(path, 'w').write(raw)

    fn(USER_PATH, user, META_LIST[0])
    fn(CANDI_PATH, candi, META_LIST[1])
    fn(BAHAN_PATH, bahan, META_LIST[2])