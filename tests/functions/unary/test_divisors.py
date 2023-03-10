"""Test divisor functions"""


import numpy as np
from sympy.ntheory import divisor_count

from py3nt.core.factorize import FactorizationFactory
from py3nt.functions.unary.divisor_functions import number_of_divisor


def test_number_of_divisors():
    """Test number of divisor function"""

    for n in np.random.randint(low=1, high=100000, size=100):
        assert number_of_divisor(n=n, factorizer=None) == divisor_count(n=n)

    factorizer = FactorizationFactory(N=100000000, with_sieve=False)
    for n in np.random.randint(low=1, high=100000000, size=50):
        assert number_of_divisor(n=n, factorizer=factorizer) == divisor_count(n=n)

    factorizer = FactorizationFactory(N=1000000)
    for n in np.random.randint(low=1, high=1000000, size=50):
        assert number_of_divisor(n=n, factorizer=factorizer) == divisor_count(n=n)

    factorizer = FactorizationFactory(N=10000000000, with_sieve=True)
    for n in np.random.randint(low=1, high=10000000000, size=50):
        assert number_of_divisor(n=n, factorizer=factorizer) == divisor_count(n=n)
