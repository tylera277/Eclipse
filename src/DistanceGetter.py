
#############################
# ###### IMPORTS ####### #
import datetime
import math
import os

import numpy as np
import pandas as pd

from datetime import timedelta, timezone, datetime
from jplephem.spk import SPK
#############################


def time_to_julian(time):

    ts = pd.Timestamp(year=time[0], month=time[1], day=time[2],
                      hour=time[3], minute=time[4], second=time[5],
                      tz='Etc/GMT')

    return ts.to_julian_date()


def julian_day_number_to_gregorian(jdn):
    """Convert the Julian Day Number to the proleptic Gregorian Year, Month, Day.
    This function is taken from https://orbital-mechanics.space/reference/julian-date.html """
    L = jdn + 68569
    N = int(4 * L / 146_097)
    L = L - int((146097 * N + 3) / 4)
    I = int(4000 * (L + 1) / 1_461_001)
    L = L - int(1461 * I / 4) + 31
    J = int(80 * L / 2447)
    day = L - int(2447 * J / 80)
    L = int(J / 11)
    month = J + 2 - 12 * L
    year = 100 * (N - 49) + I + L
    return year, month, day


def julian_to_regular_time(julian_time):
    """Convert a decimal Julian Date to the equivalent proleptic Gregorian date and time.
    This function is taken from https://orbital-mechanics.space/reference/julian-date.html """
    jdn = int(julian_time)
    if jdn < 1_721_426:
        raise ValueError("Julian Day Numbers less than 1,721,426 are not supported, "
                         "because Python's date class cannot represent years before "
                         "AD 1.")
    year, month, day = julian_day_number_to_gregorian(jdn)
    offset = timedelta(days=(julian_time % 1), hours=+12)
    dt = datetime(year=year, month=month, day=day, tzinfo=timezone.utc)
    return dt + offset


def earth_to_sun(julian_time, kernel):


    # Solar-system barycenter to earth-moon barycenter
    earth_to_sun_center = kernel[0, 3].compute(julian_time)
    # solar-system barycenter to sun center
    earth_to_sun_center -= kernel[0, 10].compute(julian_time)
    # earth-moon barycenter to earth center
    earth_to_sun_center += kernel[3, 399].compute(julian_time)

    kernel.close()

    return (-earth_to_sun_center)


def earth_to_moon(julian_time, kernel):

    earth_to_moon_center = kernel[3, 301].compute(julian_time)
    earth_to_moon_center -= kernel[3, 399].compute(julian_time)

    kernel.close()

    return earth_to_moon_center











