"""Some variables for testing"""

import pytest


@pytest.fixture(scope="function")
def primes_small():
    """Some small primes for testing.

    :return: List of small primes.
    :rtype: ``list``
    """

    return [2, 31, 43, 97]


@pytest.fixture(scope="function")
def composites_small():
    """Some small composite numbers for testing.

    :return: List of composite numbers.
    :rtype: ``list``
    """

    return [25, 12, 100, 33]


@pytest.fixture(scope="function")
def primes_large():
    """Some large primes for testing.

    :return: List of large primes.
    :rtype: ``list``
    """

    return [4878131941, 8444627467, 652966860382061, 347304843108991, 96867285040138397903]
