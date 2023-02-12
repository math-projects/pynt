"""Test primality"""

from pynt.core.primality_test import is_prime_naive


def test_primality_naive(primes_small: list, composites_small: list):
    assert is_prime_naive(1) is False
    assert is_prime_naive(2) is True
    assert is_prime_naive(3) is True

    for prime in primes_small:
        assert is_prime_naive(prime) is True

    for composite in composites_small:
        assert is_prime_naive(composite) is False
