from django.test import TestCase

from aggregator.services.re_log import re_logs_to_dict


class TestLog(TestCase):
    """Тестирование логов"""

    def test_regexp_log(self):
        """тестирование регулярок"""
        test_data = '35.237.4.214 - - [19/Dec/2020:15:22:40 +0100] "GET /administrator/%22 HTTP/1.1" 404 226 "-" ' \
                    '"Mozilla/5.0 (compatible; Discordbot/2.0; +https://discordapp.com)" "-" '
        result = {'ip': '35.237.4.214',
                  'indent': '-',
                  'user': '-',
                  'time': '19/Dec/2020:15:22:40 +0100',
                  'method': 'GET',
                  'url': '/administrator/%22',
                  'protocol': 'HTTP/1.1',
                  'status': '404',
                  'size': '226',
                  'referrer': '-',
                  'agent': 'Mozilla/5.0 (compatible; Discordbot/2.0; +https://discordapp.com)',
                  'other': '-'}
        self.assertEqual(re_logs_to_dict(test_data), result)
