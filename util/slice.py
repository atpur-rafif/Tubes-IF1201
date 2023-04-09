from typing import Any, Callable
from custom_typing import *

# Membuat data slice baru
def slice_create(base: tuple[int, list[A | Any]] = (0, [])) -> Slice[A | Any]:
    (size, array) = base
    slice: Slice[Any] = (0, [], 0)

    for i in range(size):
        slice = slice_append(slice, array[i])

    return slice

# Menambahkan elemen baru pada slice, dan meresize jika diperlukan
def slice_append(slice: Slice[A], new: A) -> Slice[A]:
    (size, array, max_size) = slice

    if max_size == 0 or size == max_size:
        max_size = 1 if max_size == 0 else max_size * 2
        new_array: list[Any] = [None for _ in range(max_size)]
        for i in range(size):
            new_array[i] = array[i]
        array = new_array

    array[size] = new
    return (size + 1, array, max_size)

# Fold pattern untuk slice
def slice_fold(slice: Slice[A], init: B, fn: Callable[[B, A, int], B]) -> B:
    (size, array, _) = slice

    value = init
    for i in range(size):
        value = fn(value, array[i], i)

    return value

# Slice filter, operasi yang memperkecil slice
def slice_filter(slice: Slice[A], fn: Callable[[A, int], bool]):
    return slice_fold(slice, slice_create(), lambda v, a, i: slice_append(v, a) if fn(a, i) else v)

def slice_remove(slice: Slice[A], fn: Callable[[A, int], bool]):
    return slice_filter(slice, lambda v, i: not fn(v, i))

def slice_remove_target(slice: Slice[A], target: A):
    return slice_remove(slice, lambda v, _: v == target)

# Slice getter, mendapatkan data mengenai slice
def slice_get_size(slice: Slice[Any]) -> int:
    return slice[0]

def slice_get_array(slice: Slice[A]) -> list[A]:
    return [slice[1][i] for i in range(slice[0])]

def slice_get_array_lazy(slice: Slice[A]) -> list[A]:
    return slice[1]

def slice_get_max_size(slice: Slice[A]) -> int:
    return slice[2]

# Slice get and count, mendapatkan informasi dengan callback
def slice_get_element(slice: Slice[A], fn: Callable[[A, int], bool]) -> A | None:
    return slice_fold(slice, None, lambda v, a, i: v if v != None else (a if fn(a, i) else None))

def slice_count(slice: Slice[A], fn: Callable[[A, int], bool]):
    return slice_fold(slice, 0, lambda v, a, i: v + 1 if fn(a, i) else v)

# Mutate slice, dengan menggunakan callback
def slice_update(slice: Slice[A], fn: Callable[[A, int], A | None]):
    (size, array, max_size) = slice

    for i in range(size):
        new = fn(array[i], i)

        if new == None:
            continue

        array[i] = new

    return (size, array, max_size)

def slice_update_target(slice: Slice[A], target: A, new: A):
    return slice_update(slice, lambda v, _: new if v == target else None)

def slice_map(slice: Slice[A], fn: Callable[[A, int], B]) -> Slice[B]:
    new_slice: Any = slice
    (size, array, _) = new_slice

    new_array: list[Any] = array

    for i in range(size):
        new_array[i] = fn(array[i], i)
    
    return new_slice
