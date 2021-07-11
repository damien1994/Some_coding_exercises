import pytest
from mytraffic.utils import sum_input_file


def test_sum_input_file():
    assert sum_input_file("test_input_data/input_test_sum_input_file.txt") == 38
