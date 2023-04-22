from state import *

def run():
    (stack_size, stack, _) = get_undo_stack()
    top = stack[stack_size - 1]
    set_undo_stack(slice_remove_target(get_undo_stack(), top))

    (user, candi_size, candi) = top

    exist = slice_get_element(get_user(), lambda u, _: u[0] == user[0])

    if exist != None:
        prompt = input_validator(
            "Terdapat user dengan nama yang sama, simpan:\n (1) Gabungan\n(2) User awal\n(3) User terbaru",
            lambda v: f"Input \"{v}\" tidak valid",
            lambda v: v == "1" or v == "2" or v == "3"
        )

        if prompt == "2":
            print("Undo dibatalkan, menggunakan user awal")
            return
        elif prompt == "3":
            set_user(slice_remove_target(get_user(), exist))
            set_candi(slice_filter(get_candi(), lambda c, _: c[1] == exist[0]))

    set_user(slice_append(get_user(), user))
    for i in range(candi_size):
        c = candi[i]
        set_candi(slice_append(get_candi(), Candi((create_candi_id(), c[1], c[2], c[3], c[4]))))
