"""Quadratic residues and symbols"""


from sympy.ntheory import jacobi_symbol as jacobi
from sympy.ntheory import legendre_symbol as legendre


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

    return legendre(a=a, p=p)


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

    return jacobi(m=a, n=n)
