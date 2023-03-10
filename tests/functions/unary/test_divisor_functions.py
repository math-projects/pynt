"""Test divisor functions"""


import numpy as np
from sympy.ntheory import divisor_count, divisor_sigma

from py3nt.core.factorize import FactorizationFactory
from py3nt.functions.unary.divisor_functions import sigma_kth


def test_number_of_divisors() -> None:
    """Test number of divisor function"""

    for n in np.random.randint(low=1, high=100000, size=100):
        assert sigma_kth(n=n, k=0, factorizer=None) == divisor_count(n=n)

    factorizer = FactorizationFactory(N=100000000, with_sieve=False)
    for n in np.random.randint(low=1, high=100000000, size=50):
        assert sigma_kth(n=n, k=0, factorizer=factorizer) == divisor_count(n=n)

    factorizer = FactorizationFactory(N=1000000)
    for n in np.random.randint(low=1, high=1000000, size=50):
        assert sigma_kth(n=n, k=0, factorizer=factorizer) == divisor_count(n=n)

    factorizer = FactorizationFactory(N=10000000000, with_sieve=True)
    for n in np.random.randint(low=1, high=10000000000, size=50):
        assert sigma_kth(n=n, k=0, factorizer=factorizer) == divisor_count(n=n)


def test_divisor_sigma() -> None:
    """Test divisor summation function"""

    factorizer = FactorizationFactory(N=10000)
    for n in np.random.randint(low=1, high=10000, size=100):
        for k in np.random.randint(low=0, high=3, size=50):
            assert sigma_kth(n=n, k=k, factorizer=factorizer) == divisor_sigma(n, k)
            assert sigma_kth(n=n, k=k, factorizer=None) == divisor_sigma(n, k)
