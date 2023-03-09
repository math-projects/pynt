"""Test Legendre function"""


import pytest

from py3nt.congruence.quadratic import jacobi_symbol, legendre_symbol


def test_legendre() -> None:
    """Test Legendre symbol"""

    assert legendre_symbol(a=-1, p=5) == 1
    assert legendre_symbol(a=-1, p=3) == -1
    assert legendre_symbol(a=12, p=3) == 0


def test_jacobi() -> None:
    """Test Jacobi symbol"""

    assert jacobi_symbol(a=-1, n=5) == 1
    assert jacobi_symbol(a=-1, n=3) == -1
    assert jacobi_symbol(a=12, n=15) == 0
    assert jacobi_symbol(a=25, n=21) == 1
    assert jacobi_symbol(a=8, n=15) == 1

    with pytest.raises(ValueError):
        jacobi_symbol(a=10, n=-11)

    with pytest.raises(ValueError):
        jacobi_symbol(a=10, n=10)
