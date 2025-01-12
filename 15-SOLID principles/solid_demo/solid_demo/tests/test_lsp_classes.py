from dataclasses import dataclass
import pytest

from solid_demo.lsp_classes import TwoDimShape, Triangle, Rectangle

@pytest.mark.parametrize(
    "two_dim_shape, expected_area",
    [
        (Triangle(2.3, 3.5), 4.02),
        (Triangle(4.3, 3.5), 7.52),
        (Rectangle(4.3, 3.5), 15.05)
    ]
)
def test_valid_subclass_substitutions(two_dim_shape: TwoDimShape, expected_area):
    assert two_dim_shape.calculate_area() == expected_area

def test_invalid_subclass():
    assert False