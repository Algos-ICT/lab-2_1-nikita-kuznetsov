with open("input.txt", 'r') as f:
    datafile = f.readlines()


def how_many_stops(data: list[str]) -> int:

    dist = int(data[0])
    can_drive = int(data[1])
    stops = list(map(int, data[3].split()))

    if can_drive >= dist:
        return 0

    for i in range(len(stops) - 1):
        if stops[i + 1] - stops[i] > can_drive:
            return -1

    counter = 0
    drive_dist = can_drive
    while can_drive <= dist:
        for i, stop in enumerate(stops):
            if stop > can_drive:
                counter += 1
                stops = stops[i:]
                break
        can_drive += drive_dist
    else:
        last_stop = stops[-1]

    if last_stop < dist:
        counter += 1

    return counter


if __name__ == '__main__':
    result = how_many_stops(datafile)
    with open("output.txt", 'w') as f:
        f.write(str(result))
