"""Test primality"""

import pytest

from py3nt.core.primality_test import is_prime_naive


def test_primality_naive(primes_small: list, composites_small: list):
    """Test primality using naive approach"""

    with pytest.raises(ValueError):
        is_prime_naive(-1)

    assert is_prime_naive(1) is False
    assert is_prime_naive(2) is True
    assert is_prime_naive(3) is True

    for prime in primes_small:
        assert is_prime_naive(prime) is True

    for composite in composites_small:
        assert is_prime_naive(composite) is False
