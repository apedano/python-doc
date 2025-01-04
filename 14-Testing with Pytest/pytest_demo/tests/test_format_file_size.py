from src.formatter import format_file_size


def test_format_file_size_returns_GB_format():
    assert format_file_size(1024**3) == "1.00 GB"

def test_format_file_size_returns_format_zero():
    assert format_file_size(0) == "0B"


def test_format_file_size_returns_format_one_byte():
    assert format_file_size(1) == "1.00 B"


def test_format_file_size_returns_format_kb():
    assert format_file_size(1024) == "1.00 KB"


def test_format_file_size_returns_format_mb():
    assert format_file_size(1024**2) == "1.00 MB"


def test_format_file_size_returns_format_gb():
    assert format_file_size(1024**3) == "1.00 GB"


def test_format_file_size_returns_format_tb():
    assert format_file_size(1024**4) == "1.00 TB"
