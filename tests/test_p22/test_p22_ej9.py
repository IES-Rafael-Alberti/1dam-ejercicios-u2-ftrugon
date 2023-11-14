import pytest
from src.p2_2.p22_ej9 import comprobrar

@pytest.mark.parametrize(
    "input_comprobado, expected",
    [
        ("asd","Iniciando sesion")
    ]
)
def test_comprobar(input_comprobado, expected):
    assert comprobrar(input_comprobado) == expected