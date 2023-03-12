"""Test binomial functions"""


import pytest

from py3nt.polynomial.binomial import homogeneous_binomial


def test_homogeneous_binomial() -> None:
    """Test homogeneous_binomial calculation"""

    assert homogeneous_binomial(a=2, b=1, n=10) == 1023
    assert homogeneous_binomial(a=3, b=2, n=5) == 211
    assert homogeneous_binomial(a=5, b=3, n=5) == 1441

    with pytest.raises(ValueError):
        homogeneous_binomial(a=1, b=1, n=100)
