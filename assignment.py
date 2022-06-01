import numpy as np


def uniform_good(mult=16807, mod=(2 ** 31) - 1, seed=123456789, size=1):
    u = np.zeros(size)
    x = (seed * mult + 1) % mod
    u[0] = x / mod
    for i in range(1, size):
        x = (x * mult + 1) % mod
        u[i] = x / mod
    return u


def uniform(low=0, high=1, seed=123456789, size=1):
    return low + (high - low) * uniform_good(seed=seed, size=size)



circle = 0

for i in range(0, 10000):
    x = uniform()
    y = uniform()
    distance = (x * x + y * y) ** 0.5

    if distance < 1:
        circle += 1

pi = 4 * circle / 10000
a =print(pi)
print(a)

