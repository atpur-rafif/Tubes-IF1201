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