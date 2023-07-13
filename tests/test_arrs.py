from utils import arrs

from dicts import get_val


def test_get():
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([], -1, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice([1, 2, 3], -1) == [3]
    assert arrs.my_slice([1, 2, 3], -9) == [1, 2, 3]


def test_get_val():
    assert get_val([1, 2, 3], 1) == 'git'
    assert get_val({1: 1, 2: 2}, 1) == 1
    assert get_val({1: 1, 2: 2}, 3) == 'git'
