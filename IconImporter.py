#! /usr/bin/env python
"""
IconImporter.py

This script converts old "icon file" format texture atlases into Portable
Network Graphics (PNG) format.

Copyright © 2020 by Richard Walters
"""

import png
import sys

# From: http://www.shikadi.net/moddingwiki/EGA_Palette
egaPalette = [
    (0x00, 0x00, 0x00), # black
    (0x00, 0x00, 0xAA), # blue
    (0x00, 0xAA, 0x00), # green
    (0x00, 0xAA, 0xAA), # cyan
    (0xAA, 0x00, 0x00), # red
    (0xAA, 0x00, 0xAA), # magenta
    (0xAA, 0x55, 0x00), # yellow / brown
    (0xAA, 0xAA, 0xAA), # white / light gray
    (0x55, 0x55, 0x55), # dark gray / bright black
    (0x55, 0x55, 0xFF), # bright blue
    (0x55, 0xFF, 0x55), # bright green
    (0x55, 0xFF, 0xFF), # bright cyen
    (0xFF, 0x55, 0x55), # bright red
    (0xFF, 0x55, 0xFF), # bright magenta
    (0xFF, 0xFF, 0x55), # bright yellow
    (0xFF, 0xFF, 0xFF), # bright white
]

def ParseWord(word):
    return int(word[0]) + int(word[1]) * 256

def Main(argv):
    if len(argv) < 3:
        print("usage: python IconImporter.py INPUT OUTPUT")
        print("")
        print("INPUT   Path to input file")
        print("OUTPUT  Path to output file")
        print("")
        print("This script will convert an old 'icon file' to a PNG file.")
        return 1
    inputPath = argv[1]
    outputPath = argv[2]
    pixels = []
    with open(inputPath, "rb") as inputFile:
        header = inputFile.read(16)
        if (header[0:10] != b"ICON FILE\x00"):
            print("Input header mismatch!")
            return 2
        widthInBytes = ParseWord(header[10:12])
        widthInPixels = widthInBytes * 8
        heightInPixels = ParseWord(header[12:14])
        icons = ParseWord(header[14:16])
        print(f"{icons} icons, {widthInPixels}x{heightInPixels}")
        pixels = [[0 for x in range(widthInPixels * icons)] for y in range(heightInPixels)]
        for icon in range(icons):
            for plane in range(4):
                for y in range(heightInPixels):
                    for x in range(widthInBytes):
                        bits = int(inputFile.read(1)[0])
                        for bit in range(8):
                            if (bits >= 128):
                                pixels[y][icon * widthInPixels + x * 8 + bit] |= (1 << plane)
                            bits = (bits << 1) & 0xFF
        print(f"Successfully imported icons from {inputPath}")
    with open(outputPath, "wb") as outputFile:
        png.Writer(widthInPixels * icons, heightInPixels, palette=egaPalette).write(outputFile, pixels)
    print(f"Successfully exported icons to {outputPath}")

if __name__ == "__main__":
    exit(Main(sys.argv))
