"""Divisor functions"""

from typing import Optional

import numpy as np

from py3nt.core.factorize import FactorizationFactory
from py3nt.polynomial.binomial import homogeneous_binomial


def sigma_kth(
    n: int,
    k: int,
    factorizer: Optional[FactorizationFactory],
    factorization: Optional[dict[int, int]] = None,
) -> int:
    r"""Calculate the divisor sum function :math:`\sigma_{k}(n)=\sum_{d\mid n}d^{k}`.

    Parameters
    ----------
    n : ``int``
        A positive integer.
    k: ``int``
        A positive integer.
    factorizer : ``FactorizationFactory``
        If a factorizer object is provided, then it is used to factorize :math:`n` first.
        The prime factorization is used to calculate the divisor sum.
        Otherwise all positive integers not exceeding :math:`n` are checked.

    Returns
    -------
    ``int``
        Divisor sigma function :math:`\sum_{d\mid n}d^{k}`.
    """

    if not factorization:
        if factorizer:
            factorization = factorizer.factorize(n=n)

    if factorization:
        if k == 0:
            return np.prod(a=np.array(list(factorization.values())) + 1)

        divisor_sigma = 1
        for prime, multiplicity in factorization.items():
            divisor_sigma *= homogeneous_binomial(a=pow(prime, k), b=1, n=multiplicity + 1)

        return divisor_sigma

    root = int(np.floor(np.sqrt(n * 1.0)))

    divisor_sigma = 0
    for i in range(1, root + 1):
        if (n % i) == 0:
            divisor_sigma += pow(i, k)
            j = n // i
            if i != j:
                divisor_sigma += pow(j, k)

    return divisor_sigma


def number_of_divisors(
    n: int,
    factorizer: Optional[FactorizationFactory],
    factorization: Optional[dict[int, int]] = None,
) -> int:
    """

    Parameters
    ----------
    n : ``int``
        A positive integer.
    factorizer : ``FactorizationFactory``
        If a factorizer object is provided, then it is used to factorize :math:`n` first.
        The prime factorization is used to calculate the divisor sum.
        Otherwise all positive integers not exceeding :math:`n` are checked.

    Returns
    -------
    ``int``
        Number of divisors of :math:`n`.
    """

    return sigma_kth(n=n, k=0, factorizer=factorizer, factorization=factorization)


def sum_of_divisors(
    n: int,
    factorizer: Optional[FactorizationFactory],
    factorization: Optional[dict[int, int]] = None,
) -> int:
    """

    Parameters
    ----------
    n : ``int``
        A positive integer.
    factorizer : ``FactorizationFactory``
        If a factorizer object is provided, then it is used to factorize :math:`n` first.
        The prime factorization is used to calculate the divisor sum.
        Otherwise all positive integers not exceeding :math:`n` are checked.

    Returns
    -------
    ``int``
        Sum of divisors of :math:`n`.
    """

    return sigma_kth(n=n, k=1, factorizer=factorizer, factorization=factorization)
