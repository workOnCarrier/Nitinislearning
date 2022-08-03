# non generator solution
def get_total_from_log_file(filename: str) -> int:
    file_obj = open(filename)
    total = 0
    for line in file_obj:
        bytestr = line.rsplit(None, 1)[1]  # assuming last column as a number of bytes downloaded
        if bytestr == '-':
            continue
        total += int(bytestr)
    return total


# generator_solution
def get_total_using_generator(filename: str) -> int:
    file_obj = open(filename)
    byte_column = (line.rsplit(None, 1)[1] for line in file_obj)
    bytes = (int(x) for x in byte_column if x != '-')
    total = sum(bytes)
    return total
