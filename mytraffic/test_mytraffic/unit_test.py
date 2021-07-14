import os
import pytest
from mytraffic.utils import sum_input_file


class TestMaker:
    """
    The aim of this class is to define the path directory for test_mytraffic
    and the path directory to input data for test_mytraffic and use them for
    all the other test
    """

    def _set_config(self):
        self.current_dir = os.path.dirname(__file__)
        self.test_data_dir = 'test_input_data'

    def test_sum_input_file(self):
        self._set_config()
        input_file = os.path.join(self.current_dir,  self.test_data_dir, 'input_test_sum_file.txt')
        assert sum_input_file(input_file) == 38
