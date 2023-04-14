"""Test binomial congruence"""

import pytest

from py3nt.congruence.binomial import (
    binomial_modulo_small_prime,
    small_binomial_modulo_prime,
)


def test_small_binomial_modulo_prime() -> None:
    """Test small binomial coefficients"""

    assert small_binomial_modulo_prime(n=10, k=4, p=7) == 0
    assert small_binomial_modulo_prime(n=10, k=4, p=13) == 2

    with pytest.raises(ValueError):
        small_binomial_modulo_prime(n=-1, k=-11, p=3)


def test_binomail_modulo_small_prime() -> None:
    """Test binomial coefficients modulo small primes"""

    assert binomial_modulo_small_prime(n=10, k=4, p=3) == 0
    assert binomial_modulo_small_prime(n=20, k=0, p=3) == 1
    assert binomial_modulo_small_prime(n=0, k=0, p=7) == 1
    assert binomial_modulo_small_prime(n=5, k=10, p=13) == 0
    assert binomial_modulo_small_prime(n=67, k=10, p=7) == 1
