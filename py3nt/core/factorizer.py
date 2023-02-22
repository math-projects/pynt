"""Factorizer class"""

from dataclasses import dataclass, field
from typing import Union

import numpy as np

from py3nt.core.factorize import (
    BaseFactorization,
    BigIntFactorization,
    LognSieveFactorization,
    NaiveSqrtFactorization,
    SieveSqrtFactorization,
)
from py3nt.defaults import LARGEST_SMALL_NUMBER, MAX_LOGN_FACTORIZATION_LIMIT
