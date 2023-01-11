import unittest


def single_minute_row(time):
    return "OOOO"


class MyTestCase(unittest.TestCase):
    def test_something(self):
        time = "00:00:00"
        self.assertEqual("OOOO", single_minute_row(time))


if __name__ == '__main__':
    unittest.main()
