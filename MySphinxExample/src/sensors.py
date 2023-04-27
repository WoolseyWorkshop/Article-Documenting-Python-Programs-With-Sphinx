"""Defines the sensor classes.

Description
-----------

Defines the base and end user classes for various sensors.

- *Sensor* - The base sensor class.
- *TempSensor* - The temperature sensor class.

Libraries/Modules
-----------------

- *random* Standard Library (https://docs.python.org/3/library/random.html)
    - Provides access to the *randint* function.

Notes
-----

- Comments are Sphinx (reStructuredText) compatible.

TODO
----

- None.

Author(s)
---------

- Created by John Woolsey on 05/27/2020.
- Modified by John Woolsey on 04/21/2023.

Copyright (c) 2020 Woolsey Workshop.  All rights reserved.

Members
-------
"""


import random


class Sensor:
    """The sensor base class.

    Defines the base class utilized by all sensors.
    """

    def __init__(self, name: str) -> None:
        """The Sensor base class initializer.

        :param name: The name of the sensor.
        :type name:  str
        """

        self.name: str = name
        """The name of the sensor."""
        self.value: int = random.randint(0, 50)
        """The value of the sensor."""

    def __str__(self) -> str:
        """Retrieves the sensor's description.

        :return: A description of the sensor.
        :rtype:  str
        """

        return f"The {self.name} sensor has a value of {self.value}."


class TempSensor(Sensor):
    """The temperature sensor class.

    Provides access to the connected temperature sensor.

    Supported units are `"F"` (Fahrenheit), `"C"` (Celsius), and `"K"` (Kelvin).
    """

    def __init__(self, name, unit="F") -> None:
        """The TempSensor class initializer.

        :param name: The name of the temperature sensor.
        :type name:  str
        :param unit: The unit of the temperature sensor with values of
            `"F"`, `"C"`, or `"K"`; defaults to `"F"`.
        :type unit:  str
        """

        super().__init__(name)
        self.unit: str = unit
        """The temperature unit."""

    def __str__(self) -> str:
        """Retrieves the temperature sensor's description.

        :return: A description of the temperature sensor.
        """

        return (
            f"The {self.name} temperature sensor has a value of "
            f"{self.value} degrees {self.unit}."
        )
