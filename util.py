from slice import *

def show_error(msg: str):
    print(msg)

def error_exit(msg: str):
    show_error(msg)
    exit()

# Force len only can be use by string data type
def str_len(string: str):
    return len(string)

def str_split(string: str, splitter: str):
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

def str_join(slice: Slice[str], mid: str) -> str:
    (size, arr, _) = slice
    result = ""

    for i in range(size):
        result += arr[i] + (mid if i  + 1 != size else "")

    return result