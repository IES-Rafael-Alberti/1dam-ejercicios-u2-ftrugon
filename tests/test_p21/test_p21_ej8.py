import pytest
from src.p2_1.P21_ej8 import niveles

@pytest.mark.parametrize(
    "input_numpunt, expected",
    [
        (0.0, "Tu nivel es inaceptable ,vas a recibir 0.0€"),
        (0.4, "Tu nivel es aceptable, vas a recibir 960.0€"),
        (0.6, "Tu nivel es meritario, vas a recibir 1440.0€"),
        (0.8, "Tu nivel es meritario, vas a recibir 1920.0€")
    ]
)
def test_niveles(input_numpunt, expected):
    assert niveles(input_numpunt) == expected