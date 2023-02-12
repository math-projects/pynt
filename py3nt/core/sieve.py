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

        if self.size < 2:
            return

        self.primes_ = [2]
        for i in np.arange(start=3, stop=self.size, step=2):
            if flags[i] == 0:
                self.primes_.append(i)
                for j in np.arange(start=i * i, stop=self.size, step=2 * i):
                    flags[j] = 1

    def generate_smallest_prime_factors(self) -> None:
        """Generate primes using smallest prime factors"""

        if self.size < 2:
            return

        smallest_factors = np.zeros(shape=(self.size,))
        self.primes_ = [2]

        for i in np.arange(start=0, stop=self.size):
            smallest_factors[i] = i

        for i in np.arange(start=2, stop=self.size, step=2):
            smallest_factors[i] = 2

        for i in np.arange(start=3, stop=self.size, step=2):
            if smallest_factors[i] == i:
                self.primes_.append(i)

                for j in np.arange(start=3 * i, stop=self.size, step=2 * i):
                    if smallest_factors[j] == j:
                        smallest_factors[j] = i

        self.smallest_factors_ = list(smallest_factors)
