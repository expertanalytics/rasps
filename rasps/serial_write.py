#!/usr/bin/env python3

import time
import serial
import math as m
from .rasps_ports import SENDER_PORT


def main():
    ser = serial.Serial(port=SENDER_PORT,
                        baudrate=9600,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout=1)
    while True:
        t = time.time()
        f = m.sin(t)
        ser.write("{} {}\n".format(t, f).encode("utf-8"))
        time.sleep(0.01)


if __name__ == "__main__":
    main()
