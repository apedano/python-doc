from dataclasses import dataclass
import pytest

from solid_demo.lsp_classes import TwoDimShape, TwoDimShape, Triangle, Rectangle, InvalidShape, InvalidShapeException

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

def test_lsp_invalid_subclass():
    shape: TwoDimShape = InvalidShape(1, 2)
    with pytest.raises(InvalidShapeException, match=""):
        shape.calculate_area()