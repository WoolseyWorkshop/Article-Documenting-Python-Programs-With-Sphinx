#!/usr/bin/env python3

"""An example Python program with Sphinx style comments.

Description
-----------

An example Python program that demonstrates how to use Sphinx (reStructuredText)
style comments.

Libraries/Modules
-----------------

- *time* Standard Library (https://docs.python.org/3/library/time.html)
    - Provides access to the *sleep* function.
- *sensors* Module (local)
    - Provides access to the *Sensor* and *TempSensor* classes.

Notes
-----

- Comments are Sphinx (reStructuredText) compatible.

TODO
----

- None.

Author(s)
---------

- Created by John Woolsey on 05/27/2020.
- Modified by John Woolsey on 04/26/2023.

Copyright (c) 2020 Woolsey Workshop.  All rights reserved.

Members
-------
"""


# Imports
from time import sleep
import sensors


# Global Constants
DEBUG: bool = True
"""The mode of operation; `False` = normal, `True` = debug."""

MIN_BASE: int = 1
"""The minimum number to map."""

MAX_BASE: int = 10
"""The maximum number to map."""

MIN_MAPPED: int = 0
"""The minimum mapped value."""

MAX_MAPPED: int = 255
"""The maximum mapped value."""


# Functions
def map_range(number: float, in_min: float, in_max: float, out_min: float, out_max: float, constrained: bool = True) -> float:
    """Maps a value from one range to another.

    This function takes a value within an input range and maps it to the
    equivalent value within an output range, maintaining the relative position
    of the value within the range.

    :param number:      The value to be mapped.
    :type number:       float
    :param in_min:      The minimum value of the input range.
    :type in_min:       float
    :param in_max:      The maximum value of the input range.
    :type in_max:       float
    :param out_min:     The minimum value of the output range.
    :type out_min:      float
    :param out_max:     The maximum value of the output range.
    :type out_max:      float
    :param constrained: If `True`, the mapped value is constrained to the output
        range; default is `True`.
    :type constrained:  bool

    :return: The mapped value.
    :rtype:  float
    """

    mapped = out_min
    if in_max - in_min != 0:
        mapped = (number - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    if out_min <= out_max:
        mapped = max(min(mapped, out_max), out_min)
    else:
        mapped = min(max(mapped, out_max), out_min)
    return mapped


def main() -> None:
    """The main program entry."""

    if DEBUG:
        print("Running in DEBUG mode.  Turn off for normal operation.")

    # Map numbers
    for i in range(MIN_BASE, MAX_BASE + 1):
        print(
            f"Base: {i:2d}, Mapped: "
            f"{round(map_range(i, MIN_BASE, MAX_BASE, MIN_MAPPED, MAX_MAPPED)):3d}"
        )
        sleep(0.25)  # wait 250 milliseconds

    # Sensors
    sensor: int = sensors.Sensor("MySensor")
    print(sensor)
    temp_in: int = sensors.TempSensor("Inside")
    print(temp_in)
    temp_out: int = sensors.TempSensor("Outside", "C")
    print(temp_out)


if __name__ == "__main__":  # required for generating Sphinx documentation
    main()
