import pytest
from src.p2_2.p22_ej6 import estrellas

@pytest.mark.parametrize(
    "input_numeestre, expected",
    [
        (-2, "el numero tiene que ser positivo"),
        (4, "****"),
        (10, "**********"),
        (15, "***************")
    ]
)
def test_estrellas(input_numeestre, expected):
    assert estrellas(input_numeestre) == expected