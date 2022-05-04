

def find_max_weight(capacity: int, ingots: list[int], max_weight: int = 0) -> int:
    # if all ingots processed return max_weight
    if not ingots:
        return max_weight

    # finding heaviest ingot and check if it fits
    heaviest = max(ingots)
    if max_weight + heaviest <= capacity:
        max_weight += heaviest

    # removing heaviest anyway and processing other ingots
    ingots.remove(heaviest)
    return find_max_weight(capacity, ingots, max_weight)


if __name__ == '__main__':
    with open("input.txt", 'r') as f:
        datafile = f.readlines()

    w = int(datafile[0].split()[0])
    w_array = [int(i) for i in datafile[1].split()]
    result = str(find_max_weight(w, w_array))

    with open("output.txt", 'w') as f:
        f.write(result)
