"""Define primality tests"""

from random import randint

import numpy as np
from sympy.ntheory.primetest import mr

from py3nt.congruence.quadratic import jacobi_symbol
from py3nt.defaults import MAX_LOGN_FACTORIZATION_LIMIT


def is_prime_naive(n: int) -> bool:
    r"""Test numbers not exceeding :math:`\sqrt{n}` for primality.

    Parameters
    ----------
    n : ``int``
        A positive integer for primality testing.

    Returns
    -------
    ``bool``
        ``True`` if :math:`n` is prime, ``False`` otherwise.

    Raises
    ------
    ValueError
        If :math:`n` is not positive.
    """

    if n <= 0:
        raise ValueError("n must be positive.")

    if n < 2:
        return False

    if n < 4:
        return True

    if (n & 1) == 0:
        return False

    root = int(np.floor(np.sqrt(n)))

    for i in np.arange(start=3, stop=root + 1, step=2):
        if (n % i) == 0:
            return False

    return True


def miller_rabin(n: int, n_witnesses: int = 5) -> bool:
    """Miller-Rabin primality test.

    Parameters
    ----------
    n : ``int``
        A positive integer.
    n_witnesses : ``int``, optional
        Number of witnesses for the test, by default 5.

    Returns
    -------
    ``bool``
        ``True`` if :math:`n` is prime, ``False`` otherwise.
    """

    if n <= MAX_LOGN_FACTORIZATION_LIMIT:
        return is_prime_naive(n=n)

    logn = int(np.floor(np.log(n * 1.0)))

    bases = np.random.randint(
        low=2,
        high=np.minimum(n - 1, 2 * logn * logn),
        size=n_witnesses,
    )

    return mr(n=n, bases=bases)


def solovay_strassen(n: int, max_iter: int = 10) -> bool:
    """Solovay-Strassen primality test.

    Parameters
    ----------
    n : ``int``
        A positive integer.
    max_iter : ``int``, optional
        Number of retries, by default 10

    Returns
    -------
    ``bool``
        ``True`` if :math:`n` is prime, ``False`` otherwise.
    """

    if n < 3:
        return n == 2

    if (n & 1) == 0:
        return False

    logn = int(np.floor(np.log(n * 1.0)))

    for _ in range(max_iter):
        a = randint(
            a=2,
            b=np.minimum(
                n - 2,
                2 * logn * logn,
            ),
        )
        rem = jacobi_symbol(a=a, n=n)

        if pow(base=a, exp=(n - 1) >> 1, mod=n) != (rem % n):
            return False

    return True
