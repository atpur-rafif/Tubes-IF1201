from custom_typing import *

from util.slice import *
from util.str import *
from util.program import *

def csv_parser(string: str) -> tuple[Slice[list[str]], CSV_Meta]:
    (row_size, row, _) = str_split(string, "\n")

    table = slice_create()

    header = ""
    header_len = -1
    for i in range(row_size):
        if row[i] == "":
            continue

        col = str_split(row[i], ";")
        col_size = slice_get_size(col)
        col_array = slice_get_array(col)

        if header_len == -1:
            header_len = col_size
            header = row[i]
            continue

        if col_size != header_len:
            show_error(f"Invalid row: {row[i]}")
            continue

        table = slice_append(table, col_array)

    return (table, (header_len, header))

