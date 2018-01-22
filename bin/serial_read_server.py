#!/usr/bin/env python3

from tornado.ioloop import IOLoop
from bokeh.application.handlers import FunctionHandler
from bokeh.application import Application
from bokeh.server.server import Server

from bokeh.models.ranges import DataRange1d
from bokeh.plotting import figure, curdoc, ColumnDataSource
from rasps.rasps_ports import RECIEVER_PORT
import serial


def read_value_pair(ser):
    msg = ser.readline().decode("utf-8")
    t, f = [float(_) for _ in msg.split()]
    return 1000*t, f


def make_document(doc):
    ser = serial.Serial(port=RECIEVER_PORT,
                        baudrate=9600,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout=2)

    t0, f0 = read_value_pair(ser)
    t1, f1 = read_value_pair(ser)

    source = ColumnDataSource(data=dict(time=[t0, t1], y=[f0, f1]))

    x_range = DataRange1d(follow="end", follow_interval=20000, range_padding=0)

    fig = figure(title="Value sniffer", x_axis_type="datetime", height=150,
                 tools="", x_range=x_range, y_range=[-1.1, 1.1])
    fig.line(x="time", y="y", source=source, line_width=3, line_alpha=0.6)
    fig.yaxis.minor_tick_line_color = None
    doc.add_root(fig)

    def update():
        t, f = read_value_pair(ser)
        source.stream({"time": [t], "y": [f]}, 200)

    doc.add_periodic_callback(update, 1)


def main():
    io_loop = IOLoop.current()
    bapp = Application(FunctionHandler(make_document))
    server = Server({"/": bapp}, io_loop=io_loop, extra_websocket_origins=["*"], port=8000)
    server.start()
    io_loop.add_callback(server.show, "/")
    io_loop.start()


if __name__ == "__main__":
    main()
#else:
#    make_document(curdoc())
