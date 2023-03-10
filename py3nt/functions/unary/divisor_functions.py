"""Divisor functions"""

from typing import Optional

import numpy as np

from py3nt.core.factorize import FactorizationFactory


def sigma_kth(n: int, k: int, factorizer: Optional[FactorizationFactory]) -> int:
    r"""Calculate the number of divisors.

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

    if factorizer:
        factorization = factorizer.factorize(n=n)

        if k == 0:
            return np.prod(a=np.array(list(factorization.values())) + 1)

        divisor_sigma = 1
        for prime, multiplicity in factorization.items():
            sum_from_prime = pow(prime, (multiplicity + 1) * k) - 1
            sum_from_prime = sum_from_prime // (pow(prime, k) - 1)

            divisor_sigma *= sum_from_prime

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
