
#############################
# ###### IMPORTS ####### #
import numpy as np

import math

from DistanceGetter import time_to_julian, julian_to_regular_time,\
    earth_to_moon, earth_to_sun
from jplephem.spk import SPK
#############################


class RoughTimeOfEclipses:

    def __init__(self, year):
        self.year = year
        self.radius_of_earth = 6371

    def predict_solar_eclipses(self):

        print("Calculating...")

        raw_time = [self.year, 1, 1, 0, 0, 0]

        julian_time_input = time_to_julian(raw_time)
        i = julian_time_input


        while i < (julian_time_input + 365):
            # print(i-julian_time_input)
            kernel = SPK.open('/Users/starman/Desktop/Eclipse/src/de440.bsp')

            earth_to_sun_array = earth_to_sun(julian_time=i, kernel=kernel)
            earth_to_moon_array = earth_to_moon(julian_time=i, kernel=kernel)

            e2s = earth_to_sun_array
            e2m = earth_to_moon_array

            theta = math.acos((np.dot(e2s, e2m)) / (np.sqrt(np.dot(e2m, e2m)) * np.sqrt(np.dot(e2s, e2s))))

            diff = np.sqrt(np.dot(e2m, e2m)) * math.sin(theta)

            if diff < self.radius_of_earth:
                if theta < (3.14159 / 2.0):
                    print("Solar:", julian_to_regular_time(i), ", ", diff)

            i += 0.1

        kernel.close()

    def predict_lunar_eclipses(self):

        print("Calculating...")

        raw_time = [self.year, 1, 1, 0, 0, 0]

        julian_time_input = time_to_julian(raw_time)
        i = julian_time_input

        kernel = SPK.open('/Users/starman/Desktop/Eclipse/src/de440.bsp')

        while i < (julian_time_input + 365):
            # print(i-julian_time_input)
            earth_to_sun_array = earth_to_sun(julian_time=i,kernel=kernel)
            earth_to_moon_array = earth_to_moon(julian_time=i, kernel=kernel)

            e2s = earth_to_sun_array
            e2m = earth_to_moon_array

            theta = math.acos((np.dot(e2s, e2m)) / (np.sqrt(np.dot(e2m, e2m)) * np.sqrt(np.dot(e2s, e2s))))

            diff = np.sqrt(np.dot(e2m, e2m)) * math.sin(theta)

            if diff < self.radius_of_earth:
                if theta > (3.14159 / 2.0):
                    print("Lunar:", julian_to_regular_time(i), ", ", diff)

            i += 0.1

        #kernel.close()