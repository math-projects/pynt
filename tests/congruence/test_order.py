"""Test order/primitive root functions"""

import pytest

from py3nt.congruence.primitives import (
    least_primitive_root_modulo_prime,
    order_modulo_n,
    primitive_root_modulo_n,
)
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


def test_primitive_root_modulo_prime() -> None:
    """Test primitive root modulo prime"""

    factorizer = FactorizationFactory(N=1000)
    assert least_primitive_root_modulo_prime(p=5, factorizer=factorizer) == 2
    assert least_primitive_root_modulo_prime(p=11, factorizer=factorizer) == 2
    assert least_primitive_root_modulo_prime(p=23, factorizer=factorizer) == 5
    assert least_primitive_root_modulo_prime(p=31, factorizer=factorizer) == 3


def test_primitive_root_modulo_n() -> None:
    """Test primitive root modulo n"""

    factorizer = FactorizationFactory(N=1000)

    assert primitive_root_modulo_n(n=9, factorizer=factorizer) in [2, 5]
    assert primitive_root_modulo_n(n=10, factorizer=factorizer) in [3, 7]
    assert primitive_root_modulo_n(n=14, factorizer=factorizer) in [3, 5]
    assert primitive_root_modulo_n(n=18, factorizer=factorizer) in [5, 11]
    assert primitive_root_modulo_n(n=25, factorizer=factorizer) in [
        2,
        3,
        8,
        12,
        13,
        17,
        22,
        23,
    ]
    assert primitive_root_modulo_n(n=26, factorizer=factorizer) in [7, 11, 15, 19]
    assert primitive_root_modulo_n(n=27, factorizer=factorizer) in [2, 5, 11, 14, 20, 23]
