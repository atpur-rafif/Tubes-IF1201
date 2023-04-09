from util.slice import *
from custom_typing import *

def show_error(msg: str):
    print(msg)

def error_exit(msg: str):
    show_error(msg)
    exit()

def wrap_partial(value: A, make_none: bool) -> A | None:
    if make_none:
        return None
    return value

