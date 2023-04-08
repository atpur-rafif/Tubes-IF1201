from typing import Any
from custom_typing import *

def create_slice(base: tuple[int, list[A]] = (0, [])) -> Slice[A]:
    (size, array) = base
    slice: Slice[Any] = (0, [], 0)

    for i in range(size):
        slice = slice_append(slice, array[i])

    return slice

def slice_append(slice: Slice[A], new: A) -> Slice[A]:
    (size, array, max_size) = slice

    if size + 1 == max_size:
        max_size *= 2
        new_array: list[Any] = [None for _ in range(max_size)]
        for i in range(size):
            new_array[i] = array[i]
        array = new_array

    array[size] = new
    return slice


