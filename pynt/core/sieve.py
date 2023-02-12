"""Generate primes using sieve"""

from dataclasses import dataclass, field

import numpy as np


@dataclass
class SieveOfEratosthenes:
    """Sieve of Eratosthenes for generating primes"""

    size: int

    primes_: list = field(init=False)
    smallest_factors_: list = field(init=False)

    def __post_init__(self):
        self.primes_ = []
        self.smallest_factors_ = []

    def generate_primes(self) -> None:
        """Generate primes and set it in ``self.primes_``"""

        flags = np.zeros(shape=(self.size,))

        primes = [2]
        for i in np.arange(start=3, stop=self.size, step=2):
            if flags[i] == 0:
                primes.append(i)
                for j in np.arange(start=i * i, stop=self.size, step=2 * i):
                    flags[j] = 1

        self.primes_ = primes
