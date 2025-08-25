import os
from pprint import pprint


def test_succeed():
    assert 1 == 1

    pprint(os.environ)
