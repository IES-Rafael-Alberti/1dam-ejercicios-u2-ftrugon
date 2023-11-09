import pytest
from src.p2_1.P21_ej7 import tipo_impositivo

@pytest.mark.parametrize(
    "input_renta, expected",
    [
        (1, "Tu renta es del 5%"),
        (10001, "tu renta es del 15%"),
        (20001, "tu renta es del 20%"),
        (36000, "tu renta es del 30%"),
        (62000, "tu renta es del 45%")
    ]
)
def test_tipo_impositivo(input_renta, expected):
    assert tipo_impositivo(input_renta) == expected