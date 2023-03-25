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


def generate_divisors(
    n: int,
    factorizer: Optional[FactorizationFactory] = None,
    factorization: Optional[dict[int, int]] = None,
) -> np.ndarray:
    r"""Generate all positive divisors of a positive integer.

    Parameters
    ----------
    n : ``int``
        A positive integer.
    factorizer : ``Optional[FactorizationFactory], optional``
        If specified, ``factorizer`` is used to factorize :math:`n`, by default ``None``.
    factorization : ``Optional[dict[int, int]]``, optional
        If specified, used as prime factorization of :math:`n`, by default ``None``.
        Cannot be ``None`` if ``factorizer`` is also ``None``.

    Returns
    -------
    ``np.ndarray``
        An unsorted numpy array of divisors: :math:`{d\in\mathbb{N}:d\mid n}`.

    Raises
    ------
    ``ValueError``
        If both ``factorizer`` and ``factorizer`` are ``None``.
    """

    if not factorization:
        if not factorizer:
            raise ValueError("`factorizer` cannot be None")

        factorization = factorizer.factorize(n=n)

    divisors = np.empty(
        shape=(number_of_divisors(n=n, factorization=factorization, factorizer=None)),
        dtype=int,
    )

    tau = 1
    divisors[0] = 1

    for prime, multiplicity in factorization.items():
        cur = 1
        tau_tmp = tau

        for _ in range(multiplicity):
            cur *= prime

            for i in range(tau_tmp):
                divisors[tau] = divisors[i] * cur
                tau += 1

    return divisors
