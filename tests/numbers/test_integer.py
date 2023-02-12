"""Test Integer"""

from py3nt.numbers.integer import Integer


def test_integer():
    """Test Integer class"""

    twelve = Integer(12)

    assert twelve == 12
