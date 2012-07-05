#!/usr/bin/python
#
# invoked by the Makefile

import fontforge
import os
import sys

def generate(font, path):
    extension = os.path.splitext(outfilepath)[1]

    font.selection.all()
    font.autoHint()

    if extension == '.ttf':
        font.correctReferences()
        font.em = 2048
        font.round()

    font.generate(path)


if len(sys.argv) > 3:
    infilepath = sys.argv[1]
    outfilepath = sys.argv[2]
    version = sys.argv[3]

    font = fontforge.open(infilepath)
    font.version = version

    generate(font, outfilepath)
