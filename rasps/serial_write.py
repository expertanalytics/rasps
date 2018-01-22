#!/usr/bin/env python3

from rasps.rasps_ports import SENDER_PORT
from rasps.write_functions import sine_writer


def write_sine() -> None:
    sine_writer(SENDER_PORT)
