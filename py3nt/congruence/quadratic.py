"""Quadratic residues and symbols."""


import numpy as np


def legendre_symbol(a: int, p: int) -> int:
    r"""Calculate Legendre symbol.

    Parameters
    ----------
    a : ``int``
        An integer.
    p : ``int``
        A prime.

    Returns
    -------
    ``int``
        Legendre symbol :math:`(\frac{a}{p})\in\{-1,0,1\}`.
    """

    a %= p

    if not a:
        return 0

    if pow(a, (p - 1) >> 1, p) == 1:
        return 1

    return -1


def jacobi_symbol(a: int, n: int) -> int:
    r"""Calculate Jacobi symbol.

    Parameters
    ----------
    a : ``int``
        An integer.
    n : ``int``
        A positive odd integer.

    Returns
    -------
    ``int``
        Jacobi symbol :math:`(\frac{a}{n})\in\{-1,0,1\}`.

    Raises
    ------
    ValueError
        If :math:`n` is not positive or odd.
    """

    if n <= 0:
        raise ValueError(f"{n} must be positive.")

    if (n & 1) == 0:
        raise ValueError(f"{n} is not odd.")

    if a < 0 or a > n:
        a %= n

    if not a:
        return int(n == 1)

    if n == 1 or a == 1:
        return 1

    if np.gcd(a, n) != 1:
        return 0

    jacobi = 1

    while a != 0:
        while (a & 1) == 0 and a > 0:
            a >>= 1
            if n % 8 in [3, 5]:
                jacobi = -jacobi
        a, n = n, a
        if a % 4 == n % 4 == 3:
            jacobi = -jacobi
        a %= n

    return jacobi
