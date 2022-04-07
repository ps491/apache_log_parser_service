from itertools import islice


def read_rows_in_chunks(iter_object, chunk_size=100):
    """Lazy function (generator) to read a file by rows.
    Default chunk size: 1k."""
    while True:
        chunk = [row for row in islice(iter_object, chunk_size)]
        if not chunk:
            break
        yield chunk


def read_file_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data
