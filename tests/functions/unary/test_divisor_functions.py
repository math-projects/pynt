"""Test divisor functions"""

import numpy as np
import pytest
from sympy.ntheory import divisor_count, divisor_sigma

from py3nt.core.factorize import FactorizationFactory
from py3nt.functions.unary.divisor_functions import (
    generate_divisors,
    number_of_divisors,
    sigma_kth,
    sum_of_divisors,
)


def test_number_of_divisors() -> None:
    """Test number of divisor function"""

    for n in np.random.randint(low=1, high=100000, size=100):
        assert number_of_divisors(n=n, factorizer=None) == divisor_count(n=n)

    factorizer = FactorizationFactory(N=100000000, with_sieve=False)
    for n in np.random.randint(low=1, high=100000000, size=50):
        assert number_of_divisors(n=n, factorizer=factorizer) == divisor_count(n=n)

    factorizer = FactorizationFactory(N=1000000)
    for n in np.random.randint(low=1, high=1000000, size=50):
        assert number_of_divisors(n=n, factorizer=factorizer) == divisor_count(n=n)

    factorizer = FactorizationFactory(N=10000000000, with_sieve=True)
    for n in np.random.randint(low=1, high=10000000000, size=50):
        assert number_of_divisors(n=n, factorizer=factorizer) == divisor_count(n=n)


def test_sum_of_divisors() -> None:
    """Test number of divisor function"""

    for n in np.random.randint(low=1, high=100000, size=100):
        assert sum_of_divisors(n=n, factorizer=None) == divisor_sigma(n, 1)

    factorizer = FactorizationFactory(N=100000000, with_sieve=False)
    for n in np.random.randint(low=1, high=100000000, size=50):
        assert sum_of_divisors(n=n, factorizer=factorizer) == divisor_sigma(n, 1)

    factorizer = FactorizationFactory(N=1000000)
    for n in np.random.randint(low=1, high=1000000, size=50):
        assert sum_of_divisors(n=n, factorizer=factorizer) == divisor_sigma(n, 1)

    factorizer = FactorizationFactory(N=10000000000)
    for n in np.random.randint(low=1, high=10000000000, size=50):
        assert sum_of_divisors(n=n, factorizer=factorizer) == divisor_sigma(n, 1)


def test_divisor_sigma() -> None:
    """Test divisor summation function"""

    factorizer = FactorizationFactory(N=10000)
    for n in np.random.randint(low=1, high=10000, size=10):
        for k in np.random.randint(low=0, high=5, size=10):
            assert sigma_kth(n=n, k=k, factorizer=factorizer) == divisor_sigma(n, k)
            assert sigma_kth(n=n, k=k, factorizer=None) == divisor_sigma(n, k)


def test_generate_divisors() -> None:
    """Test divisor generation."""

    with pytest.raises(ValueError):
        generate_divisors(n=12)

    divisors = generate_divisors(n=12, factorizer=None, factorization={2: 2, 3: 1})

    assert len(divisors) == 6
    for divisor in divisors:
        assert 12 % divisor == 0

    factorizer = FactorizationFactory(N=1000)
    for n in np.random.randint(low=1, high=1000, size=100):
        divisors = generate_divisors(n=n, factorizer=factorizer)
        assert len(divisors) == number_of_divisors(n=n, factorizer=factorizer)
        for divisor in divisors:
            assert n % divisor == 0
