from typing import TypeVar

A = TypeVar("A")
B = TypeVar("B")

# Custom data type, inspired by go slice
# (size, array, max_size)
Slice = tuple[int, list[A], int]

nama = str
password = str
role = str
User = tuple[nama, password, role]

id = int
pembuat = str
pasir = int
batu = int
air = int
Candi = tuple[id, pembuat, pasir, batu, air]

nama = str
deskripsi = str
jumlah = int
Bahan = tuple[nama, deskripsi, jumlah]