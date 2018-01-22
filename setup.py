from setuptools import setup, find_packages

setup(name="RASPS",
      version=0.1,
      packages=find_packages(),
      entry_points={
                    "console_scripts": ["sine_writer = rasps.serial_write:write_sine",
                                        "serial_server = rasps.serial_read_server:main"]
                   },
      install_requires=["bokeh>=0.12.3",
                        "pyserial>=3.3"],
      author="Ola Skavhaug",
      author_email="ola@xal.no",
      url="https://github.com/expertanalytics/rasps",
      license="MIT")
