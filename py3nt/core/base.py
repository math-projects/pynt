"""Base classes"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

import numpy as np
from sympy.ntheory import primepi

from py3nt.defaults import LARGEST_SMALL_NUMBER


@dataclass
class BaseSieve(ABC):
    """
    Abstract base class for sieve.

    Methods
    -------
    generate_primes:
        Generate primes when size is small.
    """

    limit: int
    primes_: np.ndarray = field(init=False)
    num_primes: int = field(default=0)

    def __post_init__(self) -> None:
        self.num_primes = primepi(self.limit)
        self.primes_ = np.empty(shape=(self.num_primes,), dtype=int)

    @abstractmethod
    def generate_primes(self) -> None:
        """Generate primes when size is small."""


@dataclass
class BaseFactorization(ABC):
    """
    Abstract base class for factorization.

    Methods
    -------
    factorize:
        Factorize a positive integer.
    """

    @abstractmethod
    def factorize(self, n) -> dict[int, int]:
        """Factorize positive integers not exceeding 10^70.

        :param n: Positive integer to be factorized.
        :type n: ``int``
        :return: Dictionary of canonical prime factorization.
            Keys correspond to prime factors and values correspond to their multiplicity.
        :rtype: ``dict``
        """


@dataclass
class BaseSieveFactorization(BaseFactorization):
    """
    Base Factorization class with sieve.

    Methods
    -------
    regenerate_primes:
        Generate primes if necessary.
    """

    sieve: BaseSieve
    largest_small_number: int = field(default=LARGEST_SMALL_NUMBER)

    def regenerate_primes(self) -> None:
        """Generate primes if necessary."""

        self.sieve.generate_primes()
