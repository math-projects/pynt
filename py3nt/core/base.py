"""Base classes"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional

import numpy as np

from py3nt.defaults import DEFAULT_SIEVE_LIMIT, MAX_LOGN_FACTORIZATION_LIMIT


@dataclass
class BaseSieve(ABC):
    """Abstract base class for sieve"""

    size: int
    logn_limit: Optional[int] = field(default=DEFAULT_SIEVE_LIMIT)

    primes_: list = field(init=False)
    smallest_factors_: list = field(init=False)

    def __post_init__(self) -> None:
        self.clear()

        if not self.logn_limit:
            self.logn_limit = self.size

        if self.logn_limit and (self.logn_limit > MAX_LOGN_FACTORIZATION_LIMIT):
            raise ValueError(
                f"{self.logn_limit} is greater than {MAX_LOGN_FACTORIZATION_LIMIT}"
            )

    @abstractmethod
    def generate_primes(self) -> None:
        """Generate primes when size is small"""

    @abstractmethod
    def generate_smallest_prime_factors(self) -> None:
        """Generate smallest prime factors up to size."""

    def clear(self) -> None:
        """Reset to initial state."""

        self.primes_ = []
        self.smallest_factors_ = []


@dataclass
class BaseFactorizer(ABC):
    """Abstract base class for factorization"""

    sieve: Optional[BaseSieve]

    def factorize_logn(self, n: int) -> dict[int, int]:
        """Factorize a positive integer in logn complexity.

        :param n: Positive integer to factorize.
        :type n: ```int```
        :raises ValueError: If sieve is ``None``.
        :return: Dictionary of prime factor, multiplicity as key-value pairs.
        :rtype: ``dict``
        """

        if not self.sieve:
            raise ValueError("sieve cannot be empty")

        factorization: dict[int, int] = {}

        if len(self.sieve.smallest_factors_) < 1:
            self.sieve.generate_smallest_prime_factors()

        while n > 1:
            prime_factor = self.sieve.smallest_factors_[n]

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
