"""Test Integer"""

import numpy as np

from py3nt.numbers.integer import Integer


def test_integer():
    """Test Integer class"""

    twelve = Integer(12)

    assert twelve == 12

    for m in np.random.randint(1, 100, size=100):
        n = np.random.randint(1, 100)
        M = Integer(m)
        assert M * n == m * n
        modulo = np.random.randint(5, 10)
        assert M.multiply_modular(other=n, modulus=modulo) == (m * n) % modulo

        assert pow(M, n, modulo) == pow(int(m), int(n), int(modulo))

    assert pow(Integer(-12), 2, 100) == 44
    assert Integer(-12).multiply_modular(other=-12, modulus=100) == 44
