"""Test basic functions in modular arithmetic"""

import numpy as np
import pytest

from py3nt.congruence.basics import (
    chinese_remainder_theorem,
    extended_euclidean,
    inverse,
)


def test_extended_euclidean() -> None:
    """Test extended euclidean algorithm"""

    assert extended_euclidean(a=10, b=0) == (1, 0, 10)

    for _ in range(100):
        a = np.random.randint(low=-1000, high=1000)
        b = np.random.randint(low=-1000, high=1000)
        x, y, g = extended_euclidean(a=a, b=b)
        assert np.gcd(a, b) == abs(g)
        assert a * x + b * y == g


def test_inverse() -> None:
    """Test modular inverse"""

    assert inverse(a=3, n=11, is_prime=True) == 4

    with pytest.raises(ValueError):
        assert inverse(a=100, n=10)

    for _ in range(100):
        a = np.random.randint(low=-1000, high=1000)
        b = np.random.randint(low=-100, high=1000)

        if np.gcd(a, b) > 1:
            with pytest.raises(ValueError):
                inverse(a=a, n=b)

        else:
            if b <= 1:
                with pytest.raises(ValueError):
                    inverse(a=a, n=b)
            else:
                x = inverse(a=a, n=b)
                assert a * x % b == 1


def test_chinese_remainder_theorem() -> None:
    """Test Chinese Remainder Theorem"""

    with pytest.raises(ValueError):
        chinese_remainder_theorem(r=[2, 3], m=[4, 6])

    with pytest.raises(ValueError):
        chinese_remainder_theorem(r=[2], m=[])

    with pytest.raises(ValueError):
        chinese_remainder_theorem(r=[2], m=[2])

    assert chinese_remainder_theorem(r=[2, 3], m=[3, 5]) == 8
    assert chinese_remainder_theorem(r=[2, 3, 2], m=[3, 5, 7]) == 23
    assert chinese_remainder_theorem(r=[0, 2, 1], m=[5, 7, 11]) == 100
