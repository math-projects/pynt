"""Congruence of binomial coefficients"""

from typing import Optional

import numpy as np

from py3nt.congruence.basics import inverse
from py3nt.numbers.integer import Integer


def small_binomial_modulo_prime(
    n: int,
    k: int,
    p: int,
    factorials: Optional[list[int] | np.ndarray] = None,
) -> int:
    r"""

    Parameters
    ----------
    n : ``int``
        An integer.
    k : ``int``
        An integer.
    p : ``int``
        A prime.
    factorials : ``Optional[list[int]  |  np.ndarray], optional``
        Array of precalculated factorials :math:`\pmod{p}`., by default ``None``

    Returns
    -------
    ``int``
        :math:`\binom{n}{k}\pmod{p}` when :math:`n,k< p`.

    Raises
    ------
    ``ValueError``
        If :math:`n` or :math:`k` is negative.
    """

    if n < 0 or k < 0:
        raise ValueError("`n` or `k` cannot be negative,")

    if not n and not k:
        return 1

    if not n:
        return 0

    if not k:
        return 1

    if n < k:
        return 0

    if not isinstance(factorials, np.ndarray) and not isinstance(factorials, list):
        factorials = np.empty(shape=(n + 1,), dtype=int)
        factorials[0] = 1
        for i in range(1, n + 1):
            factorials[i] = Integer(i).multiply_modular(other=factorials[i - 1], modulus=p)

    rem = Integer(factorials[n]).multiply_modular(
        other=inverse(a=factorials[k], n=p, is_prime=True), modulus=p
    )
    rem = Integer(rem).multiply_modular(
        other=inverse(a=factorials[n - k], n=p, is_prime=True), modulus=p
    )

    return rem


def binomial_modulo_small_prime(n: int, k: int, p: int) -> int:
    r"""
    Uses Lucas theorem to calculate binomial coefficients modulo primes. If

    .. math::
        n = (n_{r}\ldots n_{0})_{p}\\
        k = (k_{r}\ldots k_{0})_{p}
    
    then
    
    .. math:: \binom{n}{k} \equiv \binom{n_{r}}{k_{r}}\cdots\binom{n_{0}}{k_{0}}\pmod{p}

    Parameters
    ----------
    n : ``int``
        An integer.
    k : ``int``
        An integer.
    p : ``int``
        A prime.
    factorials : ``Optional[list[int]  |  np.ndarray], optional``
        Array of precalculated factorials :math:`\pmod{p}`., by default ``None``

    Returns
    -------
    ``int``
        :math:`\binom{n}{k}\pmod{p}` when :math:`n,k< p`.
    """

    factorials = np.empty(shape=(p,), dtype=int)
    factorials[0] = 1
    for i in range(1, p):
        factorials[i] = Integer(i).multiply_modular(other=factorials[i - 1], modulus=p)

    rem = 1
    while n > 0:
        r = n % p
        s = k % p
        rem = Integer(rem).multiply_modular(
            other=small_binomial_modulo_prime(n=r, k=s, p=p, factorials=factorials),
            modulus=p,
        )
        n //= p
        k //= p

    return rem
