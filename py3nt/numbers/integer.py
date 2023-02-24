"""Integers"""


import numpy as np

from py3nt.defaults import LARGEST_SMALL_NUMBER


class Integer(int):
    """Integer class"""

    def multiply_modular(self, other: int, modulus: int) -> int:
        """Calculate ``self*other%modulus``
        This remainder will always be non-negative.
        If negative integers are provided, they will be converted to positive first.

        :param other: Multiplier.
        :type other: ``int``
        :param modulus: Modulo used for multiplcation.
        :type modulus: ``int``
        :return: Multiplication of ``self`` and ``other`` modulo ``modulus``.
        :rtype: ``int``
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

    def __pow__(self, exponent: int, modulus=None):
        if not modulus:
            return pow(int(self), int(exponent))

        return pow(int(self), int(exponent), int(modulus))

    def _pollard_func(self, x: int, c: int) -> int:
        remainder = Integer(x).multiply_modular(other=x, modulus=self)
        remainder = (remainder + c) % self

        return remainder

    def pollard_rho_factor(self, a: int, c: int, max_iter: int = 5) -> int:
        if (self % 2) == 0:
            return 2

        if self <= LARGEST_SMALL_NUMBER:
            raise ValueError(
                f"{self} is smaller than: {LARGEST_SMALL_NUMBER}. Use normal sieve."
            )

        x = a
        y = x

        divisor = 1
        iteration = 0

        for _ in range(max_iter):
            x = self._pollard_func(x=x, c=c)
            y = self._pollard_func(x=y, c=c)
            y = self._pollard_func(x=y, c=c)

            divisor = np.gcd(abs(x - y), self)

            if divisor > 1:
                return divisor
            iteration += 1

        return divisor

    def brent_pollard_rho_factor(self, max_iter: int = 5) -> int:
        if self % 2 == 0:
            return 2

        if self < LARGEST_SMALL_NUMBER:
            raise ValueError(
                f"{self} is smaller than {LARGEST_SMALL_NUMBER}. Use normal sieve."
            )

        y = np.random.randint(1, self - 1)
        c = np.random.randint(1, self - 1)
        m = np.random.randint(1, self - 1)

        divisor, r, q = 1, 1, 1
        while divisor == 1:
            x = y
            for _ in range(r):
                y = self._pollard_func(x=y, c=c)

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
            for _ in range(max_iter):
                ys = self._pollard_func(x=ys, c=c)
                divisor = np.gcd(abs(x - ys), self)
                if divisor > 1:
                    break

        return divisor
