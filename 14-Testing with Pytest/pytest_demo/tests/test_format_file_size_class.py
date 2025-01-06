from src.formatter import format_file_size

class TestFormatSizes:

    def test_format_file_size_returns_GB_format(self):
        assert format_file_size(1024**3) == "1.00 GB"

    def test_format_file_size_returns_format_one_byte(self):
        assert format_file_size(1) == "1.00 B"


    def test_format_file_size_returns_format_kb(self):
        assert format_file_size(1024) == "1.00 KB"


    def test_format_file_size_returns_format_mb(self):
        assert format_file_size(1024**2) == "1.00 MB"


    def test_format_file_size_returns_format_gb(self):
        assert format_file_size(1024**3) == "1.00 GB"


    def test_format_file_size_returns_format_tb(self):
        assert format_file_size(1024**4) == "1.00 TB"
