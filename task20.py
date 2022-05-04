


def is_almost_palindrome(k: int, word: str):
    if len(word) == 1:
        return True
    if k >= len(word)//2:
        return True

    # else
    counter = 0
    w_len = len(word)
    for i in range(w_len//2):
        if word[i] != word[w_len - i - 1]:
            counter += 1
            if counter > k:
                return False
    return True


def find_all_substrings(string: str):
    for i in range(len(string)):
        for j in range(i, len(string)):
            yield string[i:j + 1]


def count_almost_palindromes(k: int, string: str) -> int:
    counter = 0
    for substring in find_all_substrings(string):
        if is_almost_palindrome(k, substring):
            counter += 1
    return counter


if __name__ == '__main__':
    with open("input.txt", 'r') as f:
        datafile = f.readlines()

    K = int(input().split()[1])
    S = input()

    result = count_almost_palindromes(K, S)

    with open("output.txt", 'w') as f:
        f.write(str(result))
