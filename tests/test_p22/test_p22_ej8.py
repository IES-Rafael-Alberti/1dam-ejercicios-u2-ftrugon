import pytest
from src.p2_2.p22_ej8 import escalera

@pytest.mark.parametrize(
    "input_numero, expected",
    [
        (5, "9 7 5 3 1 "),
        (3, "5 3 1 ")
    ]
)
def test_escalera(input_numero, expected):
    assert escalera(input_numero) == expected