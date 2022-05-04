

def can_divide(coins, n, first, second, third, cache):
    if first == 0 and second == 0 and third == 0:
        if n < 0:
            return True
        return False

    if n < 0:
        return False

    way = (first, second, third)
    if way not in cache:
        to_first = False
        to_second = False
        to_third = False

        if first - coins[n] >= 0:
            to_first = can_divide(coins, n - 1, first - coins[n], second, third, cache)
        if not to_first and second - coins[n] >= 0:
            to_second = can_divide(coins, n - 1, first, second - coins[n], third, cache)
        if not to_first and not to_second and third - coins[n] >= 0:
            to_third = can_divide(coins, n - 1, first, second, third - coins[n], cache)

        cache[way] = to_first or to_second or to_third

    return cache[way]


if __name__ == '__main__':
    with open("input.txt", 'r') as f:
        datafile = f.readlines()

    n = int(datafile[0]) - 1
    coins = list(map(int, datafile[1].split()))

    summ = sum(coins)
    if summ % 3 != 0:
        result = False
    else:
        third = summ // 3
        result = can_divide(coins, n, third, third, third, {})

    with open("output.txt", 'w') as f:
        f.write("1") if result else f.write("0")
