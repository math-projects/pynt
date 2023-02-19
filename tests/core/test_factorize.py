"""Test positive integer factorization"""


import pytest

from py3nt.core.factorize import BaseFactorizer, Factorizer
from py3nt.core.sieve import SieveOfEratosthenes, SieveOfEratosthenesOptimized


class TestFactorizer:
    """Test Factorizer class"""

    def test_factorize_invalid(self) -> None:
        """Test factorize invalid cases"""

        factorizer = Factorizer()

        with pytest.raises(ValueError):
            factorizer.factorize(n=0)

        factorization = factorizer.factorize(n=1)
        assert 1 in factorization
        assert factorization[1] == 1

        with pytest.raises(ValueError):
            factorizer.factorize(n=int(1e80))

    def test_factorize_with_sieve_logn(self) -> None:
        """Test logn factorization"""

        sieve = SieveOfEratosthenesOptimized(limit=10)
        sieve.generate_primes()

        assert hasattr(sieve, "smallest_factors_")

        factorizer = Factorizer(sieve=sieve)

        assert isinstance(factorizer, BaseFactorizer)

        factorization = factorizer.factorize(10)

        assert isinstance(factorization, dict)
        assert (2 in factorization) and (5 in factorization)
        assert factorization[2] == 1 and factorization[5] == 1

    def test_factorize_with_sieve_small(self) -> None:
        """Test factorization of small numbers with sieve"""

        sieve = SieveOfEratosthenes(limit=int(1e7 + 100))
        sieve.generate_primes()

        factorizer = Factorizer(sieve=sieve)

        assert isinstance(factorizer, BaseFactorizer)

        factorization = factorizer.factorize(n=int(1e7 + 5))

        assert isinstance(factorization, dict)
        assert 5 in factorization

    def test_factorize_without_sieve_small(self) -> None:
        """Test factorization of small numbers without sieve"""

        factorizer = Factorizer()

        assert isinstance(factorizer, BaseFactorizer)

        factorization = factorizer.factorize(n=111)
        assert isinstance(factorization, dict)

        assert 3 in factorization and 37 in factorization
        assert factorization[3] == 1 and factorization[37] == 1

        factorization = factorizer.factorize(n=20)
        assert isinstance(factorization, dict)

        assert 2 in factorization and 5 in factorization
        assert factorization[2] == 2 and factorization[5] == 1

    def test_factorize_big(self) -> None:
        """Test factorization of large numbers"""

        factorizer = Factorizer()
        factorization = factorizer.factorize(n=int(1e15))
        assert isinstance(factorization, dict)
