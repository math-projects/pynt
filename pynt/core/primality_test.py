"""Define primality tests"""

import numpy as np


def is_prime_naive(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True

    if (n & 1) == 0:
        return False

    root = int(np.floor(np.sqrt(n)))

    for i in np.arange(start=3, stop=root + 1, step=2):
        if (n % i) == 0:
            return False

    return True
