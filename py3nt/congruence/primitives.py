"""Order/primitive root functions"""


import numpy as np

from py3nt.core.factorize import FactorizationFactory
from py3nt.functions.unary.divisor_functions import generate_divisors


def order_modulo_prime_power(
    a: int, p: int, e: int, factorizer: FactorizationFactory
) -> int:
    r"""Caculate :math:`\mbox{ord}_{p}(a)`.
    The smallest positive integer such that

    .. math:: a^{\mbox{ord}_{p}(a)} \equiv1\pmod{p^{e}}

    Parameters
    ----------
    a : ``int``
        An integer.
    p : ``int``
        A prime.
    e : ``int``
        A positive integer.
        :math:`p^{e}` must not exceed the default biggest number.
    factorizer : ``FactorizationFactory``
        Used to factorize `p-1`.

    Returns
    -------
    ``int``
        :math:`\mbox{ord}_{p}(a)`.
    """

    divisors = generate_divisors(n=p - 1, factorizer=factorizer)
    divisors = np.sort(divisors)

    d = p - 1

    for divisor in divisors:
        if pow(base=a, exp=int(divisor), mod=int(p)) == 1:
            d = divisor
            break

    order = d * pow(p, e - 1)
    for k in range(e, 1, -1):
        if pow(a, int(d), int(pow(p, k))) == 1:
            order = d * pow(p, e - k)

    return order


def order_modulo_n(
    a: int,
    n: int,
    factorizer: FactorizationFactory,
) -> int:
    r"""Caculate :math:`\mbox{ord}_{n}(a)`.
    The smallest positive integer such that

    .. math:: a^{\mbox{ord}_{n}(a)} & \equiv1\pmod{n}

    Parameters
    ----------
    a : ``int``
        An integer.
    n : ``int``
        A positive integer.
    factorizer : ``FactorizationFactory``
        Used to factorize :math:`n`.

    Returns
    -------
    ``int``
        :math:`\mbox{ord}_{n}(a)`.

    Raises
    ------
    ``ValueError``
        If :math:`\gcd(a,n) > 1`.
    """
    g = np.gcd(a, n)
    if g > 1:
        raise ValueError(f"a: {a}, n: {n}, gcd: {g} > 1.")

    order = 1
    factorization = factorizer.factorize(n=n)

    for prime, multiplicity in factorization.items():
        order = np.lcm(
            order,
            order_modulo_prime_power(a=a, p=prime, e=multiplicity, factorizer=factorizer),
        )

    return order
