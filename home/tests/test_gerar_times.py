import pytest


def test_should_fail():
    with pytest.raises(ZeroDivisionError) as execution:
        result = 1 / 0
    assert 'division by zero' in str(execution.value)

