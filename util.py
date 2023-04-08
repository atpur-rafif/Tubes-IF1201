def show_error(msg: str):
    print(msg)

def error_exit(msg: str):
    show_error(msg)
    exit()

# Force len only can be use by string data type
def str_len(string: str):
    return len(string)