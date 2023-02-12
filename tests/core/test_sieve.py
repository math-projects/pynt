"""Test sieve"""

from pynt.core.sieve import SieveOfEratosthenes


def test_sieve_normal():
    """Test normal prime generation"""

    sieve = SieveOfEratosthenes(size=1)
    sieve.generate_primes()

    assert isinstance(sieve.primes_, list)
    assert len(sieve.primes_) == 0

    sieve = SieveOfEratosthenes(size=10)
    sieve.generate_primes()

    primes = sieve.primes_

    assert isinstance(primes, list)
    assert primes == [2, 3, 5, 7]

    sieve = SieveOfEratosthenes(size=100)
    sieve.generate_primes()
    primes = sieve.primes_

    assert len(primes) == 25


def test_sieve_smallest_factor():
    """Test prime generation using smallest factor sieve"""

    sieve = SieveOfEratosthenes(size=1)
    sieve.generate_smallest_prime_factors()

    assert isinstance(sieve.smallest_factors_, list)
    assert len(sieve.smallest_factors_) == 0

    sieve = SieveOfEratosthenes(size=10)
    sieve.generate_smallest_prime_factors()

    primes = sieve.primes_

    assert isinstance(primes, list)
    assert isinstance(primes, list)
    assert primes == [2, 3, 5, 7]

    sieve = SieveOfEratosthenes(size=100)
    sieve.generate_smallest_prime_factors()
    primes = sieve.primes_

    assert len(primes) == 25

    assert isinstance(sieve.smallest_factors_, list)
    assert len(sieve.smallest_factors_) == 100
    assert sieve.smallest_factors_[45] == 3
