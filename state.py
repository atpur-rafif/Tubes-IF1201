from slice import *

def create_state(init: A) -> tuple[Callable[[], A], Callable[[A], None]]:
    mutable = [init]

    def get():
        return mutable[0]

    def set(new: A):
        mutable[0] = new

    return (get, set)

(get_user, set_user) = create_state(slice_create())
(get_candi, set_candi) = create_state(slice_create())
(get_bahan, set_bahan) = create_state(slice_create())

(get_logged_as, set_logged_as) = create_state(User())