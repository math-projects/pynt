"""Quadratic residues and symbols"""


from sympy.ntheory import jacobi_symbol as jacobi
from sympy.ntheory import legendre_symbol as legendre


def legendre_symbol(a: int, p: int) -> int:
    """Calculate Legendre symbol (a/p).
    p must be a prime.

    :param a: An integer.
    :type a: ``int``
    :param p: A prime.
    :type p: ``int``
    :return: Legendre symbol (a/n). One of -1, 0 or 1.
    :rtype: ``int``
    """

    return legendre(a=a, p=p)


def jacobi_symbol(a: int, n: int) -> int:
    """Calculate Jacobi symbol (a/n).
    n must be a positive odd number.

    :param a: An integer.
    :type a: ``int``
    :param n: A positive odd integer.
    :type n: ``int``
    :raises ValueError: If n is not positive or odd.
    :return: Jacobi symbol (a/n). One of -1, 0 or 1.
    :rtype: ``int``
    """

    if n <= 0:
        raise ValueError(f"{n} must be positive.")

    if (n & 1) == 0:
        raise ValueError(f"{n} is not odd.")

    return jacobi(m=a, n=n)
