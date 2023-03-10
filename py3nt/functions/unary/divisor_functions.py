"""Divisor functions"""

import numpy as np

from py3nt.core.factorize import FactorizationFactory


def number_of_divisor(n: int, factorizer: FactorizationFactory) -> int:
    """Calculate the number of divisors.

    Parameters
    ----------
    n : ``int``
        A positive integer.
    factorizer : ``FactorizationFactory``
        If a factorizer class is provided, then it is used to factorize :math:`n` first.
        The canonical prime factorization is used to calculate the number of divisors.
        Otherwise all numbers not exceeding :math:`n` are checked.

    Returns
    -------
    ``int``
        Number of divisors of :math:`n`.
    """

    if factorizer:
        factorization = factorizer.factorize(n=n)
        multiplicities = [multiplicity for _, multiplicity in factorization.items()]

        return np.prod(np.array(multiplicities) + 1)

    root = int(np.floor(np.sqrt(n * 1.0)))

    num_divisors = 0
    for i in range(1, root):
        if (n % i) == 0:
            num_divisors += 2

    if root * root == n:
        num_divisors += 1

    return num_divisors
