from typing import Any, Callable
from custom_typing import *

def create_slice(base: tuple[int, list[A | Any]] = (0, [])) -> Slice[A | Any]:
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

def slice_fold(slice: Slice[A], init: B, fn: Callable[[B, A, int], B]) -> B:
    (size, array, _) = slice

    value = init
    for i in range(size):
        value = fn(value, array[i], i)

    return value

# Slice filter (smaller resize)
def slice_filter(slice: Slice[A], fn: Callable[[A, int], bool]):
    return slice_fold(slice, create_slice(), lambda v, a, i: slice_append(v, a) if fn(a, i) else v)

def slice_remove(slice: Slice[A], fn: Callable[[A, int], bool]):
    return slice_filter(slice, lambda v, i: not fn(v, i))

def slice_remove_target(slice: Slice[A], target: A):
    return slice_remove(slice, lambda v, _: v == target)

# Slice getter
def slice_get_size(slice: Slice[Any]) -> int:
    return slice[0]

def slice_get_array(slice: Slice[A]) -> list[A]:
    return [slice[1][i] for i in range(slice[0])]

def slice_get_array_lazy(slice: Slice[A]) -> list[A]:
    return slice[1]

def slice_get_max_size(slice: Slice[A]) -> int:
    return slice[2]

# Slice get and count
def slice_get_element(slice: Slice[A], fn: Callable[[A, int], bool]) -> A | None:
    return slice_fold(slice, None, lambda v, a, i: v if v != None else (a if fn(a, i) else None))

def slice_count(slice: Slice[A], fn: Callable[[A, int], bool]):
    return slice_fold(slice, 0, lambda v, a, i: v + 1 if fn(a, i) else v)