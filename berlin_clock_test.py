import unittest


def single_minute_row(time):
    minutes = extract_single_minute(time)
    if minutes % 5 == 4:
        return "YYYY"
    if minutes % 5 == 2:
        return "YYOO"
    if minutes % 5 == 3:
        return "YYYO"
    if minutes % 5 == 1:
        return "YOOO"
    return "OOOO"


def extract_single_minute(time):
    return int(time.split(":")[1])


class MyTestCase(unittest.TestCase):
    def test_to_midnight(self):
        self.assertEqual("OOOO", single_minute_row("00:00:00"))

    def test_to_59(self):
        self.assertEqual("YYYY", single_minute_row("23:59:59"))

    def test_to_32(self):
        self.assertEqual("YYOO", single_minute_row("12:32:00"))

    def test_to_43(self):
        self.assertEqual("YYYO", single_minute_row("12:43:00"))

    def test_to_26(self):
        self.assertEqual("YOOO", single_minute_row("12:26:00"))

    def test_parse_time_to_single_minute(self):
        self.assertEqual(32, extract_single_minute("12:32:00"))


if __name__ == '__main__':
    unittest.main()
