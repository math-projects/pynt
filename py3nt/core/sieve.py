"""Generate primes using sieve"""


from dataclasses import dataclass, field

import numpy as np

from py3nt.core.base import BaseSieve


@dataclass
class SieveOfEratosthenes(BaseSieve):
    r"""
    Sieve of Eratosthenes for generating primes.
    Usually used for factorizing by division of primes not exceeding :math:`\sqrt{n}`.
    So, in most cases ``limit`` should be set to :math:`\ceil{\sqrt{n}}`.

    Methods
    -------
    generate_primes:
        Generate primes up to ``limit`` using sieve of Eratosthenes.
    """

    def generate_primes(self) -> None:
        """Generate primes and set it in ``self.primes_``"""

        flags = np.zeros(shape=(self.limit + 1,), dtype=np.byte)

        if (not self.limit) or self.limit < 2:
            return

        prime_count = 1
        self.primes_[0] = 2
        for i in np.arange(start=3, stop=self.limit + 1, step=2):
            if flags[i] == 0:
                self.primes_[prime_count] = i
                prime_count += 1
                flags[i * i : self.limit + 1 : i * 2] = 1


@dataclass
class SieveOfEratosthenesOptimized(BaseSieve):
    r"""
    We can store smallest prime factors for :math:`\log{n}` factorization.
    Therefore, :math:`n` must be in sieve range.

    Methods
    -------
    generate_primes:
        Generate primes using pre-stored prime factors of positive integers.
    """

    largest_prime_factors_: np.ndarray = field(init=False)

    def __post_init__(self) -> None:
        super().__post_init__()
        self.largest_prime_factors_ = np.empty(shape=(0,), dtype=int)

    def generate_primes(self) -> None:
        """Generate primes using largest prime factors"""

        if self.limit < 2:
            return

        self.largest_prime_factors_ = np.empty(shape=(self.limit + 1,), dtype=int)

        self.primes_[0] = 2

        prime_count = 1

        for i in np.arange(start=0, stop=self.limit + 1):
            self.largest_prime_factors_[i] = i

        for i in np.arange(start=2, stop=self.limit + 1, step=2):
            self.largest_prime_factors_[i] = 2

        for i in np.arange(start=3, stop=self.limit + 1, step=2):
            if self.largest_prime_factors_[i] == i:
                self.primes_[prime_count] = i
                prime_count += 1
                self.largest_prime_factors_[i * i : self.limit + 1 : 2 * i] = i

        self.num_primes = prime_count
