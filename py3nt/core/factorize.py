"""Factorize integers"""


from dataclasses import dataclass

import numpy as np

from py3nt.core.base import BaseFactorizer, BaseSieve
from py3nt.core.sieve import SieveOfEratosthenesOptimized
from py3nt.defaults import MAX_LOGN_FACTORIZATION_LIMIT


@dataclass
class Factorizer(BaseFactorizer):
    """Factorize positive integers"""

    def _factorize_with_sieve(self, n: int) -> dict[int, int]:
        if not isinstance(self.sieve, BaseSieve):
            raise ValueError("Invalid sieve")

        if isinstance(self.sieve, SieveOfEratosthenesOptimized):
            if self.sieve.largest_prime_factors_.shape[0] < self.max_logn_limit:
                if self.max_logn_limit <= MAX_LOGN_FACTORIZATION_LIMIT:
                    self.sieve.generate_primes()

                    return self.factorize_logn(n=n)

        primes = self.sieve.primes_
        root = int(np.floor(np.sqrt(n)))

        factorization = {}

        for prime in primes:
            if prime > root:
                break

            if (n % prime) == 0:
                multiplicity = 0
                while (n % prime) == 0:
                    n //= prime
                    multiplicity += 1

                factorization[prime] = multiplicity

        if n > 1:
            factorization[n] = 1

        return factorization

    def factorize_small(self, n: int) -> dict[int, int]:
        if self.sieve:
            return self._factorize_with_sieve(n=n)

        root = int(np.floor(np.sqrt(n)))

        factorization = {}

        for i in np.arange(start=2, step=1, stop=root + 1):
            if (n % i) == 0:
                prime_factor = i
                multiplicity = 0

                while (n % prime_factor) == 0:
                    n //= prime_factor
                    multiplicity += 1
                factorization[prime_factor] = multiplicity

        if n > 1:
            factorization[n] = 1

        return factorization

    def factorize_big(self, n: int) -> dict[int, int]:
        return {}
