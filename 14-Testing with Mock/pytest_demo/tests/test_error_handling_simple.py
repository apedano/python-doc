import pytest
from src.formatter import format_file_size

def test_format_file_size_negative_size():
    with pytest.raises(ValueError, match="Size cannot be negative"):
        format_file_size(-1)