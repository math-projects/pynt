"""Factorize integers"""


from collections import deque
from dataclasses import dataclass, field

import numpy as np

from py3nt.core.base import BaseFactorization, BaseSieveFactorization
from py3nt.core.primality_test import is_prime
from py3nt.core.sieve import SieveOfEratosthenes, SieveOfEratosthenesOptimized
from py3nt.defaults import (
    BIGGEST_NUMBER,
    LARGEST_SMALL_NUMBER,
    LOGN_PRIME_FACTOR_FIELD,
    MAX_LOGN_FACTORIZATION_LIMIT,
)
from py3nt.numbers.integer import Integer


def is_prime_power(n: int) -> tuple[int, int]:
    """Check if :math:`n` is a prime power or not.

    Parameters
    ----------
    n : ``int``
        A positive integer.

    Returns
    -------
    tuple[int, int]
        :math:`(p, e)` where :math:`n=p^{e}`.
    """

    if n < 2:
        return (0, 0)

    lim: int = int(np.log2(n))

    for i in range(1, lim + 1):
        root = Integer(n).kthroot(k=i)
        if root**i == n:
            if is_prime(root):
                return (root, i)

    return (0, lim)


@dataclass
class NaiveSqrtFactorization(BaseFactorization):
    """
    Factorize small numbers in sqrt(n) complexity.

    Methods
    -------
    factorize:
        Factorize a positive integer using naive sqrt method.
    """

    def factorize(self, n: int) -> dict[int, int]:
        root = int(np.floor(np.sqrt(1.0 * n)))

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


@dataclass
class SieveSqrtFactorization(BaseSieveFactorization):
    r"""
    Factorization using naive sieve and primes not exceeding :math:`\sqrt{n}`.

    Methods
    -------
    factorize:
        Factorize a positive integer using sieve generated primes not exceeding :math:`\sqrt{n}`.
    """

    def factorize(self, n: int) -> dict[int, int]:
        primes = self.sieve.primes_
        root = int(np.floor(np.sqrt(1.0 * n)))

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


@dataclass
class LognSieveFactorization(BaseSieveFactorization):
    """
    Factorize small numbers in logn complexity.

    Methods
    -------
    factorize:
        Factorize a positive integer using pre-stored prime factors.
    """

    def factorize(self, n: int) -> dict[int, int]:
        factorization: dict[int, int] = {}
        prime_factors = getattr(self.sieve, LOGN_PRIME_FACTOR_FIELD)

        while n > 1:
            prime_factor = prime_factors[n]

            multiplcity = 0
            while (n % prime_factor) == 0:
                n //= prime_factor
                multiplcity += 1

            factorization[prime_factor] = multiplcity

        return factorization


@dataclass
class BigIntFactorization(BaseFactorization):
    """
    Factorize large positive integers not exceeding a default biggest number.

    Methods
    -------
    factorize:
        Factorize a positive integer using Pollard's rho algorithm.
    """

    def factorize(self, n) -> dict[int, int]:
        if np.greater(n, BIGGEST_NUMBER):
            raise ValueError(
                f"{n} is greater than the current default biggest number: {BIGGEST_NUMBER}"
            )

        queue = deque([n])
        factorization: dict = {}

        while queue:
            cur = queue.popleft()

            if is_prime(n=cur):
                if cur in factorization:
                    factorization[cur] += 1
                else:
                    factorization[cur] = 1
            else:
                factor = Integer(cur).brent_pollard_rho_factor()
                queue.append(factor)
                queue.append(cur // factor)

        return factorization


@dataclass
class FactorizationFactory:
    """Factorize positive integers not exceeding the default biggest number.

    Methods
    -------
    factorize:
        Factorize a positive integer.

    Raises
    ------
    ValueError
        If n is negative or exceeds the default biggest number.
    """

    N: int
    with_sieve: bool = field(default=True)

    factorizer: BaseFactorization = field(init=False)

    def __post_init__(self) -> None:
        self.factorizer = self._get_factorizer_class()

        if isinstance(self.factorizer, BaseSieveFactorization):
            self.factorizer.regenerate_primes()

    def _get_factorizer_class(self) -> BaseFactorization:
        if not self.with_sieve:
            return NaiveSqrtFactorization()
        if np.less_equal(self.N, MAX_LOGN_FACTORIZATION_LIMIT):
            return LognSieveFactorization(sieve=SieveOfEratosthenesOptimized(limit=self.N))
        if np.less_equal(self.N, LARGEST_SMALL_NUMBER):
            return SieveSqrtFactorization(
                sieve=SieveOfEratosthenes(limit=int(np.floor(np.sqrt(self.N * 1.0))))
            )
        return BigIntFactorization()

    def factorize(self, n: int) -> dict[int, int]:
        """Factorize positive integers.

        Parameters
        ----------
        n : ``int``
            A positive integer.

        Returns
        -------
        dict[int, int]
            Key value pairs of prime factorization.
            Keys are prime factors.
            Values are multiplicities of corresponding prime factors.

        Raises
        ------
        ValueError
            If :math:`n` is not positive.
        """

        if n < 1:
            raise ValueError("n must be a positive integer")

        if n == 1:
            return {1: 1}

        return self.factorizer.factorize(n=n)
