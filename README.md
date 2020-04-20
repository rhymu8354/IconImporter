# IconImporter

This is a file format conversion script.  For input, it takes the old "icon
file" format which the author used in the past to store texture atlases for
graphics drawn using the
[Enhanced Graphics Adapter (EGA)](https://en.wikipedia.org/wiki/Enhanced_Graphics_Adapter)
for PCs in the 1980s.  For output, it writes the same texture atlas in
[Portable Network Graphics (PNG)](https://en.wikipedia.org/wiki/Portable_Network_Graphics)
format, as an image with all the "icons" in a single row (meaning the image
height is the icon height, and the image width is the icon width multiplied by
the number of icons).

## Usage

    python IconImporter.py INPUT OUTPUT

    INPUT   Path to input file
    OUTPUT  Path to output file

    This script will convert an old 'icon file' to a PNG file.

## Supported platforms / recommended toolchains

This is a Python script designed to work with Python 3.  It should work on any
platform which supports Python 3.  The version of Python used during the
development of the script was Python 3.7.0.

## Prerequisites

* [Python](https://www.python.org/) version 3 (or higher, hopefully).
* [PyPNG](https://pypi.org/project/pypng/) -- Python library which allows PNG
  image files to be read and written
  * This command may be used to install the library: `pip install
  pypng`
