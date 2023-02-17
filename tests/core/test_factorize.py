"""Test positive integer factorization"""

from py3nt.core.factorize import BaseFactorizer, Factorizer
from py3nt.core.sieve import SieveOfEratosthenes


class TestFactorizer:
    """Test Factorizer class"""

    def test_factorize_with_sieve_logn(self) -> None:
        """Test logn factorization"""

        sieve = SieveOfEratosthenes(size=10)

        factorizer = Factorizer(sieve=sieve)

        assert isinstance(factorizer, BaseFactorizer)

        factorization = factorizer.factorize_small(10)

        assert isinstance(factorization, dict)
        assert (2 in factorization) and (5 in factorization)
        assert factorization[2] == 1 and factorization[5] == 1

    def test_factorize_with_sieve_small(self) -> None:
        """Test factorization of small numbers with sieve"""

        sieve = SieveOfEratosthenes(size=int(1e7 + 100))

        factorizer = Factorizer(sieve=sieve)

        assert isinstance(factorizer, BaseFactorizer)

        factorization = factorizer.factorize_small(n=int(1e7 + 5))

        assert isinstance(factorization, dict)
        assert 5 in factorization

    def test_factorize_without_sieve_small(self) -> None:
        """Test factorization of small numbers without sieve"""

        factorizer = Factorizer(sieve=None)

        assert isinstance(factorizer, BaseFactorizer)

        factorization = factorizer.factorize_small(n=111)
        assert isinstance(factorization, dict)

        assert 3 in factorization and 37 in factorization
        assert factorization[3] == 1 and factorization[37] == 1

        factorization = factorizer.factorize_small(n=20)
        assert isinstance(factorization, dict)

        assert 2 in factorization and 5 in factorization
        assert factorization[2] == 2 and factorization[5] == 1
