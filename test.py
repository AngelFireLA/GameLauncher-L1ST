import sys
import time


def factorielle(n):
    if n <= 0:
        return 1
    return n * factorielle(n - 1)

def factorielle_itérative(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        if i % 10000 == 0:
            print(i, len(str(fact)))
    return fact

start_time = time.perf_counter()
f = factorielle(500)
print(time.perf_counter()-start_time)

start_time = time.perf_counter()
f2 = factorielle_itérative(500)
print(time.perf_counter()-start_time)
# print(f, len(str(f)))
# print()
