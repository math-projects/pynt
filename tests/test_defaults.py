"""Test default values"""


import pytest

from py3nt.defaults import Defaults


def test_defaults() -> None:
    """Test default values"""

    defaults = Defaults()

    with pytest.raises(ValueError):
        defaults.set_largest_small_number(new_largest_small_number=int(1e7))

    with pytest.raises(ValueError):
        defaults.set_biggest_number(new_biggest_number=(1 << 40))

    defaults.set_biggest_number(int(1e50))
    assert defaults.get_biggest_number() == int(1e50)

    defaults.set_largest_small_number(int(1e15))
    assert defaults.get_largest_small_number() == int(1e15)

    defaults.reset()
