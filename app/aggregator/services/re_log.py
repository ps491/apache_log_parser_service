import re
from datetime import datetime


def re_logs_to_dict(row: str) -> dict:
    """Pegexp rows"""
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
    # распарсиваем в словарь
    result = pattern.match(row).groupdict()
    # распарсиваем time, переводим в объект datetime
    result['time'] = datetime.strptime(result['time'], '%d/%b/%Y:%H:%M:%S %z')
    return result
