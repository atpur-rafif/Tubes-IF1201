from typing import Any, Callable, Union
from custom_typing import *

# Membuat data slice baru
def slice_create(base: tuple[int, list[Union[A, Any]]] = (0, [])) -> Slice[Union[A, Any]]:
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

# RECURSIVE
# Fold pattern untuk slice
def slice_fold(slice: Slice[A], init: B, fn: Callable[[B, A, int], B]) -> B:
    (size, array, max_size) = slice
    i = size - 1

    if size == 0:
        return init
    elif i == 0:
        return fn(init, array[i], i)
    else:
        value = slice_fold(Slice((size - 1, array, max_size)), init, fn)
        return fn(value, array[i], i)

def slice_map(slice: Slice[A], fn: Callable[[A, int], B]) -> Slice[B]:
    new_slice: Any = slice
    (size, array, max_size) = new_slice

    new_array: list[Any] = [None for _ in range(max_size)]

    for i in range(size):
        new_array[i] = fn(array[i], i)
    
    return (size, new_array, max_size)

# Slice filter, operasi yang memperkecil slice
def slice_filter(slice: Slice[A], fn: Callable[[A, int], bool]) -> Slice[A]:
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
def slice_get_element(slice: Slice[A], fn: Callable[[A, int], bool]) -> Union[A, None]:
    return slice_fold(slice, None, lambda v, a, i: v if v != None else (a if fn(a, i) else None))

def slice_count(slice: Slice[A], fn: Callable[[A, int], bool]):
    return slice_fold(slice, 0, lambda v, a, i: v + 1 if fn(a, i) else v)


# Mutate slice, dengan menggunakan callback
def slice_update(slice: Slice[A], fn: Callable[[A, int], Union[A, None]]):
    (size, array, max_size) = slice

    for i in range(size):
        new = fn(array[i], i)

        if new == None:
            continue

        array[i] = new

    return (size, array, max_size)

def slice_update_target(slice: Slice[A], target: A, new: A):
    return slice_update(slice, lambda v, _: new if v == target else None)

