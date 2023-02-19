"""Base classes"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional

import numpy as np

from py3nt.defaults import LARGEST_SMALL_NUMBER, MAX_LOGN_FACTORIZATION_LIMIT


@dataclass
class BaseSieve(ABC):
    """Abstract base class for sieve"""

    limit: int
    primes_: np.ndarray = field(init=False)
    num_primes: int = field(init=False, default=0)

    def __post_init__(self) -> None:
        self.clear()

    @abstractmethod
    def generate_primes(self) -> None:
        """Generate primes when size is small"""

    def clear(self) -> None:
        """Reset to initial state."""

        self.primes_ = np.empty(shape=(0,))
        self.num_primes = 0

    @property
    def max_prime_count(self) -> int:
        """Maximum number of primes possible up to n.

        :param n: Upper bound for primes.
        :type n: ``int``
        :return: An upper bound on number of primes not exceeding ``n``.
        :rtype: int
        """

        if self.limit < 2:
            return 0

        tmp = np.log(self.limit)
        res = 1.0 + (1.28 / tmp)
        res *= self.limit / tmp
        res = int(np.floor(res))

        return res


@dataclass
class BaseFactorizer(ABC):
    """Abstract base class for factorization"""

    sieve: Optional[BaseSieve] = field(default=None)
    max_logn_limit: int = field(default=MAX_LOGN_FACTORIZATION_LIMIT)
    largest_small_number: int = field(default=LARGEST_SMALL_NUMBER)

    def factorize_logn(self, n: int) -> dict[int, int]:
        """Factorize a positive integer in logn complexity.

        :param n: Positive integer to factorize.
        :type n: ```int```
        :raises ValueError: If sieve is ``None``.
        :return: Dictionary of prime factor, multiplicity as key-value pairs.
        :rtype: ``dict``
        """

        factorization: dict[int, int] = {}
        smallest_factors = getattr(self.sieve, "smallest_factors_")

        while n > 1:
            prime_factor = smallest_factors[n]

            multiplcity = 0
            while (n % prime_factor) == 0:
                n //= prime_factor
                multiplcity += 1

            factorization[prime_factor] = multiplcity

        return factorization

    @abstractmethod
    def factorize_small(self, n: int) -> dict[int, int]:
        """Factorize positive integers greater than 10^14.

        :param n: Positive integer to be factorized.
        :type n: ``int``
        :return: Dictionary of canonical prime factorization.
            Keys correspond to prime factors and values correspond to their multiplicity.
        :rtype: ``dict``
        """

    @abstractmethod
    def factorize_big(self, n: int) -> dict[int, int]:
        """Factorize positive integers greater than 10^14.

        :param n: Positive integer to be factorized.
        :type n: ``int``
        :return: Dictionary of canonical prime factorization.
            Keys correspond to prime factors and values correspond to their multiplicity.
        :rtype: ``dict``
        """

    def factorize(self, n) -> dict[int, int]:
        """Factorize positive integers not exceeding 10^70.

        :param n: Positive integer to be factorized.
        :type n: ``int``
        :return: Dictionary of canonical prime factorization.
            Keys correspond to prime factors and values correspond to their multiplicity.
        :rtype: ``dict``
        """

        if n < 1:
            raise ValueError("n must be a positive integer")

        if n == 1:
            return {1: 1}

        if np.greater_equal(n, 1e70):
            raise ValueError("n cannot be greater than 10^70")

        if np.greater_equal(n, 1e14):
            return self.factorize_big(n=n)
        return self.factorize_small(n=n)
