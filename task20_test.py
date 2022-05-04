import random
import time
from string import ascii_lowercase

from task20 import count_almost_palindromes


K = 10
S = ""
word_size = 100

for _ in range(word_size):
    S += random.choice(ascii_lowercase)
print(S)

start = time.perf_counter()
result = count_almost_palindromes(K, S)
print(time.perf_counter() - start)

