import pytest

def test_addition():
    # positive test case
    assert add(5, 10) == 15

    # negative test case
    assert add(-5, 10) == -5

    # edge case: adding zero to a number
    assert add(5, 0) == 5

# parametrize test cases for different input values
@pytest.mark.parametrize("input_1,input_2", [
    (1, 2),
    (-1, 2),
    (10, -5)
])
def test_addition(input_1, input_2):
    assert add(input_1, input_2) == input_1 + input_2
