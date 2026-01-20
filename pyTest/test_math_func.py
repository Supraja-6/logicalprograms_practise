"""import math_func
import pytest 
import sys
#@pytest.mark.number
#@pytest.mark.skip(reason = "do not run number add tests")

@pytest.mark.skipif(sys.version_info > (3.3), reason = "do not run number add tests")
def test_add():
    assert math_func.add(7, 3) == 10     #assertion that we want to assert that the function is returning the desired result
    assert math_func.add(6) == 8
    assert math_func.add(5) == 7

@pytest.mark.number
def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10
    assert math_func.product(7) == 14

@pytest.mark.strings
def test_add_strings():
    result = math_func.add('Hello', ' World')
    assert result == 'Hello World'
    assert type(result) is str
    assert 'Heldlo' not in result

@pytest.mark.strings
def test_product_strings():
    assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
    result = math_func.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str 
    assert 'Hello ' in result"""

import math_func
import pytest

@pytest.mark.parametpyterize('num1, num2, result',
                         [
                                 (7, 3, 10),
                                 ('Hello', ' World', 'Hello World'),
                                 (10.5, 25.5, 36)
                         ]
                         )
def test_add(num1, num2, result):
    assert math_func.add(num1, num2) == result
    
    
    """assert math_func.add(7, 3) == 10
    result = math_func.add('Hello', ' World')
    assert result == 'Hello World'
    result = math_func.add(10.5, 25.5)
    assert result == 36"""
