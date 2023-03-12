"""Binomial functions and expansions"""

import numpy as np


def homogeneous_binomial(a: int, b: int, n: int) -> int:
    r"""
    Calculate the homogeneous binomial: :math:`a^{n-1}+a^{n-2}b+\ldots+b^{n-1}`.
    We do not use :math:`\frac{a^{n}-b^{n}}{a-b}`.
    This can easily run into overflow issue.

    If :math:`f(n)=\frac{a^{n}-b^{n}}{a-b}`, then :math:`f(n+1)=(a+b)f(n)-ab \cdot f(n-1)`.

    If the companion matrix is

    .. math::
        C =
            \begin{pmatrix}
                a+b & -ab\\
                1 & 0
            \end{pmatrix}

    then

    .. math::
        \begin{pmatrix}
            f(n)\\
            f(n-1)
        \end{pmatrix} = C^{n-2}
        \begin{pmatrix}
            a+b\\
            1
        \end{pmatrix}

    We use matrix exponentiation to calculate :math:`C^{n-2}` in :math:`O(log{n})`.

    Parameters
    ----------
    a : ``int``
        An integer.
    b : ``int``
        An integer different than ``a``.
    n : ``int``
        A positive integer.

    Returns
    -------
    ``int``
        Value of :math:`a^{n-1}+a^{n-2}b+\ldots+b^{n-1}`.

    Raises
    ------
    ValueError
        If :math:`n` is not positive or :math:`a=b`.
    """

    if a == b:
        raise ValueError(f"a: {a} and b: {b} are same. They must be different.")

    if n < 1:
        raise ValueError(f"n: {n} must be positive.")

    if n == 1:
        return n

    if n == 2:
        return a + b

    print(a, b, n)

    companion = np.array([[a + b, -a * b], [1, 0]])
    f_n = np.linalg.matrix_power(a=companion, n=n - 2)

    return f_n[0, 0] * (a + b) + f_n[0, 1]
