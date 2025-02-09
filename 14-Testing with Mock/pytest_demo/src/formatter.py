import math

def format_file_size(size_bytes):
    if size_bytes < 0:
        raise ValueError("Size cannot be negative")

    elif size_bytes == 0:
        return "0B"

    size_name = ["B", "KB", "MB", "GB", "TB"]
    #finds the exponent in base 1024 of the size (to find the position in the size_name array)
    i = int(math.floor(math.log(size_bytes) / math.log(1024)))
    p = math.pow(1024, i)
    # formats the normalized number to the power of 1024 (the fractional part)
    s = "{:.2f}".format(size_bytes / p)
    return f"{s} {size_name[i]}"