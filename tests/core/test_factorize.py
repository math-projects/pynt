"""Test positive integer factorization"""


import pytest

from py3nt.core.factorize import FactorizationFactory
from py3nt.core.sieve import SieveOfEratosthenesOptimized


class TestFactorizer:
    """Test FactorizationFactory class"""

    def test_factorize_invalid(self) -> None:
        """Test factorize invalid cases"""

        factorizer = FactorizationFactory(N=100, with_sieve=False)

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

        assert hasattr(sieve, "largest_prime_factors_")

        factorizer = FactorizationFactory(N=20, with_sieve=True)

        assert isinstance(factorizer, FactorizationFactory)

        factorization = factorizer.factorize(10)

        assert isinstance(factorization, dict)
        assert (2 in factorization) and (5 in factorization)
        assert factorization[2] == 1 and factorization[5] == 1

    def test_factorize_with_sieve_small(self) -> None:
        """Test factorization of small numbers with sieve"""

        factorizer = FactorizationFactory(N=int(1e10))

        factorization = factorizer.factorize(n=int(1e2 + 5))

        assert isinstance(factorization, dict)
        assert 5 in factorization
        assert 3 in factorization
        assert 7 in factorization
        for key in factorization:
            assert factorization[key] == 1

        factorization = factorizer.factorize(n=37)
        assert factorization == {37: 1}

    def test_factorize_without_sieve_small(self) -> None:
        """Test factorization of small numbers without sieve"""

        factorizer = FactorizationFactory(N=200, with_sieve=False)

        assert isinstance(factorizer, FactorizationFactory)

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

        factorizer = FactorizationFactory(N=int(1e50))
        factorization = factorizer.factorize(n=int(1e15) + 1)
        assert isinstance(factorization, dict)
        assert 7 in factorization
        assert 13 in factorization
        assert 11 in factorization

        factorization = factorizer.factorize(n=(1 << 64) + 1)
        for prime in factorization:
            assert prime > 1

        factorization = factorizer.factorize(n=357479581)
        assert 61 in factorization

        assert factorizer.factorize(n=12) == {2: 2, 3: 1}

        factorizer = FactorizationFactory(N=int(1e70))
        with pytest.raises(ValueError):
            factorization = factorizer.factorize(n=int(1e80))
