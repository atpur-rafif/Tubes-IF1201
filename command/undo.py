from state import *
from custom_typing import *

def run():
    (stack_size, stack, _) = get_undo_stack()
    top = stack[stack_size - 1]
    set_undo_stack(slice_remove_target(get_undo_stack(), top))

    (user, candi_size, candi) = top

    exist = slice_get_element(get_user(), lambda u, _: u[0] == user[0])

    if exist != None:
        prompt = input_validator(
            "Terdapat user baru dengan nama yang sama\n(1) User baru\n(2) User lama\nLakukan simpan: ",
            lambda v: f"Input \"{v}\" tidak valid",
            lambda v: v == "1" or v == "2"
        )

        if prompt == "1":
            print("Undo dibatalkan, menggunakan user baru")
            return
        elif prompt == "2":
            set_user(slice_remove_target(get_user(), exist))

            def filter_fn(c: Candi, _: Any):
                if exist != None and exist[0] == c[1]:
                    empty_candi_id(c[0])
                    return True
                return False

            set_candi(slice_filter(get_candi(), filter_fn))

    set_user(slice_append(get_user(), user))
    for i in range(candi_size):
        c = candi[i]
        set_candi(slice_append(get_candi(), Candi((create_candi_id(), c[1], c[2], c[3], c[4]))))

    print("Jin berhasil dikembalikan")
