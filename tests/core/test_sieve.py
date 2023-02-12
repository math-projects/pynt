"""Test sieve"""

from pynt.core.sieve import SieveOfEratosthenes


def test_sieve_normal():
    """Test normal prime generation"""

    sieve = SieveOfEratosthenes(size=10)
    sieve.generate_primes()

    primes = sieve.primes_

    assert isinstance(primes, list)
    assert primes == [2, 3, 5, 7]

    sieve = SieveOfEratosthenes(size=100)
    sieve.generate_primes()
    primes = sieve.primes_

    assert len(primes) == 25
