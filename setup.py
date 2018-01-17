from setuptools import setup, find_packages

setup(name="RASPS",
      version=0.1,
      packages=find_packages(),
      scripts=["bin/serial_write.py", "bin/serial_read_server.py"],
      install_requires=["bokeh>=0.12.3",
                        "pyserial>=3.3"],
      author="Ola Skavhaug",
      author_email="ola@xal.no",
      url="https://github.com/expertanalytics/rasps",
      license="MIT")