

def find_max_weight(capacity: int, ingots: list[int]) -> int:
    taken = [[True] + [False] * capacity]

    for ingot in ingots:
        taken.append(taken[-1][:])

        for weight in range(ingot, capacity + 1):
            taken[-1][weight] = taken[-2][weight] or taken[-2][weight - ingot]
        taken = taken[-1:]

    for weight in range(capacity, -1, -1):
        if taken[-1][weight]:
            return weight


if __name__ == '__main__':
    with open("input.txt", 'r') as f:
        datafile = f.readlines()

    w = int(datafile[0].split()[0])
    w_array = [int(i) for i in datafile[1].split()]
    result = str(find_max_weight(w, w_array))

    with open("output.txt", 'w') as f:
        f.write(result)
