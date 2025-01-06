from src.formatter import format_file_size

def test_format_file_size_returns_format_zero():
    assert format_file_size(0) == "0B"


