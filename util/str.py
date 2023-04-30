from util.slice import *

# Force len only can be use by string data type
def str_len(string: str) -> int:
    return len(string)

def str_split(string: str, splitter: str) -> Slice[str]:
    string_len = str_len(string)
    splitter_len = str_len(splitter)

    slice = slice_create()

    word = ""
    i = 0
    while i < string_len:
        char = string[i]

        match = True
        if i + splitter_len <= string_len:
            for j in range(splitter_len):
                if string[i + j] != splitter[j]:
                    match = False
        else:
            match = False

        if match:
            slice = slice_append(slice, word)
            word = ""
            i += splitter_len
        else:
            word += char
            i += 1

    slice = slice_append(slice, word)

    return slice

# RECURSIVE
def str_join(slice: Slice[str], mid: str) -> str:
    (size, array, max_size) = slice
    i = size - 1

    if size == 0:
        return ""
    elif i == 0:
        return array[i]
    else:
        return str_join(Slice((size - 1, array, max_size)), mid) + mid + array[i]