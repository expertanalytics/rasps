#!/usr/bin/env python3

from rasps.rasps_ports import SENDER_PORT
from rasps.write_functions import sine_writer


if __name__ == "__main__":
    sine_writer(SENDER_PORT)
