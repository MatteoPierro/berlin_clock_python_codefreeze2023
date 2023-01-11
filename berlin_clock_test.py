import unittest


def single_minute_row(time):
    minutes = extract_minutes(time)
    number_of_active_lights = minutes % 5
    return ("Y" * number_of_active_lights).ljust(4, 'O')


def extract_minutes(time):
    return int(time.split(":")[1])


def extract_hours(time):
    return int(time.split(":")[0])


def five_minutes_row(time):
    minutes = extract_minutes(time)
    lights_on = minutes // 5
    groups_with_red_light = lights_on // 3
    remaining_lights = lights_on % 3
    return ("YYR" * groups_with_red_light + "Y" * remaining_lights).ljust(11, "O")


def single_hour_row(time):
    hours = extract_hours(time)
    number_of_active_lights = hours % 5
    return ("R" * number_of_active_lights).ljust(4, 'O')


def five_hours_row(time):
    hours = extract_hours(time)
    number_of_active_lights = hours // 5
    return ("R" * number_of_active_lights).ljust(4, 'O')


class MyTestCase(unittest.TestCase):
    def test_extract_minutes(self):
        self.assertEqual(32, extract_minutes("12:32:00"))

    def test_extract_hours(self):
        self.assertEqual(12, extract_hours("12:32:00"))

    def test_single_minutes_row(self):
        self.assertEqual("OOOO", single_minute_row("00:00:00"))
        self.assertEqual("YYYY", single_minute_row("23:59:59"))
        self.assertEqual("YYOO", single_minute_row("12:32:00"))
        self.assertEqual("YYYO", single_minute_row("12:43:00"))
        self.assertEqual("YOOO", single_minute_row("12:26:00"))

    def test_five_minutes_row(self):
        self.assertEqual("OOOOOOOOOOO", five_minutes_row("00:00:00"))
        self.assertEqual("YYRYYRYYRYY", five_minutes_row("23:59:59"))
        self.assertEqual("YYRYOOOOOOO", five_minutes_row("12:23:00"))
        self.assertEqual("YYRYYRYOOOO", five_minutes_row("12:35:00"))
        self.assertEqual("YOOOOOOOOOO", five_minutes_row("12:05:00"))
        self.assertEqual("YYOOOOOOOOO", five_minutes_row("12:10:00"))
        self.assertEqual("YYROOOOOOOO", five_minutes_row("12:15:00"))

    def test_single_hour_row(self):
        self.assertEqual("OOOO", single_hour_row("00:00:00"))
        self.assertEqual("RRRO", single_hour_row("23:59:59"))
        self.assertEqual("RROO", single_hour_row("02:04:00"))
        self.assertEqual("ROOO", single_hour_row("06:04:00"))
        self.assertEqual("RRRR", single_hour_row("14:35:00"))

    def test_five_hours_row(self):
        self.assertEqual("OOOO", five_hours_row("00:00:00"))
        self.assertEqual("RRRR", five_hours_row("23:59:59"))
        self.assertEqual("ROOO", five_hours_row("08:23:00"))
        self.assertEqual("RROO", five_hours_row("10:23:00"))
        self.assertEqual("RRRO", five_hours_row("15:23:00"))


if __name__ == '__main__':
    unittest.main()
