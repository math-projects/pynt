"""Some default values"""

import numpy as np

LOGN_PRIME_FACTOR_FIELD = "largest_prime_factors_"


class Defaults:
    """Set default values"""

    _LARGEST_SMALL_NUMBER = int(1e14)
    _BIGGEST_NUMBER = int(1e70)
    _MAX_LOGN_FACTORIZATION_LIMIT = int(1e7)
    _DEFAULT_SIEVE_LIMIT = int(1e7)

    def get_largest_small_number(self) -> int:
        """Get the current default largest small number for sieve sqrt factorization."""

        return self._LARGEST_SMALL_NUMBER

    def set_largest_small_number(self, new_largest_small_number: int) -> None:
        """Set the largest small number to ``new_largest_small_number``"""

        if np.less_equal(new_largest_small_number, self._MAX_LOGN_FACTORIZATION_LIMIT):
            raise ValueError(
                f"""{new_largest_small_number} must be greater than
                logn factorization limit: {self._MAX_LOGN_FACTORIZATION_LIMIT}"""
            )
        self._LARGEST_SMALL_NUMBER = new_largest_small_number

    def get_biggest_number(self) -> int:
        """Get the current default biggest number you can factorize."""

        return self._BIGGEST_NUMBER

    def set_biggest_number(self, new_biggest_number) -> None:
        """Set the biggest number to ``new_biggest_number``"""

        if np.less_equal(new_biggest_number, self._LARGEST_SMALL_NUMBER):
            raise ValueError(
                f"""{new_biggest_number} must be greater than
                largest small number: {self._LARGEST_SMALL_NUMBER}"""
            )

    def get_max_logn_factorization_limit(self) -> int:
        """Get the current default maximum logn factorization limit."""

        return self._MAX_LOGN_FACTORIZATION_LIMIT

    def get_default_sieve_limit(self) -> int:
        """Get the current default sieve limit."""

        return self._DEFAULT_SIEVE_LIMIT


defaults = Defaults()

LARGEST_SMALL_NUMBER = defaults.get_largest_small_number()
BIG_NUMBER = defaults.get_biggest_number()
MAX_LOGN_FACTORIZATION_LIMIT = defaults.get_max_logn_factorization_limit()
DEFAULT_SIEVE_LIMIT = defaults.get_default_sieve_limit()
