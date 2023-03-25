"""Test order/primitive root functions"""

import pytest

from py3nt.congruence.primitives import order_modulo_n
from py3nt.core.factorize import FactorizationFactory


def test_order() -> None:
    """Test order modulo n"""

    factorizer = FactorizationFactory(N=10000)
    with pytest.raises(ValueError):
        order_modulo_n(a=12, n=10, factorizer=factorizer)
    assert order_modulo_n(a=12, n=13, factorizer=factorizer) == 2
    assert order_modulo_n(a=2, n=7, factorizer=factorizer) == 3
    assert order_modulo_n(a=5, n=16, factorizer=factorizer) == 4
    assert order_modulo_n(a=3, n=13, factorizer=factorizer) == 3
    assert order_modulo_n(a=3, n=14, factorizer=factorizer) == 6
    assert order_modulo_n(a=597, n=1001, factorizer=factorizer) == 30
    assert order_modulo_n(a=12, n=169, factorizer=factorizer) == 26
