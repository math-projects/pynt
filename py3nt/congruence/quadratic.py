"""Quadratic residues and symbols"""


from py3nt.numbers.integer import Integer


def legendre(a: int, p: int) -> int:
    """Calculate Legendre symbol (a/p).
    p must be a prime.

    :param a: Integer in Legendre symbol.
    :type a: ``int``
    :param p: Modulus in Legendre symbol.
    :type p: ``int``
    :return: Legendre symbol (a/n). One of -1, 0 or 1.
    :rtype: ``int``
    """

    if (a % p) == 0:
        return 0

    remainder = pow(Integer(a), exp=(p - 1) >> 1, mod=p)

    if ((remainder - 1) % p) == 0:
        return 1

    return -1


def jacobi(a: int, n: int) -> int:
    """Calculate Jacobi symbol (a/n).
    n must be a positive odd number.

    :param a: Integer in Jacobi symbol.
    :type a: ``int``
    :param n:
    :type n: int
    :raises ValueError: If n is not positive or odd.
    :return: Jacobi symbol (a/n). One of -1, 0 or 1.
    :rtype: ``int``
    """

    if n <= 0:
        raise ValueError(f"{n} must be positive.")

    if (n & 1) == 0:
        raise ValueError(f"{n} is not odd.")

    res = 1
    a %= n

    while a != 0:
        while (a & 1) == 0:
            a >>= 1
            rem = n % 8

            if rem == 3 or rem == 5:
                res = -res

        a, n = n, a

        if (a % 4) == (n % 4) == 3:
            res = -res

        a %= n

    if n == 1:
        return res

    return 0
