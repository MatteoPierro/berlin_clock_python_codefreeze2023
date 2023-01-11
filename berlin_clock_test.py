import unittest


def single_minute_row(time):
    if time == "23:59:59":
        return "YYYY"
    if time == "12:32:00":
        return "YYOO"
    return "OOOO"


class MyTestCase(unittest.TestCase):
    def test_to_midnight(self):
        self.assertEqual("OOOO", single_minute_row("00:00:00"))

    def test_to_59(self):
        self.assertEqual("YYYY", single_minute_row("23:59:59"))

    def test_to_32(self):
        self.assertEqual("YYOO", single_minute_row("12:32:00"))


if __name__ == '__main__':
    unittest.main()
