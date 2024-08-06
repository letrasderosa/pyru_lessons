import pytest

from lesson.calculator import calculator, plus

def test_calc_plus():
    assert  calculator('2+2') == 4

def test_no_signs():
    with pytest.raises(ValueError) as error:
        calculator('abracadabra')
    assert 'Выражение должно содержать хотя бы один знак (+-/*)' == error.value.args[0]

def test_two_signs():
    with pytest.raises(ValueError) as error:
        calculator('2+2+2')
        assert 'Выражение должно содержать 2 целых числа и 1 знак' == error.value.args[0]


def test_plus():
    assert plus(3,3) == 6


def test_plus_zeroes():
    assert plus(0,0) == 0


def test_plus_should_be_zero_if_negative():
    assert plus(1,-1) == 0


if __name__ == '__main__':
    pytest.main()

