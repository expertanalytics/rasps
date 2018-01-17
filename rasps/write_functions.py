import time
import serial
import math as m


def sine_writer(port: str, sleep_time: float=0.01) -> None:
    ser = serial.Serial(port=port,
                        baudrate=9600,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout=1)
    while True:
        t = time.time()
        f = m.sin(t)
        msg = "{} {}\n".format(t, f)
        print(msg)
        ser.write(msg.encode("utf-8"))
        time.sleep(sleep_time)
