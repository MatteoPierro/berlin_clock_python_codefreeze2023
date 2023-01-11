import unittest

MAXIMUM_MINUTES_IN_FIVE_MINUTES_ROW = 55


def single_minute_row(time):
    minutes = extract_minutes(time)
    number_of_active_lights = minutes % 5
    return ("Y" * number_of_active_lights).ljust(4, 'O')


def extract_seconds(time):
    return int(time.split(":")[2])


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


def second_light(time):
    seconds = extract_seconds(time)
    if seconds % 2:
        return "O"
    return "Y"


def convert_to_berlin_clock(time):
    return "".join([
        second_light(time),
        five_hours_row(time),
        single_hour_row(time),
        five_minutes_row(time),
        single_minute_row(time)
    ])


def berlin_to_digital(berlin_clock):
    number_of_hours = hours_from(berlin_clock)
    hours = str(number_of_hours).rjust(2, "0")

    number_of_minutes = minutes_from(berlin_clock)
    minutes = str(number_of_minutes).rjust(2, "0")

    return f"{hours}:{minutes}:00"


def minutes_from(berlin_clock):
    five_minutes = berlin_clock[9:20]
    single_minutes = berlin_clock[20:24]
    five_minutes_lights_off = five_minutes.count("O")
    single_minutes_lights_on = single_minutes.count("Y")
    return MAXIMUM_MINUTES_IN_FIVE_MINUTES_ROW - (five_minutes_lights_off * 5) + single_minutes_lights_on


def hours_from(berlin_clock):
    five_hours = berlin_clock[1:5]
    single_hours = berlin_clock[5:9]
    return five_hours.count("R") * 5 + single_hours.count("R")


class MyTestCase(unittest.TestCase):

    def test_extract_seconds(self):
        self.assertEqual(13, extract_seconds("12:32:13"))

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

    def test_second_light(self):
        self.assertEqual("Y", second_light("00:00:00"))
        self.assertEqual("O", second_light("00:00:01"))
        self.assertEqual("Y", second_light("00:00:04"))
        self.assertEqual("O", second_light("23:59:59"))

    def test_convert_to_berlin_clock(self):
        self.assertEqual("YOOOOOOOOOOOOOOOOOOOOOOO", convert_to_berlin_clock("00:00:00"))
        self.assertEqual("ORRRRRRROYYRYYRYYRYYYYYY", convert_to_berlin_clock("23:59:59"))
        self.assertEqual("YRRROROOOYYRYYRYYRYOOOOO", convert_to_berlin_clock("16:50:06"))
        self.assertEqual("ORROOROOOYYRYYRYOOOOYYOO", convert_to_berlin_clock("11:37:01"))

    def test_berlin_to_digital(self):
        self.assertEqual("00:00:00", berlin_to_digital("YOOOOOOOOOOOOOOOOOOOOOOO"))
        self.assertEqual("05:00:00", berlin_to_digital("YROOOOOOOOOOOOOOOOOOOOOO"))
        self.assertEqual("10:00:00", berlin_to_digital("YRROOOOOOOOOOOOOOOOOOOOO"))
        self.assertEqual("15:00:00", berlin_to_digital("YRRROOOOOOOOOOOOOOOOOOOO"))
        self.assertEqual("01:00:00", berlin_to_digital("Y000OROOOOOOOOOOOOOOOOOO"))
        self.assertEqual("00:05:00", berlin_to_digital(convert_to_berlin_clock("00:05:00")))
        self.assertEqual("00:10:00", berlin_to_digital(convert_to_berlin_clock("00:10:00")))
        self.assertEqual("00:01:00", berlin_to_digital(convert_to_berlin_clock("00:01:00")))


if __name__ == '__main__':
    unittest.main()
