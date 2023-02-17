"""Generate primes using sieve"""


from dataclasses import dataclass

import numpy as np

from py3nt.core.base import BaseSieve


@dataclass
class SieveOfEratosthenes(BaseSieve):
    """Sieve of Eratosthenes for generating primes"""

    def generate_primes(self) -> None:
        """Generate primes and set it in ``self.primes_``"""

        flags = np.zeros(shape=(self.size,), dtype=np.uint8)

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

        if not self.logn_limit:
            raise ValueError("logn_limit cannot be None")

        if self.logn_limit < 2:
            return

        smallest_factors = np.zeros(shape=(self.logn_limit + 1,), dtype=int)
        self.primes_ = [2]

        for i in np.arange(start=0, stop=self.logn_limit + 1):
            smallest_factors[i] = i

        for i in np.arange(start=2, stop=self.logn_limit + 1, step=2):
            smallest_factors[i] = 2

        for i in np.arange(start=3, stop=self.logn_limit + 1, step=2):
            if smallest_factors[i] == i:
                self.primes_.append(i)

                for j in np.arange(start=3 * i, stop=self.logn_limit + 1, step=2 * i):
                    if smallest_factors[j] == j:
                        smallest_factors[j] = i

        self.smallest_factors_ = list(smallest_factors)
