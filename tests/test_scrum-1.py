
import pytest

@pytest.mark.parametrize("input1, input2, expected_sum", [
(5, 10, 15),
(-5, 10, 5),
(5, -10, -5),
(-5, -10, -15)])
def test_addition(input1, input2, expected_sum):
assert add(input1, input2) == expected_sum

def add(a, b):
return a + b