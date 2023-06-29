"""Totient functions"""

from typing import Optional

import numpy as np

from py3nt.core.factorize import FactorizationFactory


def jordan(
    n: int,
    k: int,
    factorizer: Optional[FactorizationFactory] = None,
    factorization: Optional[dict[int, int]] = None,
) -> int:
    r"""Calculate Jordan's Totient function of :math:`n`:
    The number of positive integer tuples :math:`(a_{1},\ldots,a_{k})`
    not exceeding :math:`n`.
    A generation of Euler's Totient function.

    .. math::
        J_{k}(n) = n^{k}\prod_{p\mid n}\left(1-\dfrac{1}{p^{k}}\right)\\
        \varphi(n) = J_{1}(n)

    Parameters
    ----------
    n : ``int``
        A positive integer.
    k : ``int``
        A positive integer.
    factorizer : ``Optional[FactorizationFactory]``
        If a factorizer object is provided, then it is used to factorize :math:`n` first.
        The prime factorization is used to calculate the value.
    factorization: ``Optional[dict]``
        A dictionary of prime factorization.
        Keys must be primes.
        Values must be the corresponding multiplicities.

    Returns
    -------
    ``int``
        :math:`J_{k}(n)`.

    Raises
    ------
    ``ValueError``
        If both ``factorizer`` and ``factorization`` are none.
    """

    if n < 1 or k < 1:
        raise ValueError("`n` or `k` must be a positive integer.")

    if not factorization:
        if not factorizer:
            raise ValueError("`factorizer` cannot be None")

        factorization = factorizer.factorize(n=n)

    phi = pow(n, k)

    for prime in factorization:
        p_k = pow(prime, k)
        phi //= p_k
        phi *= p_k - 1

    return phi


def carmichael(
    n: int,
    factorizer: Optional[FactorizationFactory] = None,
    factorization: Optional[dict[int, int]] = None,
) -> int:
    r"""Carmichael function :math:`\lambda(n)`.
    Also known as the universal exponent :math:`\pmod{n}`.
    Calculated using the prime factorization of :math:`n=p_{1}^{e_{1}}\cdots p_{k}^{e_{k}}`

    .. math::
        \lambda(2^{k+2}) = 2^{k}\\
        \lambda(p^{k}) = p^{k-1}(p-1)\\
        \lambda(ab) = \mbox{lcm}(\lambda(a), \lambda(b))

    if :math:`p` is an odd prime and :math:`\gcd(a,b)=1`.
    Use this on the prime factorization.

    Parameters
    ----------
    n : ``int``
        A positive integer.
    factorizer : Optional[FactorizationFactory]
        If a factorizer object is provided, then it is used to factorize :math:`n` first.
        The prime factorization is used to calculate the value.
    factorization: ``Optional[dict]``
        A dictionary of prime factorization.
        Keys must be primes.
        Values must be the corresponding multiplicities.

    Returns
    -------
    ``int``
        :math:`\lambda(n)`.

    Raises
    ------
    ValueError
        If :math:`n` is not positive or both `factorization` and `factorizer` are `None`.
    """

    if n < 1:
        raise ValueError("`n` must be a positive integer.")

    if not factorization:
        if not factorizer:
            raise ValueError("`factorizer` cannot be None")

        factorization = factorizer.factorize(n=n)

    universal_exponent = 1

    if (n & 1) == 0:
        multiplicity = 0
        while (n & 1) == 0:
            n >>= 1
            multiplicity += 1

        if multiplicity > 1:
            universal_exponent *= 1 << (multiplicity - 2)

    if n == 1:
        return universal_exponent

    for prime, multiplicity in factorization.items():
        universal_exponent = np.lcm(universal_exponent, pow(prime, multiplicity - 1))
        universal_exponent = np.lcm(universal_exponent, prime - 1)

    return universal_exponent
