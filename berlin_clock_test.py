import unittest


def single_minute_row(time):
    minutes = extract_minutes(time)
    number_of_active_lights = minutes % 5
    return ("Y" * number_of_active_lights).ljust(4, 'O')


def extract_minutes(time):
    return int(time.split(":")[1])


def five_minutes_row(time):
    minutes = extract_minutes(time)
    lights_on = minutes // 5
    groups_with_red_light = lights_on // 3
    remaining_lights = lights_on % 3
    return ("YYR" * groups_with_red_light + "Y" * remaining_lights).ljust(11, "O")


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
        self.assertEqual(32, extract_minutes("12:32:00"))

    def test_something(self):
        self.assertEqual("OOOOOOOOOOO", five_minutes_row("00:00:00"))

    def test_something2(self):
        self.assertEqual("YYRYYRYYRYY", five_minutes_row("23:59:59"))

    def test_something3(self):
        self.assertEqual("YYRYOOOOOOO", five_minutes_row("12:23:00"))
        self.assertEqual("YYRYYRYOOOO", five_minutes_row("12:35:00"))
        self.assertEqual("YOOOOOOOOOO", five_minutes_row("12:05:00"))
        self.assertEqual("YYOOOOOOOOO", five_minutes_row("12:10:00"))
        self.assertEqual("YYROOOOOOOO", five_minutes_row("12:15:00"))


if __name__ == '__main__':
    unittest.main()
