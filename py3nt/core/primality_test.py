"""Define primality tests"""

from random import randint

import numpy as np
from sympy.ntheory.primetest import mr

from py3nt.congruence.quadratic import jacobi_symbol
from py3nt.defaults import MAX_LOGN_FACTORIZATION_LIMIT


def is_prime_naive(n: int) -> bool:
    """Check if ``n`` is prime using square root method.

    :param n: Integer to check.
    :type n: ``int``
    :raises ValueError: If ``n`` is negative.
    :return: ``True`` if :math:`n` is a prime. Otherwise, ``False``.
    :rtype: ``bool``
    """

    if n < 0:
        raise ValueError("n cannot be negative")

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

    :param n: An integer.
    :type n: ``int``
    :param n_witnesses: Number of witnesses for the test, defaults to 5.
    :type n_witnesses: ``int``, optional
    :return: Whether :math:`n` is prime or not.
    :rtype: ``bool``
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

    :param n: An integer.
    :type n: ``int``
    :param max_iter: Number of retries, defaults to 10.
    :type max_iter: ``int``, optional
    :return: Whether :math:`n` is an integer.
    :rtype: ``bool``
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
