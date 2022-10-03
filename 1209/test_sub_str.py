"""Tests go check sub str."""
import pytest
from check_sub_str import fun_one

test_str = [("AAA AAA bbb bbb", 50), ("aaa aaa", 0), ("AAA AAa", 100)]


@pytest.mark.parametrize("test_in, test_out", test_str)
def test_sub_str(test_in, test_out):
    assert fun_one(test_in) == test_out
