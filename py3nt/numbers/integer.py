"""Integers"""


import numpy as np
from sympy.ntheory import pollard_rho

from py3nt.defaults import MAX_LOGN_FACTORIZATION_LIMIT


class Integer(int):
    """
    Integer class

    Methods
    -------
    multiply_modular:
        Modular multiplication of current integer with another integer.
    pollard_rho_factor:
        Find a divisor of current integer using Pollard's rho factor algorithm.
    """

    def multiply_modular(self, other: int, modulus: int) -> int:
        """
        Calculate ``self*other%modulus``.
        This remainder will always be non-negative.
        If negative integers are provided, they will be converted to positive first.

        Parameters
        ----------
        other : ``int``
            Multiplier.
        modulus : ``int``
            Modulo used for multiplcation.

        Returns
        -------
        ``int``
            Multiplication of ``self`` and ``other`` modulo ``modulus``.
        """

        remainder = 0

        cur = self % modulus
        other %= modulus

        while other > 0:
            if (other & 1) == 1:
                remainder += cur
                if remainder > modulus:
                    remainder -= modulus

            other >>= 1
            cur <<= 1
            if cur > modulus:
                cur -= modulus

        remainder %= modulus

        return remainder

    def kthroot(self, k: int) -> int:
        r"""

        Parameters
        ----------
        k : ``int``
            A positive integer.

        Returns
        -------
        ``int``
            A positive integer :math:`r` such that :math:`r^{k}\leq n<r^{k+1}`.
        """

        high = 1
        while pow(high, k) < self:
            high <<= 1
        low = high >> 1
        while high - low > 1:
            mid = (low + high) >> 1
            cur = pow(mid, k)
            if cur < self:
                low = mid
            elif self < cur:
                high = mid
            else:
                return mid
        if pow(high, k) == self:
            return high
        else:
            return low

    def __pow__(self, exponent: int, modulus=None):
        if not modulus:
            return pow(int(self), int(exponent))

        return pow(int(self), int(exponent), int(modulus))

    def pollard_rho_factor(self, a: int, c: int, max_iter: int = 5) -> int:
        """
        Find a factor of ``n`` greater than 1 using Pollard's rho factorization.
        Use :math:`f(x) = x^2+c`

        Parameters
        ----------
        a : ``int``
            Initial value of ``x``.
        c : ``int``
            Constant in the polynomial.
        max_iter : ``int``, optional
            Maximum number of iteration to find a non-trivial divisor, by default 5

        Returns
        -------
        ``int``
            A non-trivial divisor of ``n`` if ``n`` is not a prime.

        Raises
        ------
        ``ValueError``
            If ``n`` can be factorized using classical sieve
            or is larger than the biggest number.
        """

        if (self % 2) == 0:
            return 2

        return pollard_rho(n=self, s=a, a=c, retries=max_iter)

    def brent_pollard_rho_factor(self) -> int:
        """Brent's optimization of Pollard's rho algorithm.

        Returns
        -------
        ``int``
            A non-trivial factor of :math:`n` when :math:`n` is not a prime.
        """

        if (self & 1) == 0:
            return 2

        if self < MAX_LOGN_FACTORIZATION_LIMIT:
            return self.pollard_rho_factor(a=2, c=1, max_iter=10)

        y = np.random.randint(low=2, high=int(np.minimum(self - 1, (1 << 30))))
        c = np.random.randint(low=2, high=int(np.minimum(self - 1, (1 << 30))))
        m = np.random.randint(low=2, high=int(np.minimum(self - 1, (1 << 30))))
        divisor, r, q = 1, 1, 1

        while divisor == 1:
            x = y
            for _ in range(r):
                y = (Integer(y).multiply_modular(other=y, modulus=self) + c) % self

            k = 0
            while k < r and divisor == 1:
                ys = y
                for _ in range(min(m, r - k)):
                    y = ((y * y) % self + c) % self
                    q = q * (abs(x - y)) % self
                divisor = np.gcd(q, self)
                k = k + m
            r <<= 1

        if divisor == self:
            while True:
                ys = ((ys * ys) % self + c) % self
                divisor = np.gcd(abs(x - ys), self)
                if divisor > 1:
                    break

        return divisor
