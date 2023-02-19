"""Test sieve"""

import numpy as np

from py3nt.core.sieve import SieveOfEratosthenes, SieveOfEratosthenesOptimized


def test_sieve_normal():
    """Test normal prime generation"""

    sieve = SieveOfEratosthenes(limit=1)
    sieve.generate_primes()

    assert isinstance(sieve.primes_, np.ndarray)
    assert sieve.num_primes == 0
    assert sieve.max_prime_count == 0

    sieve = SieveOfEratosthenes(limit=10)
    sieve.generate_primes()

    primes = sieve.primes_

    assert isinstance(primes, np.ndarray)
    assert sieve.num_primes == 4
    assert primes.tolist() == [2, 3, 5, 7]

    sieve = SieveOfEratosthenes(limit=100)
    sieve.generate_primes()
    primes = sieve.primes_

    assert len(primes) == 25


def test_sieve_optimized():
    """Test smallest prime factor sieve"""

    sieve = SieveOfEratosthenesOptimized(limit=1)
    sieve.generate_primes()

    assert isinstance(sieve.primes_, np.ndarray)
    assert sieve.num_primes == 0

    sieve = SieveOfEratosthenesOptimized(limit=100)
    sieve.generate_primes()

    assert isinstance(sieve.primes_, np.ndarray)
    assert sieve.num_primes == 25

    assert hasattr(sieve, "smallest_factors_")
    smallest_factors = getattr(sieve, "smallest_factors_")

    assert isinstance(smallest_factors, np.ndarray)
    assert smallest_factors.shape[0] == 100 + 1
    assert smallest_factors[45] == 3
