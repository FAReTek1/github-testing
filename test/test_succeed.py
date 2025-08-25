import os


def test_succeed():
    assert 1 == 1
    assert os.getenv("TEST_SECRET") is not None

