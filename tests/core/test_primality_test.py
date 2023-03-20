"""Test primality"""

import pytest

from py3nt.core.primality_test import is_prime_naive, miller_rabin, solovay_strassen


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


def test_primality_mr(primes_small: list, composites_small: list, primes_large: list):
    """Test primality using Miller Rabin"""

    for prime in primes_small:
        assert miller_rabin(n=prime) is True

    for composite in composites_small:
        assert miller_rabin(n=composite) is False

    for prime in primes_large:
        assert miller_rabin(n=prime) is True


def test_solovay_strassen(primes_large: list):
    """Test primality using Solovay Strassen"""

    assert solovay_strassen(n=2) is True
    assert solovay_strassen(n=1) is False
    assert solovay_strassen(n=4) is False

    for prime in primes_large:
        assert solovay_strassen(n=prime, max_iter=10) is True
