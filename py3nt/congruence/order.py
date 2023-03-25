"""Order/primitive root functions"""

from typing import Optional

from py3nt.core.factorize import FactorizationFactory


def order(
    a: int,
    n: int,
    factorizer: Optional[FactorizationFactory],
    factorization: Optional[dict[int, int]] = None,
) -> int:
    if not factorization:
        if factorizer:
            factorization = factorizer.factorize(n=n)
        else:
            raise ValueError("Both `factorizer` and `factorization` cannot be `None`.")
