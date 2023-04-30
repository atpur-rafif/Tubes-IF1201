from time import time

seed = int(time() * 1e6)
X = [int(time() * 1e6)]

# glibc parameter, source: https://en.wikipedia.org/wiki/Linear_congruential_generator#Parameters_in_common_use
A = (1103515245)
C = (12345)
M = (2 ** 31 - 1)

def random_gclib() -> int:
    X[0] = int((A * X[0] + C) % M)
    return X[0]

def random_range(start: int, end: int) -> int:
    return start + (random_gclib() % (end - start + 1))