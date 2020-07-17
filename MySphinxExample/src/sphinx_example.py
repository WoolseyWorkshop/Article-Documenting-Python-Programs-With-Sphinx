#!/usr/bin/env python3

"""Example Python program with Sphinx style comments.

Description
-----------

Example Python program with Sphinx style (reStructuredText) comments.

Libraries/Modules
-----------------

- time standard library (https://docs.python.org/3/library/time.html)
    - Access to sleep function.
- sensors module (local)
    - Access to Sensor and TempSensor classes.

Notes
-----

- Comments are Sphinx (reStructuredText) compatible.

TODO
----

- None.

Author(s)
---------

- Created by John Woolsey on 05/27/2020.
- Modified by John Woolsey on 07/02/2020.

Copyright (c) 2020 Woolsey Workshop.  All rights reserved.

Members
-------
"""


# Imports
from time import sleep
import sensors


# Global Constants
DEBUG = 1
"""The mode of operation; 0 = normal, 1 = debug."""
MIN_BASE = 1
"""The minimum number to map."""
MAX_BASE = 10
"""The maximum number to map."""
MIN_MAPPED = 0
"""The minimum mapped value."""
MAX_MAPPED = 255
"""The maximum mapped value."""


# Functions
def init():
    """Initializes the program."""

    if DEBUG:
        print("Initializing program.")


def map_range(number, in_min, in_max, out_min, out_max):
    """Maps a number from one range to another.

    :param number:  The input number to map.
    :param in_min:  The minimum value of an input number.
    :param in_max:  The maximum value of an input number.
    :param out_min: The minimum value of an output number.
    :param out_max: The maximum value of an output number.

    :return: The mapped number.
    """

    mapped = (number - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    if out_min <= out_max:
        return max(min(mapped, out_max), out_min)
    return min(max(mapped, out_max), out_min)


def main():
    """Main program entry."""

    init()  # program initialization

    # Map numbers
    for i in range(MIN_BASE, MAX_BASE + 1):
        print(
            f"Base: {i:2d}, Mapped: "
            f"{map_range(i, MIN_BASE, MAX_BASE, MIN_MAPPED, MAX_MAPPED):5.1f}"
        )
        sleep(0.25)  # wait 250 milliseconds

    # Sensors
    sensor = sensors.Sensor("MySensor")
    print(sensor)
    temp_in = sensors.TempSensor("Inside")
    print(temp_in)
    temp_out = sensors.TempSensor("Outside", "C")
    print(temp_out)
    temp_out.set_unit("K")
    print(temp_out)


if __name__ == "__main__":
    main()
