"""Generate primes using sieve"""


from dataclasses import dataclass, field

import numpy as np

from py3nt.core.base import BaseSieve


@dataclass
class SieveOfEratosthenes(BaseSieve):
    """Sieve of Eratosthenes for generating primes"""

    def generate_primes(self) -> None:
        """Generate primes and set it in ``self.primes_``"""

        flags = np.zeros(shape=(self.limit + 1,), dtype=np.byte)

        if (not self.limit) or self.limit < 2:
            return

        self.primes_ = np.empty(shape=(self.max_prime_count,), dtype=int)

        prime_count = 1
        self.primes_[0] = 2
        for i in np.arange(start=3, stop=self.limit + 1, step=2):
            if flags[i] == 0:
                self.primes_[prime_count] = i
                prime_count += 1

                stop = int(np.floor(self.limit / i))

                for j in np.arange(start=i, stop=stop + 1, step=2):
                    non_prime = j * i
                    if non_prime > self.limit:
                        break
                    flags[non_prime] = 1

        self.num_primes = prime_count
        self.primes_ = self.primes_[:prime_count]


@dataclass
class SieveOfEratosthenesOptimized(BaseSieve):
    """We can store smallest prime factors for logn factorization"""

    smallest_factors_: np.ndarray = field(init=False)

    def generate_primes(self) -> None:
        """Generate primes using smallest prime factors"""

        if self.limit < 2:
            return

        self.smallest_factors_ = np.empty(shape=(self.limit + 1,), dtype=int)

        self.primes_ = np.empty(shape=(self.max_prime_count,))
        self.primes_[0] = 2

        prime_count = 1

        for i in np.arange(start=0, stop=self.limit + 1):
            self.smallest_factors_[i] = i

        for i in np.arange(start=2, stop=self.limit + 1, step=2):
            self.smallest_factors_[i] = 2

        for i in np.arange(start=3, stop=self.limit + 1, step=2):
            if self.smallest_factors_[i] == i:
                self.primes_[prime_count] = i
                prime_count += 1

                stop = int(np.floor(self.limit / i))
                for j in np.arange(start=i, stop=stop + 1, step=2):
                    not_prime = j * i
                    if self.smallest_factors_[not_prime] == not_prime:
                        self.smallest_factors_[not_prime] = i

        self.num_primes = prime_count
