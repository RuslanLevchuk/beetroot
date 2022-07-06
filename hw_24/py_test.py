import pytest
from u_test import TempConvTest

from t_converter import converter

def test_something():
    assert converter('-14C') == (7, 'F', '7F')

def test_something_2():
    assert converter('52F') == (11, 'C', '11C')

def test_unittest():
    TempConvTest