from typing import TypeVar, Literal

A = TypeVar("A")
B = TypeVar("B")

# Custom data type, inspired by go slice
# (size, array, max_size)
Slice = tuple[int, list[A], int]

nama = str
password = str
role = Literal["bandung_bondowoso", "roro_jonggrang", "jin_pengumpul", "jin_pembangun"]
User = tuple[nama, password, role]

id = int
pembuat = str
pasir = int
batu = int
air = int
Candi = tuple[id, pembuat, pasir, batu, air]

nama = Literal["pasir", "batu", "air"]
deskripsi = str
jumlah = int
Bahan = tuple[nama, deskripsi, jumlah]

CSV_Meta = tuple[int, str]