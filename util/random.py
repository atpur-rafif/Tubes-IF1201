from time import time

def create_random_range(start: int, end: int):
    m = end - start

    seed = int(time() * 1e6)
    gen_state = [int(seed % m)]
    A = int((seed // m) % (m - 1)) + 1
    C = int((seed // (m * m)) % (m - 1)) + 1

    def generator():
        gen_state[0] = int((A * gen_state[0] + C) % m)
        return start + gen_state[0]

    return generator