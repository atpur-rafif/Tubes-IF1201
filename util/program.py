from typing import Callable, Union
from custom_typing import *

def show_error(msg: str) -> None:
    print('\033[93m' + msg + '\033[0m')

def error_exit(msg: str) -> None:
    print('\033[91m' + msg + '\033[0m')
    exit()

def wrap_partial(value: A, make_none: bool) -> Union[A, None]:
    if make_none:
        return None
    return value

# RECURSIVE
def input_validator(msg: str, error: Callable[[str], str], check: Callable[[str], bool]) -> str:
    value = input(msg)
    if not check(value):
        show_error(error(value))
        return input_validator(msg, error, check)
    else:
        return value
