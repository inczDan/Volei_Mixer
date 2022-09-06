import pytest

from administracaodeparticipantes.models import Participante
from home import gerador_times


def test_tem_que_falhar():
    with pytest.raises(ZeroDivisionError) as execution:
        result = 1 / 0
    assert 'division by zero' in str(execution.value)


