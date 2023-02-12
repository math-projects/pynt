"""Factorize integers"""


from dataclasses import dataclass, field

import numpy as np


@dataclass
class Factorize:
    """Factorize positive integers"""

    n: int

    factorization_: list = field(init=False)

    def __post_init__(self) -> None:
        self.factorization_ = []

    def factorize_small(self) -> None:
        if self.n < 1:
            self.factorization_ = [{1: 1}]

            return

        if np.greater(self.n, 1e14) is True:
            self.factorization_ = []

            return
