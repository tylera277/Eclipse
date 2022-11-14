

import numpy as np

import math

from RoughTimeOfEclipses import RoughTimeOfEclipses


user_choice_of_eclipse = input("s for solar eclipse, l for lunar eclipse: ")
user_choice_of_year = int(input("Please enter the year:"))

if user_choice_of_eclipse == "s":
    RoughTimeOfEclipses(year=user_choice_of_year).predict_solar_eclipses()
elif user_choice_of_eclipse == "l":
    RoughTimeOfEclipses(year=user_choice_of_year).predict_lunar_eclipses()



