"""Test totient functions"""

import pytest

from py3nt.core.factorize import FactorizationFactory
from py3nt.functions.unary.totient import carmichael, jordan


def test_totient() -> None:
    """Test Jordan function."""

    factorizer = FactorizationFactory(N=1000)
    assert jordan(n=6, k=1, factorizer=factorizer) == 2
    assert jordan(n=9, k=2, factorizer=factorizer) == 72
    assert jordan(n=10, k=2, factorizer=factorizer) == 72
    assert jordan(n=4, k=3, factorizer=factorizer) == 56
    assert jordan(n=5, k=5, factorizer=factorizer) == 3124

    with pytest.raises(ValueError):
        jordan(n=6, k=1, factorizer=None)

    with pytest.raises(ValueError):
        jordan(n=0, k=0, factorizer=None)


def test_carmichael() -> None:
    """Test Carmichael's function"""

    factorizer = FactorizationFactory(N=1000)
    assert carmichael(n=4, factorizer=factorizer) == 1
    assert carmichael(n=12, factorizer=factorizer) == 2
    assert carmichael(n=21, factorizer=factorizer) == 6
    assert carmichael(n=35, factorizer=factorizer) == 12
    assert carmichael(n=36, factorizer=factorizer) == 6
    assert carmichael(n=36, factorization={3: 2, 2: 2}) == 6

    with pytest.raises(ValueError):
        carmichael(n=10, factorizer=None)

    with pytest.raises(ValueError):
        carmichael(n=0, factorizer=None)
