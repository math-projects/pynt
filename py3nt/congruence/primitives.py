"""Order/primitive root functions"""


import numpy as np

from py3nt.core.factorize import FactorizationFactory, is_prime, is_prime_power
from py3nt.functions.unary.divisor_functions import generate_divisors


def highest_power_of_2(a: int) -> int:
    r"""Calculate :math:`\nu_{2}(a)`.

    Parameters
    ----------
    a : ``int``
        An integer.

    Returns
    -------
    ``int``
        Highest power of 2 that divides :math:`a`.
    """

    exp = 0

    while not a & 1:
        a >>= 1
        exp += 1

    return exp


def order_modulo_power_of_2(a: int, k: int) -> int:
    r"""Calculate :math:`\mbox{ord}_{2^{k}}(a)`.
    The smallest positive integer such that

    .. math:: a^{\mbox{ord}_{2^{k}}(a)} \equiv1\pmod{2^{k}}


    Parameters
    ----------
    a : int
        _description_
    k : int
        _description_

    Returns
    -------
    int
        _description_

    Raises
    ------
    ValueError
        _description_
    """

    if not a & 1:
        raise ValueError(f"a: {a} is divisible by 2.")

    alpha = highest_power_of_2(a=a - 1)

    if alpha >= k:
        return 1

    beta = highest_power_of_2(a=a + 1)

    return 1 << (k - alpha - beta + 1)


def order_modulo_prime_power(
    a: int, p: int, e: int, factorizer: FactorizationFactory
) -> int:
    r"""Caculate :math:`\mbox{ord}_{p^{e}}(a)`.
    The smallest positive integer such that

    .. math:: a^{\mbox{ord}_{p^{e}}(a)} \equiv1\pmod{p^{e}}

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

    if p == 2:
        return order_modulo_power_of_2(a=a, k=e)

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


def order_modulo_n(a: int, n: int, factorizer: FactorizationFactory) -> int:
    r"""Caculate :math:`\mbox{ord}_{n}(a)`.
    The smallest positive integer such that

    .. math:: a^{\mbox{ord}_{n}(a)} \equiv1\pmod{n}

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
            order_modulo_prime_power(
                a=a, p=prime, e=multiplicity, factorizer=factorizer
            ),
        )

    return order


def least_primitive_root_modulo_prime(p: int, factorizer: FactorizationFactory) -> int:
    r"""Find the least primitive root :math:`\pmod{p}`.

    Parameters
    ----------
    p : ``int``
        A prime.
    factorizer : ``FactorizationFactory``
        Used to calculate order :math:`\pmod{p}`.

    Returns
    -------
    ``int``
        Least primitive root.

    Raises
    ------
    ``ValueError``
        If :math:`p` is not a prime.
    """

    if p < 2:
        raise ValueError(f"p:{p} < 2.")

    if not is_prime(p):
        raise ValueError(f"p: {p} is not a probable prime.")

    limit = int(np.floor(pow(p, 0.68)))

    g = 1
    for a in range(2, limit + 1):
        if order_modulo_prime_power(a=a, p=p, e=1, factorizer=factorizer) == p - 1:
            g = a
            break

    return g


def primitive_root_modulo_prime_power(
    p: int, e: int, factorizer: FactorizationFactory
) -> int:
    r"""Find the least primitive root :math:`\pmod{p^{e}}`.

    Parameters
    ----------
    p : ``int``
        A prime.
    e: ``int``
        A positive integer.
    factorizer : ``FactorizationFactory``
        Used to calculate order :math:`\pmod{p^{e}}`.

    Returns
    -------
    ``int``
        Least primitive root.
    """
    g = least_primitive_root_modulo_prime(p=p, factorizer=factorizer)
    order = order_modulo_prime_power(a=p, p=p, e=e, factorizer=factorizer)

    if order != pow(p, e - 1) * (p - 1):
        return g + p

    return g


def primitive_root_modulo_n(n: int, factorizer: FactorizationFactory) -> int:
    r"""Primitive root :math:`n` if it exists.

    Parameters
    ----------
    n : ``int``
        A positive integer.
    factorizer : ``FactorizationFactory``
        Used to calculate primitive root :math:`\pmod{p}`.

    Returns
    -------
    ``int``
        A primitive root.

    Raises
    ------
    ValueError
        If :math:`n<3` or :math:`n` does not have a primitive root.
    """

    if n < 3:
        raise ValueError(f"n: {n} must be at least 3.")

    if not n & 3:
        raise ValueError(f"n: {n} is divisible by 4, does not have a primitive root.")

    m = None
    if not n & 1:
        m = n
        n >>= 1

    p, e = is_prime_power(n=n)
    print(m, n, p, e)

    if not p:
        raise ValueError(f"n: {n} is not one of 2, 4, p^k, 2p^k")

    g = primitive_root_modulo_prime_power(p=p, e=e, factorizer=factorizer)

    if m:
        if not g & 1:
            g += pow(p, e)

            if g > m:
                g %= m

    return g
