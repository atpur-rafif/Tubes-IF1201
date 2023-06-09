from env import *
from typing import Union
from util.slice import *
from util.data import *

def create_state(init: A) -> tuple[Callable[[], A], Callable[[A], None]]:
    mutable = [init]

    def get():
        return mutable[0]

    def set(new: A):
        mutable[0] = new

    return (get, set)

# Panggil fungsi ini untuk mendapatkan data dan merubah data
# Contoh:
#   user = get_user()
#   (Operasi pada variabel user)
#   set_user(user)

DEFAULT_USER = slice_create((2, [
    User(("Bondowoso", "cintaroro", "bandung_bondowoso")), 
    User(("Roro", "gasukabondo", "roro_jonggrang"))
    ]))

if Folder == None:
    prompt = input_validator(
        "Folder save tidak diberikan, membuat save baru (Y/N)? ",
        lambda v: f"Input \"{v}\" tidak valid",
        lambda v: v == "Y" or v == "N"
    )

    if prompt == "N":
        print("Keluar program...")
        exit()
    
    Folder = input_validator(
        "Masukkan folder save baru: ",
        lambda v: f"Folder \"{v}\" sudah digunakan",
        lambda v: not exists(v)
    )

    write_data(Folder, (
        DEFAULT_USER,
        slice_create(), 
        slice_create()
    ))

    print("Save data baru berhasil dibuat")

(USER_SLICE, CANDI_SLICE, BAHAN_SLICE) = read_data(Folder)

(get_user, set_user) = create_state(USER_SLICE)
(get_candi, set_candi) = create_state(CANDI_SLICE)
(get_bahan, set_bahan) = create_state(BAHAN_SLICE)

(get_logged_as, set_logged_as) = create_state(wrap_partial(User(), True))

def get_role() -> Union[role, None]:
    user = get_logged_as()
    if user == None:
        return None
    return user[2]

BAHAN_SIZE = 3
BAHAN_LIST = [
    ("pasir", "ini pasir"),
    ("batu", "ini batu"),
    ("air", "ini air")
]

# Initialize bahan
for i in range(BAHAN_SIZE):
    bahan = slice_get_element(get_bahan(), lambda b, _: b[0] == BAHAN_LIST[i][0]) 
    if bahan == None:
        set_bahan(slice_append(get_bahan(), Bahan((BAHAN_LIST[i][0], BAHAN_LIST[i][1], 0))))

max_id = slice_fold(get_candi(), -1, lambda v, a, _: a[0] if a[0] > v else v)
(get_candi_id, set_candi_id) = create_state(max_id)
(get_unused_id, set_unused_id) = create_state(slice_create())

def empty_candi_id(i: int):
    set_unused_id(slice_append(get_unused_id(), i))

def create_candi_id() -> int:
    (unused_length, unused_array, _) = get_unused_id()

    if unused_length == 0:
        set_candi_id(get_candi_id() + 1)
        return get_candi_id()
    else:
        min = unused_array[0]
        for i in range(unused_length):
            if unused_array[i] < min:
                min = unused_array[i]
        set_unused_id(slice_remove_target(get_unused_id(), min))
        return min

used_id = [False for _ in range(max_id + 1)]
(candi_size, candi_array, _) = get_candi()

for i in range(candi_size):
    used_id[candi_array[i][0]] = True

for i in range(max_id):
    if used_id[i] == False:
        empty_candi_id(i)

# Element of undo stack (user, banyak_candi, list of candi)
def undo_slice_wrapper() -> Slice[tuple[User, int, list[Candi]]]:
    return slice_create()
(get_undo_stack, set_undo_stack) = create_state(undo_slice_wrapper())