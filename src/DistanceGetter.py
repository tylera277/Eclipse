
#############################
# Imports
import datetime
import math
import os

import numpy as np
import pandas as pd

from jplephem.spk import SPK
#############################


def time_to_julian(time):

    ts = pd.Timestamp(year=time[0], month=time[1], day=time[2],
                      hour=time[3], minute=time[4], second=time[5],
                      tz='Etc/GMT')

    return ts.to_julian_date()


def earth_to_sun(julian_time):
    kernel = SPK.open('/Users/starman/Desktop/Eclipse/src/de440.bsp')

    # Solar-system barycenter to earth-moon barycenter
    earth_to_sun_center = kernel[0, 3].compute(julian_time)
    # solar-system barycenter to sun center
    earth_to_sun_center -= kernel[0, 10].compute(julian_time)
    # earth-moon barycenter to earth center
    earth_to_sun_center += kernel[3, 399].compute(julian_time)

    kernel.close()

    return (-earth_to_sun_center)


def earth_to_moon(julian_time):
    kernel = SPK.open('/Users/starman/Desktop/Eclipse/src/de440.bsp')

    earth_to_moon_center = kernel[3, 301].compute(julian_time)
    earth_to_moon_center -= kernel[3, 399].compute(julian_time)

    kernel.close()

    return earth_to_moon_center











