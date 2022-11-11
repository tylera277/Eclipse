
#############################
# ###### IMPORTS ####### #
import unittest
import os

from src.DistanceGetter import earth_to_sun, \
    earth_to_moon, time_to_julian


#############################


class DistanceGetterTests(unittest.TestCase):

    def test_julian_time(self):
        time = [2022, 11, 11, 10, 26, 0]
        calculated_julian_time = time_to_julian(time)


        expected_julian_time = 2459894.9347222
        decimalPlace = 7

        self.assertAlmostEqual(calculated_julian_time, expected_julian_time, decimalPlace)

    def test_earth_to_sun(self):
        # Julian time for: time = [2022, 11, 11, 10, 26, 0]
        # (year, month, day, hour, minute, second)
        julian_time = 2459894.9347222

        calculated_position_of_sun = earth_to_sun(julian_time=julian_time)
        expected_position_of_sun = [-9.777300637177825E+07, -1.020810456047095E+08, -4.425041605816688E+07]

        decimal_place = 1

        self.assertAlmostEqual(calculated_position_of_sun[0], expected_position_of_sun[0], decimal_place)
        self.assertAlmostEqual(calculated_position_of_sun[1], expected_position_of_sun[1], decimal_place)
        self.assertAlmostEqual(calculated_position_of_sun[2], expected_position_of_sun[2], decimal_place)

    def test_earth_to_moon(self):
        # Julian time for: time = [2022, 11, 11, 10, 26, 0]
        # (year, month, day, hour, minute, second)
        julian_time = 2459894.9347222

        calculated_position_of_moon = earth_to_moon(julian_time=julian_time)
        expected_position_of_moon = [5.111039648019476E+04, 3.545737775619901E+05, 1.793674236320691E+05]

        decimal_place = 2

        self.assertAlmostEqual(calculated_position_of_moon[0], expected_position_of_moon[0], decimal_place)
        self.assertAlmostEqual(calculated_position_of_moon[1], expected_position_of_moon[1], decimal_place)
        self.assertAlmostEqual(calculated_position_of_moon[2], expected_position_of_moon[2], decimal_place)
