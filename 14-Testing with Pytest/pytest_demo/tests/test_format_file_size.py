from src.formatter import format_file_size


def test_format_file_size_returns_GB_format():
    assert format_file_size(1024**3) == "2.00 GB"