"""Tests for checkers."""
from chekers import check_date
import pytest

test_date = [([1900, 2, 29], False), ([2000, 2, 29], True), ([2010, 30, 20], False)]


@pytest.mark.parametrize("test_in, test_out", test_date)
def test_sub_str(test_in, test_out):
    assert check_date(test_in[0], test_in[1], test_in[2]) == test_out
