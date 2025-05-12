import pytest
from main import hello


def test_hello_type_error():
    with pytest.raises(TypeError):
        hello(123)
