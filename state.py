from env import *
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

(USER_SLICE, CANDI_SLICE, BAHAN_SLICE) = read_data(FOLDER)

(get_user, set_user) = create_state(USER_SLICE)
(get_candi, set_candi) = create_state(CANDI_SLICE)
(get_bahan, set_bahan) = create_state(BAHAN_SLICE)

(get_logged_as, set_logged_as) = create_state(wrap_partial(User(), True))

def get_role() -> role | None:
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
        set_bahan(slice_append(get_bahan(), Bahan((BAHAN_LIST[i][0], BAHAN_LIST[0][1], 0))))

max_id = slice_fold(get_candi(), -1, lambda v, a, _: a[0] if a[0] > v else v)
(get_candi_id, set_candi_id) = create_state(max_id)

def create_candi_id():
    set_candi_id(get_candi_id() + 1)
    return get_candi_id()
