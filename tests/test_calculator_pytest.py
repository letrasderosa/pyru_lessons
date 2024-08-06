import pytest

from lesson.calculator import calculator

def test_plus():
    assert  calculator('2+2') == 4

def test_no_signs():
    with pytest.raises(ValueError) as error:
        calculator('abracadabra')
    assert 'Выражение должно содержать хотя бы один знак (+-/*)' == error.value.args[0]

def test_two_signs():
    with pytest.raises(ValueError) as error:
        calculator('2+2+2')
        print(f'error.value.args: {error.value.args}')
        assert 'Выражение должно содержать 2 целых числа и 1 знак' == error.value.args[0]

if __name__ == '__main__':
    pytest.main()

