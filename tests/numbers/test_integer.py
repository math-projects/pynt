"""Test Integer"""

import random

import numpy as np
import pytest

from py3nt.numbers.integer import Integer


class TestInteger:
    """Test Integer class"""

    def test_integer_multiplication_exponentiation(self) -> None:
        """Test Integer.multiply_modular and pow(a, b, m)"""

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
        assert pow(Integer(-13), 2) == 169

    def test_pollard_rho_factor(self) -> None:
        """Test Pollard's rho factorization"""

        assert Integer(100).pollard_rho_factor(a=2, c=1) == 2

        with pytest.raises(ValueError):
            Integer((1 << 32) + 1).pollard_rho_factor(a=2, c=1)

        n = (1 << 50) + 1
        factor = Integer(n).pollard_rho_factor(a=2, c=1, max_iter=5)
        assert factor > 1
        assert (n % factor) == 0

        n = (1 << 64) + 1
        factor = Integer(n).pollard_rho_factor(a=2, c=1, max_iter=5)
        assert factor == 1

    def test_brent_pollard_rho(self) -> None:
        """Test Brent-Pollard's rho factorization"""

        assert Integer(1 << 40).brent_pollard_rho_factor() == 2

        with pytest.raises(ValueError):
            Integer((1 << 32) + 1).brent_pollard_rho_factor()

        for _ in range(5):
            n = random.randint((1 << 50), (1 << 60))
            factor = Integer(n).brent_pollard_rho_factor(max_iter=10)
            assert factor > 1
            assert (n % factor) == 0
