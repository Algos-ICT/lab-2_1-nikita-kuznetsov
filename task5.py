with open("input.txt", 'r') as f:
    datafile = f.readlines()


def max_prize_amount(candies: int) -> tuple[int, list[int]]:

    if candies < 2:
        return 1, [candies]

    candy_per_child = [1]
    candies -= 1

    while candies > candy_per_child[-1]:
        new_candies = candy_per_child[-1] + 1
        candy_per_child.append(new_candies)
        candies -= new_candies

    candy_per_child[-1] += candies

    return len(candy_per_child), candy_per_child


if __name__ == '__main__':
    result1, result2 = max_prize_amount(int(datafile[0]))
    with open("output.txt", 'w') as f:
        f.write(f"{str(result1)}\n{' '.join(list(map(str, result2)))}")
