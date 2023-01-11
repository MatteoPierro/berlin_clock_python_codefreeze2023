import unittest


def single_minute_row(time):
    return "OOOO"


class MyTestCase(unittest.TestCase):
    def test_to_midnight(self):
        self.assertEqual("OOOO", single_minute_row("00:00:00"))


if __name__ == '__main__':
    unittest.main()
