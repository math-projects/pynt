"""Integers"""


from sympy.ntheory import pollard_rho

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

    def pollard_rho_factor(self, a: int, c: int, max_iter: int = 5) -> int:
        """
        Find a factor of ``n`` greater than 1 using Pollard's rho factorization.
        Use f(x) = x^2+c
        :param a: Initial value of ``x``.
        :type a: ``int``
        :param c: Constant in the polynomial.
        :type c: ``int``
        :param max_iter: Maximum number of iteration to find a non-trivial divisor, defaults to 5
        :type max_iter: ``int``, optional
        :raises ValueError: If ``n`` can be factorized using classical sieve.
        :return: A non-trivial divisor of ``n`` if ``n`` is not a prime.
        :rtype: ``int``
        """

        if (self % 2) == 0:
            return 2

        if self <= LARGEST_SMALL_NUMBER:
            raise ValueError(
                f"{self} is smaller than: {LARGEST_SMALL_NUMBER}. Use normal sieve."
            )

        return pollard_rho(n=self, s=a, a=c, retries=max_iter)
