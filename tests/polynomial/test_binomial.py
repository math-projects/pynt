"""Test binomial functions"""


import pytest

from py3nt.polynomial.binomial import (
    binomial_coefficient,
    generate_binomial_coefficients,
    homogeneous_binomial,
)


def test_homogeneous_binomial() -> None:
    """Test homogeneous_binomial calculation"""

    assert homogeneous_binomial(a=2, b=1, n=10) == 1023
    assert homogeneous_binomial(a=3, b=2, n=5) == 211
    assert homogeneous_binomial(a=5, b=3, n=5) == 1441
    assert homogeneous_binomial(a=100, b=91, n=1) == 1

    with pytest.raises(ValueError):
        homogeneous_binomial(a=1, b=1, n=100)

    with pytest.raises(ValueError):
        homogeneous_binomial(a=2, b=1, n=0)


def test_binomial_coefficient() -> None:
    """Test Binomial Coefficient"""

    assert binomial_coefficient(n=10, k=5) == 252
    assert binomial_coefficient(n=4, k=10) == 0
    assert binomial_coefficient(n=100, k=0) == 1
    assert binomial_coefficient(n=7, k=2) == 21

    with pytest.raises(ValueError):
        binomial_coefficient(n=-1, k=10)


def test_generate_binomial_coefficient() -> None:
    """Test binomial coefficient generation"""

    nCk = generate_binomial_coefficients(n=10)

    assert nCk[0, 0] == 1
    assert nCk[1][0] == 1
    assert nCk[1][1] == 1
    assert nCk[1][10] == 0
    assert nCk[10][4] == 210
    assert nCk[10, 5] == 252
    assert nCk[10, 10] == 1
