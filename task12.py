

def half_subset(array: list[int]) -> tuple[int, list[int]]:
    if sum(array) % 2 > 0:
        return -1, []

    half = sum(array) // 2
    array_copy = array.copy()
    index_array = []

    for i, _ in enumerate(array):
        check = array_copy[-1]
        if check <= half:
            half -= check
            index_array.append(array.index(check) + 1)
        array_copy = array_copy[:-1]

    return len(index_array), sorted(index_array)


if __name__ == '__main__':
    with open("input.txt", 'r') as f:
        datafile = f.readlines()

    result = half_subset(list(map(int, datafile[1].split())))
    with open("output.txt", 'w') as f:
        f.write(str(result))


