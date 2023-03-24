"""some basic functions in modular arithmetic"""


def extended_euclidean(a: int, b: int) -> tuple[int, int, int]:
    r"""Given :math:`a,b`.
    Find :math:`x,y` such that :math:`ax+by=\gcd(a,b)`.
    Such :math:`x,y` exists by Bézout's identity.
    Use Extended Euclidean algorithm.

    Parameters
    ----------
    a : ``int``
        An integer.
    b : ``int``
        An integer.

    Returns
    -------
    ``tuple[int, int, int]``
        :math:`x,y,\gcd(x,y)`.
    """

    x = 0
    old_x = 1
    gcd = b
    old_gcd = a

    while gcd != 0:
        quotient = old_gcd // gcd
        (old_gcd, gcd) = (gcd, old_gcd - quotient * gcd)
        (old_x, x) = (x, old_x - quotient * x)

    if not b:
        return (old_x, 0, old_gcd)

    return (old_x, (old_gcd - old_x * a) // b, old_gcd)


def inverse(a: int, n: int, is_prime: bool = False) -> int:
    r"""
    Calculate modular inverse of :math:`a\pmod{n}`.
    Use Extended algorithm when :math:`\gcd(a,n)=1`.

    Parameters
    ----------
    a : ``int``
        An integer.
    n : ``int``
        A positive integer greater than 1.
    is_prime : ``bool, optional``
        Whether :math:`n` is prime or not, by default False.
        If prime, then Fermat's little theorem is used to calculate inverse.

         .. math::
            a^{p-2} \equiv a^{-1}\pmod{p}

    Returns
    -------
    ``int``
        :math:`x` such that :math:`ax\equiv1\pmod{n}`.

    Raises
    ------
    ``ValueError``
        If :math:`\gcd(a,n) > 1` or :math:`n<2`.
    """

    if n <= 1:
        raise ValueError("n must be at least 2.")

    a %= n

    if not a:
        raise ValueError("a cannot be divisible by n.")

    if is_prime:
        return pow(a, n - 2, n)

    x, _, g = extended_euclidean(a=a, b=n)

    if g > 1:
        raise ValueError(f"gcd({a}, {n})={g} which is greater than 1.")

    return x
