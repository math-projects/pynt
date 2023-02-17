"""Factorize integers"""


from dataclasses import dataclass

import numpy as np

from py3nt.core.base import BaseFactorizer


@dataclass
class Factorizer(BaseFactorizer):
    """Factorize positive integers"""

    def _factorize_with_sieve(self, n: int) -> dict[int, int]:
        if not self.sieve:
            raise ValueError("Sieve cannot be None")

        if n < 1e7:
            return self.factorize_logn(n)

        if len(self.sieve.primes_) < 1:
            self.sieve.generate_primes()

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

        if n < 2:
            return {1: 1}

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
