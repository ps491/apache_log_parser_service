import re

# Regex for the common Apache log format.
parts = [
    r'(?P<ip>\S+)',  # host %h
    r'(?P<indent>\S+)',  # indent %l (unused)
    r'(?P<user>\S+)',  # user %u
    r'\[(?P<time>.+)\]',  # time %t
    r'"(?P<method>.*)',  # "   request "%r"
    r'(?P<url>.*)',  # request "%r"
    r'(?P<protocol>.*)"',  # request "%r"    "
    r'(?P<status>[0-9]+)',  # status %>s
    r'(?P<size>\S+)',  # size %b (careful, can be '-')
    r'"(?P<referrer>.*)"',  # referrer "%{Referer}i"
    r'"(?P<agent>.*)"',  # user agent "%{User-agent}i"
    r'"(?P<other>.*)"',  # user agent "%{User-agent}i"
]
pattern = re.compile(r'\s+'.join(parts) + r'\s*\Z')

log_data = []
# with open('access_2022_04_04.log', 'r') as f:
#     for row in f.read().splitlines():
#         log_data.append(pattern.match(row).groupdict())
from itertools import islice


def read_in_chunks(iter_object, chunk_size=2):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        chunk = [row for row in islice(iter_object, chunk_size)]
        if not chunk:
            break
        yield chunk


with open('access_2022_04_04.log', 'r') as f:
    # for row in f.read().splitlines():
    #     print(row)
    # if hasattr(f.read().splitlines(), '__iter__'):
    #     print('ok')

    for slice in read_in_chunks(f):
        log_data = []
        for i in slice:
            log_data.append(pattern.match(i).groupdict())
        print(log_data)
