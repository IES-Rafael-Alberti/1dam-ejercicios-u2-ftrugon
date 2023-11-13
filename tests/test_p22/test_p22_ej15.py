import pytest
from src.p2_2.p22_ej9 import comprobrar

@pytest.mark.parametrize(
    "input_num, expected",
    [
        ("0","Serie => 0 = 0")
    ]
)
def test_comprobar(input_num, expected):
    assert comprobrar(input_num) == expected