"""Integers"""


from sympy.ntheory import pollard_rho

from py3nt.defaults import BIGGEST_NUMBER, LARGEST_SMALL_NUMBER


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

    def __pow__(self, exponent: int, modulus=None):
        if not modulus:
            return pow(int(self), int(exponent))

        return pow(int(self), int(exponent), int(modulus))

    def pollard_rho_factor(self, a: int, c: int, max_iter: int = 5) -> int:
        """
        Find a factor of ``n`` greater than 1 using Pollard's rho factorization.
        Use f(x) = x^2+c

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

        if self <= LARGEST_SMALL_NUMBER or self > BIGGEST_NUMBER:
            raise ValueError(
                f"{self} is smaller than: {LARGEST_SMALL_NUMBER}. Use normal sieve."
            )

        return pollard_rho(n=self, s=a, a=c, retries=max_iter)
