import pytest


@pytest.fixture(scope="function")
def primes_small():
    return [2, 31, 43, 97]


@pytest.fixture(scope="function")
def composites_small():
    return [25, 12, 100, 33]
